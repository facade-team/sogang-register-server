from main import db
from main.model.user import User
from main.model.user_subject import UserSubject
from main.model.user_complete import UserComplete
import string, random

from ..service.mailer_service import sendmail

# 회원가입한 회원 정보를 user모델(즉, user테이블에 넣기)
def search_email(data):
    # email, name 으로 존재하는지 찾고 메일 보내기
    username = data['username']
    useremail = data['email']

    try:
        user = User.query.filter_by(email=useremail).first()
        if not user:
            response_object = {
                'status': 'fail',
                'message': '해당하는 email이 존재하지 않습니다.'
            }
            db.session.close()
            return response_object, 402
        else:
            if username == user.username : 
                # email, name matched.
                response_object = {
                    'status': 'success',
                    'message': '해당하는 이메일이 존재합니다.'
                }
                db.session.close()
                return response_object, 201
            else:
                # email 은 존재, 이름이 틀린 경우
                response_object = {
                    'status': 'fail',
                    'message': 'email과 이름이 매칭되지 않습니다.'
                }
                db.session.close()
                return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def search_password(data):
    # email, name 으로 존재하는지 찾고 메일 보내기
    username = data['username']
    useremail = data['email']

    try:
        user = User.query.filter_by(email=useremail).first()
        if not user:
            response_object = {
                'status': 'fail',
                'message': '해당하는 email이 존재하지 않습니다.'
            }
            db.session.close()
            return response_object, 402
        else:
            if username == user.username :
                # email, name matched. 임시 password email로 전송.
                temp = random_generator(12)
                # db 수정

                if set_password(user,temp):
                    # 해당 회원의 email로 임시 비번 전송
                    mail_object = {
                        'email': useremail,
                        'script': temp,
                        'purpose': 'password'
                    }
                    sendmail(mail_object)
                    response_object = {
                        'status': 'success',
                        'message': '해당하는 이메일로 임시 password를 전송했습니다.'
                    }
                    db.session.close()
                    return response_object, 201
                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'db 접속 실패'
                    }
                    db.session.close()
                    return response_object, 411
            else:
                # email 은 존재, 이름이 틀린 경우
                response_object = {
                    'status': 'fail',
                    'message': 'email과 이름이 매칭되지 않습니다.'
                }
                db.session.close()
                return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def set_password(user, pwd):
    try:
        user.password = pwd
        db.session.commit()
        return True
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def change_password(user_email,data):
    # old 패스워드 맞는지 확인
    try:
        user = User.query.filter_by(email=user_email).first()
        if user and user.check_password(data['old_password']):
            set_password(user,data['new_password'])
            response_object = {
                'status': 'success',
                'message': '새로운 비밀번호로 변경되었습니다.'
            }
            db.session.close()
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': '이전 비밀번호가 일치하지 않습니다.'
            }
            db.session.close()
            return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def dropout(user_email,data):
    try:
        # name, password까지 체크 필요
        user = User.query.filter_by(email=user_email).first()
        if user and user.check_password(data['password']):
            if user.username == data['username']:
                # db 테이블에서 삭제
                db.session.delete(user)
                db.session.commit()
                db.session.close()
                
                favorite = UserSubject.query.filter_by(email=user_email).all()
                if favorite:
                    for i in favorite:
                        db.session.delete(i)
                        db.session.commit()
                        db.session.close()
                
                compelete = UserComplete.query.filter_by(email=user_email).all()
                if compelete:
                    for i in compelete:
                        db.session.delete(i)
                        db.session.commit()
                        db.session.close()

                response_object = {
                    'status': 'success',
                    'message': '회원 탈퇴 되었습니다.'
                }
                db.session.close()
                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': '입력한 form에서 이름이 일치하지 않은 경우'
                }
                db.session.close()
                return response_object, 402
        else:
            response_object = {
                'status': 'fail',
                'message': '비밀번호가 일치하지 않습니다.'
            }
            db.session.close()
            return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()
    

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()
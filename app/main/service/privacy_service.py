from main import db
from main.model.user import User
import string, random

from ..service.mailer_service import sendmail

# 회원가입한 회원 정보를 user모델(즉, user테이블에 넣기)
def search_email(data):
    # email, name 으로 존재하는지 찾고 메일 보내기
    username = data['username']
    useremail = data['email']

    user = User.query.filter_by(email=useremail).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': '해당하는 email이 존재하지 않습니다.'
        }
        return response_object, 409
    else:
        if username == user.username : 
            # email, name matched.
            response_object = {
                'status': 'success',
                'message': '해당하는 이메일이 존재합니다.'
            }
            return response_object, 201
        else:
            # email 은 존재, 이름이 틀린 경우
            response_object = {
                'status': 'fail',
                'message': 'email과 이름이 매칭되지 않습니다.'
            }
            return response_object, 410

def search_password(data):
    # email, name 으로 존재하는지 찾고 메일 보내기
    username = data['username']
    useremail = data['email']

    user = User.query.filter_by(email=useremail).first()
    if not user:
        response_object = {
            'status': 'fail',
            'message': '해당하는 email이 존재하지 않습니다.'
        }
        return response_object, 409
    else:
        if username == user.username :
            # email, name matched. 임시 password email로 전송.
            temp = random_generator()
            # db 수정

            if set_password(user,temp):
                # 해당 회원의 email로 임시 비번 전송
                mail_object = {
                    'email': useremail,
                    'script': temp
                }
                sendmail(mail_object)

                response_object = {
                    'status': 'success',
                    'message': '해당하는 이메일로 임시 password를 전송했습니다.'
                }
                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'db 접속 실패'
                }
                return response_object, 411
        else:
            # email 은 존재, 이름이 틀린 경우
            response_object = {
                'status': 'fail',
                'message': 'email과 이름이 매칭되지 않습니다.'
            }
            return response_object, 410

def set_password(user, pwd):
    try:
        user.password = pwd
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

def change_password(data):
    # token 검증
    
    # 패스워드 변경 se

    return 'password change', 201
def dropout(data):
    #
    return 'dropout'

def random_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def save_changes(data):
    db.session.add(data)
    db.session.commit()
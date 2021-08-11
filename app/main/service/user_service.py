#user 모델에 관련된 쿼리문 작성 파일
import uuid
import datetime
from sqlalchemy.orm import noload

from sqlalchemy.sql.elements import Null
from main import db
from main.model.user import User
from main.model.issue import Report

from ..service.mailer_service import sendmail
# email 형식 틀린 것 걸러내기
import re
from ..service.privacy_service import random_generator

# 회원가입한 회원 정보를 user모델(즉, user테이블에 넣기)
def save_new_user(data):
    # 맞는 email 형식인지 먼저 체크
    try:
        if checkmail(data['email']):
            user = User.query.filter_by(email=data['email']).first()
            # db에 중복되는 email 주소 없음.
            if not user:
                majorparse = ' '.join(data['major'])
                new_user = User(
                    email=data['email'],
                    username=data['username'],
                    password=data['password'],
                    registered_on=datetime.datetime.utcnow(),
                    major=majorparse,
                    allow_email=data['allow_email']
                )
                save_changes(new_user)
                response_object = {
                    'status': 'success',
                    'message': '회원가입 되었습니다.'
                }
                db.session.close()
                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': '이미 가입된 email 주소입니다.',
                }
                db.session.close()
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': '입력한 email 주소는 맞는 형식이 아닙니다.'
            }
            db.session.close()
            return response_object,402
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def allow_email(email, data):
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            user.allow_email = data['allow_email']
            user.major = ' '.join(data['major'])
            db.session.commit()
            db.session.close()
            response_object = {
                'status': 'success',
                'message': '해당 유저의 전공 변경 및 이메일 동의 여부 변경'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': '존재하지 않는 유저'
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

def gen_secret_code(email):
    temp = random_generator(6)
    # db에 임시 코드 저장
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            user.verify_code = temp
            db.session.commit()
            db.session.close()

            email_object = {
                'purpose': 'register',
                'email': email,
                'script': temp
            }
            # email로 전송
            sendmail(email_object)
            response_object = {
                'status': 'success',
                'message': '인증 코드 발송 성공'
            }
            db.session.close()
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': '해당 email이 존재하지 않습니다.'
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

def verify_a_user(data):
    try:
        user = User.query.filter_by(email=data['email']).first()
        if user:
            if user.verify_code == data['script']:
                user.verify_on = True
                # 인증 완료 한 후 인증 코드 column 초기화
                user.verify_code = None
                db.session.commit()
                db.session.close()

                response_object = {
                    'status': 'success',
                    'message': '해당 유저 이메일 인증 성공'
                }
                db.session.close()
                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': '잘못된 인증 코드를 입력했습니다.'
                }
                db.session.close()
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': '해당하는 이메일이 존재하지 않습니다.'
            }
            db.session.close()
            return response_object, 402
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

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

# email 형식 체크
def checkmail(email):
    p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    result = p.match(email) != None
    
    #True, False로 return
    return result

def can_use(email):
    try:
        if checkmail(email):
            user = User.query.filter_by(email=email).first()
            if not user:
                response_object = {
                        'status': 'success',
                        'message': '사용 가능한 email 입니다.'
                    }
                db.session.close()
                return response_object, 201
            else:
                response_object = {
                        'status': 'fail',
                        'message': '중복된 email 입니다.'
                    }
                db.session.close()
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': '입력한 email 주소는 맞는 형식이 아닙니다.'
            }
            db.session.close()
            return response_object, 402
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()
        
def get_user(email):
    try:
        user = User.query.filter_by(email=email).first()
        if user:
            major = "전공없음"
            if user.major:
                major = user.major.split(' ')
            
            response_object = {
                'status': 'success',
                'message': '회원 조회에 성공했습니다.',
                'data': {
                    'email' : user.email,
                    'username' : user.username,
                    'major' : major,
                    'allow_email': user.allow_email,
                    'verify_on': user.verify_on
                }
            }
            db.session.close()
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': '해당 회원이 없습니다.',
                'data': {
                    'major': 'no user'
                }
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

def report(sender,data,flag):
    try:
        newReport = Report(
            email = data['email'],
            title = data['title'],
            script = data['script'],
            useremail = None
        )
        if flag == True:
            newReport.useremail = sender
        
        db.session.add(newReport)
        db.session.commit()
        db.session.close()
        
        response_object = {
            'status': 'success',
            'message': '문의가 접수되었습니다.'
        }
        return response_object, 201
    except Exception as e:
        response_object = {
                'status': 'error',
                'message': str(e)
            }
        return response_object, 500
    finally:
        db.session.close()
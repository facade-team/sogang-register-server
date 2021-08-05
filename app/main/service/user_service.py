#user 모델에 관련된 쿼리문 작성 파일
import uuid
import datetime

from sqlalchemy.sql.elements import Null
from main import db
from main.model.user import User

from ..service.mailer_service import sendmail
# email 형식 틀린 것 걸러내기
import re
from ..service.privacy_service import random_generator

# 회원가입한 회원 정보를 user모델(즉, user테이블에 넣기)
def save_new_user(data):
    # 맞는 email 형식인지 먼저 체크
    if checkmail(data['email']):
        user = User.query.filter_by(email=data['email']).first()
        # db에 중복되는 email 주소 없음.
        if not user:
            majorparse = ' '.join(data['major'])
            print(majorparse)
            new_user = User(
                public_id=str(uuid.uuid4()),
                email=data['email'],
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow(),
                major=majorparse
            )
            save_changes(new_user)
            response_object = {
                'status': 'success',
                'message': '회원가입 되었습니다.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': '이미 가입된 email 주소입니다.',
            }
            return response_object, 401
    else:
        response_object = {
            'status': 'fail',
            'message': '입력한 email 주소는 맞는 형식이 아닙니다.'
        }
        return response_object,402

def gen_secret_code(email):
    temp = random_generator(6)

    # db에 임시 코드 저장
    user = User.query.filter_by(email=email).first()
    if user :
        user.verify_code = temp
        db.session.commit()

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
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': '해당 email이 존재하지 않습니다.'
        }
        return response_object, 401

def verify_a_user(data):
    user = User.query.filter_by(email=data['email']).first()
    
    if user:
        if user.verify_code == data['script']:
            user.verify_on = True
            db.session.commit()

            # 인증 완료 한 후 인증 코드 column 초기화
            user.verify_code = None
            db.session.commit()

            response_object = {
                'status': 'success',
                'message': '해당 유저 이메일 인증 성공'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': '잘못된 인증 코드를 입력했습니다.'
            }
            return response_object, 401
    else:
        response_object = {
            'status': 'fail',
            'message': '해당하는 이메일이 존재하지 않습니다.'
        }
        return response_object, 402

def save_changes(data):
    db.session.add(data)
    db.session.commit()
    db.session.close()

# email 형식 체크
def checkmail(email):
    p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    result = p.match(email) != None
    
    #True, False로 return
    return result

def can_use(email):
    if checkmail(email):
        user = User.query.filter_by(email=email).first()
        if not user:
            response_object = {
                    'status': 'success',
                    'message': '사용 가능한 email 입니다.'
                }
            return response_object, 201
        else:
            response_object = {
                    'status': 'fail',
                    'message': '중복된 email 입니다.'
                }
            return response_object, 401
    else:
        response_object = {
            'status': 'fail',
            'message': '입력한 email 주소는 맞는 형식이 아닙니다.'
        }
        return response_object, 402

# def get_a_user(public_id):
#     return User.query.filter_by(public_id=public_id).first()
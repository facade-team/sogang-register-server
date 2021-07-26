#user 모델에 관련된 쿼리문 작성 파일
import uuid
import datetime
from main import db
from main.model.user import User

from ..service.mailer_service import sendmail
# email 형식 틀린 것 걸러내기
import re

def generate_token(user):
    try:
        # generate the auth token
        auth_token = user.encode_auth_token(user.id)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.',
            'Authorization': auth_token.decode()
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

# 회원가입한 회원 정보를 user모델(즉, user테이블에 넣기)
def save_new_user(data):
    # 맞는 form을 입력했는지 체크
    if data['email'] in data and data['username'] in data and data['password'] in data:
        # 맞는 email 형식인지 먼저 체크
        if checkmail(data['email']):
            user = User.query.filter_by(email=data['email']).first()
            # db에 중복되는 email 주소 없음.
            if not user:
                new_user = User(
                    public_id=str(uuid.uuid4()),
                    email=data['email'],
                    username=data['username'],
                    password=data['password'],
                    registered_on=datetime.datetime.utcnow()
                )
                save_changes(new_user)
                response_object = {
                    'status': 'success',
                    'message': '회원가입 되었습니다. '
                }
                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': '이미 가입된 email 주소입니다.',
                }
                return response_object, 409
        else:
            response_object = {
                'status': 'fail',
                'message': '입력한 email 주소는 맞는 형식이 아닙니다.'
            }
            return response_object,409
    else:
        response_object = {
            'status': 'fail',
            'message': '입력되지 않은 form이 있습니다.'
        }
        return response_object, 409


def get_all_users():
    return User.query.all()

def get_a_user(id):
    return User.query.filter_by(id=id).first()

def verify_a_user(data):
    # 인증 메일 보내기 전 이메일 형식 확인
    if checkmail(data['email']):
        sendmail(data = data)
        # 인증 메일을 보내고 난 후 인증 코드를 작성하고 post 한 후 상황
        # data 와 실제 메일로 발송한 인증 코드 비교
        # 맞을 경우 맞다고 return, 틀릴 경우 틀리다고 return.
    else:
        response_object = {
            'status': 'fail',
            'message': '입력한 email 주소는 맞는 형식이 아닙니다.'
        }
        return response_object, 409

def save_changes(data):
    db.session.add(data)
    db.session.commit()

# email 형식 체크
def checkmail(email):
    p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    result = p.match(email) != None
    
    #True, False로 return
    return result

def canuse(email):
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
            return response_object, 409
    else:
        response_object = {
            'status': 'fail',
            'message': '입력한 email 주소는 맞는 형식이 아닙니다.'
        }
        return response_object, 409

        




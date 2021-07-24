#user 모델에 관련된 쿼리문 작성 파일
from main import db
from main.model.user import User
import datetime

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

#회원가입한 회원 정볼를 user모델(즉, user테이블에 넣기)
def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
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


def get_all_users():
    return User.query.all()

def get_a_user(id):
    return User.query.filter_by(id=id).first()

def verify_a_user(data):
    # 인증 메일을 보내고 난 후 인증 코드를 작성하고 post 한 후 상황
    # data 와 실제 메일로 발송한 인증 코드 비교
    # 맞을 경우 맞다고 return, 틀릴 경우 틀리다고 return.
    return '인증되었습니다!'

def save_changes(data):
    db.session.add(data)
    db.session.commit() 
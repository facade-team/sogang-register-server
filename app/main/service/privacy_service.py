from main import db
from main.model.user import User

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
    try:
        # fetch the user data
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            # 여기서부터 토큰 부여하는 로직
            # jwt 형식으로 암호화해서 auth_token 생성
            auth_token = user.encode_auth_token(user)
            if auth_token:
                response_object = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'Authorization': auth_token
                    #user.decode_auth_token(auth_token)
                }
                return response_object, 201
            else:
                response_object = {
                'status': 'fail',
                'message': 'token 생성 실패'
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'email or password does not match.'
            }
            return response_object, 401
    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Try again',
        }
        return response_object, 500
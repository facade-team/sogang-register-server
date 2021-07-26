from app.main.model.user import User
from ..service.blacklist_service import save_token

class Auth:

    @staticmethod
    def login_user(data):
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
            

    @staticmethod
    def logout_user(data):
        # 로그인 안 한 상태에서 로그아웃 눌렀을 경우, auth_token은 ''
        if data:
            print(data)
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        
        if auth_token:
            # decode
            # decode 한 후 맞는 회원 정보인지 확인
            # exp, iat로 만료 시간 확인
            
            # 접근 권한 있는지 확인
            return 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403
from app.main.model.user import User

class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data['email']).first()
            if user and user.check_password(data['password']):
                # 인증 여부 확인
                if user.verify_on == True:
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
                    'message': '이메일 인증을 먼저 해 주세요'
                    }
                    return response_object, 402
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 403
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 404
            
    # token 유효성 판단. decode -> exp, iat 확인 -> true, false 리턴
    @staticmethod
    def middleware(data):
        # 로그인 안 한 상태에서 로그아웃 눌렀을 경우, auth_token은 ''
        if data:
            auth_token = data
        else:
            auth_token = ''
        
        if auth_token:
            # decode
            token = User.decode_auth_token(auth_token)
            # decode 한 후 맞는 회원 정보인지 확인
            user = User.query.filter_by(email=token['email']).first()
            if user:
                response_object = {
                        'status': 'success',
                        'message': 'token 인증이 완료되었습니다.',
                        'email': user.email
                    }
                return response_object
        else:
            response_object = {
                'status': 'fail',
                'message': 'Token이 존재하지 않습니다. 다시 로그인 해 주세요.'
            }
            return response_object, 403
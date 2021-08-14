from app.main.model.user import User
from app.main import db
from app.main.service.user_service import get_user
from app.main.service.user_subject_service import get_subjects

class Auth:
    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data['email']).first()
            if user and user.check_password(data['password']):
                # 인증 여부 확인
                if user.verify_on == True:
                    # 여기서부터 토큰 부여하는 로직
                    auth_token = user.encode_auth_token(user)
                    if auth_token:
                        user_data=get_user(data['email'])[0]['data']
                        user_data['Authorization'] = auth_token
                        user_favorite = get_subjects(data['email'])[0]['data']

                        response_object = {
                            'status': 'success',
                            'message': 'Successfully logged in.',
                            'data': user_data,
                            'favorites':user_favorite
                        }
                        #user.decode_auth_token(auth_token)
                        db.session.close()
                        return response_object, 201
                    else:
                        response_object = {
                        'status': 'fail',
                        'message': 'token 생성 실패'
                        }
                        db.session.close()
                        return response_object, 401
                else:
                    # 여기서부터 토큰 부여하는 로직
                    auth_token = user.encode_auth_token(user)
                    if auth_token:
                        user_data=get_user(data['email'])[0]['data']
                        user_data['Authorization'] = auth_token

                        response_object = {
                            'status': 'success',
                            'message': '인증은 안되어있지만 로그인 성공',
                            'data': user_data
                        }
                        db.session.close()
                        return response_object, 202
                    else:
                        response_object = {
                        'status': 'fail',
                        'message': 'token 생성 실패'
                        }
                        db.session.close()
                        return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                db.session.close()
                return response_object, 403
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': str(e)
            }
            db.session.close()
            return response_object, 404
        finally:
            db.session.close()
            
    # token 유효성 판단. decode -> exp, iat 확인 -> true, false 리턴
    @staticmethod
    def middleware(data):
        try:
            # 로그인 안 한 상태에서 로그아웃 눌렀을 경우, auth_token은 ''
            if data:
                auth_token = data
            else:
                auth_token = None
            
            if auth_token:
                # decode
                token = User.decode_auth_token(auth_token)
                if token:
                    # decode 한 후 맞는 회원 정보인지 확인
                    user = User.query.filter_by(email=token['email']).first()
                    if user:
                        response_object = {
                                'status': 'success',
                                'message': 'token 인증이 완료되었습니다.',
                                'email': user.email
                            }
                        db.session.close()
                        return response_object
                    else:
                        response_object = {
                          'status': 'fail',
                          'message': 'User가 존재하지 않습니다. 다시 로그인 해 주세요.'
                        }
                        db.session.close()
                        return response_object
                else:
                  response_object = {
                    'status': 'fail',
                    'message': "'{}'은 유효하지 않은 토큰입니다. 다시 로그인 해 주세요.".format(auth_token)
                  }
                  db.session.close()
                  return response_object
                  
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Token이 존재하지 않습니다. 다시 로그인 해 주세요.'
                }
                db.session.close()
                return response_object
        except Exception as e:
            response_object = {
                'status' : 'error',
                'message' : str(e)
            }
            return response_object
        finally:
            db.session.close()

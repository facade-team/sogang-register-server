from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    @api.response(201, 'Successfully logged in.')
    @api.response(401, 'token 생성 실패')
    @api.response(402, '이메일 인증을 먼저 해 주세요')
    @api.response(403, 'email or password does not match.')
    @api.response(404, 'Try again - DB 연결 Error')
    def post(self):
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)
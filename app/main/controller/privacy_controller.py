from flask import request
from flask_restx import Resource

from ..util.dto import PrivacyDto
from ..service.privacy_service import search_email, search_password, change_password, dropout

from app.main.service.auth_helper import Auth

# user dto
api = PrivacyDto.api
privacy = PrivacyDto.privacy
changepwd = PrivacyDto.changepwd
drop = PrivacyDto.drop

@api.route('/emailsearch')
class EmailSearch(Resource):
    @api.expect(privacy, validate=True)
    @api.response(201, 'Email successfully searched.')
    @api.doc('회원이 가입한 이메일을 찾으려고 하는 경우')
    def post(self):
        """Search User's Email"""
        data = request.json
        return search_email(data=data)

@api.route('/passwordreset')
class PasswordSearch(Resource):
    @api.expect(privacy, validate=True)
    @api.response(201, 'Password successfully reset.')
    @api.doc('회원이 가입한 비밀번호를 초기화 하는 경우')
    def post(self):
        """Reset User's Password"""
        data = request.json
        return search_password(data=data)

@api.route('/passwordchange')
class PasswordChange(Resource):
    @api.expect(changepwd, validate=True)
    @api.response(201, 'Password successfully changed.')
    @api.doc('회원이 가입한 비밀번호를 바꾸려고 하는 경우')
    def post(self):
        """Change User's Password"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return change_password(res['email'],data = data)

@api.route('/dropout')
class UserDropOut(Resource):
    @api.expect(drop, validate=True)
    @api.response(201, 'User successfully dropped out.')
    @api.doc('회원이 서비스를 탈퇴하는 경우')
    def post(self):
        """Drop User's data"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return dropout(res['email'],data = data)
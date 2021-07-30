from flask import request
from flask_restx import Resource

from ..util.dto import PrivacyDto
from ..service.privacy_service import search_email, search_password

# user dto
api = PrivacyDto.api
privacy = PrivacyDto.privacy

@api.route('/emailsearch')
class EmailSearch(Resource):
    @api.expect(privacy, validate=True)
    @api.response(201, 'Email successfully searched.')
    @api.doc('회원이 가입한 이메일을 찾으려고 하는 경우')
    def post(self):
        """Search User's Email"""
        data = request.json
        return search_email(data=data)

@api.route('/passwordsearch')
class PasswordSearch(Resource):
    @api.expect(privacy, validate=True)
    @api.response(201, 'Password successfully searched.')
    @api.doc('회원이 가입한 비밀번호를 찾으려고 하는 경우')
    def post(self):
        """Search User's Password"""
        data = request.json
        return search_password(data=data)
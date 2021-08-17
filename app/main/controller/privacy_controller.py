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

parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/emailsearch')
class EmailSearch(Resource):
    @api.expect(privacy, validate=True)
    @api.response(201, '해당하는 이메일이 존재합니다.')
    @api.response(401, 'email과 이름이 매칭되지 않습니다.')
    @api.response(402, '해당하는 email이 존재하지 않습니다.')
    @api.doc('회원이 가입한 이메일을 찾으려고 하는 경우')
    def post(self):
        """Search User's Email"""
        data = request.json
        return search_email(data=data)

@api.route('/passwordreset')
class PasswordSearch(Resource):
    @api.expect(privacy, validate=True)
    @api.response(201, '해당하는 이메일로 임시 password를 전송했습니다.')
    @api.response(411, 'db 접속 실패')
    @api.response(401, 'email과 이름이 매칭되지 않습니다.')
    @api.response(402, '해당하는 email이 존재하지 않습니다.')
    @api.doc('회원이 가입한 비밀번호를 초기화 하는 경우')
    def post(self):
        """Reset User's Password"""
        data = request.json
        return search_password(data=data)

@api.route('/passwordchange')
@api.expect(parser)
class PasswordChange(Resource):
    @api.expect(changepwd, validate=True)
    @api.response(201, '새로운 비밀번호로 변경되었습니다.')
    @api.response(401, '이전 비밀번호가 일치하지 않습니다.')
    @api.doc('회원이 가입한 비밀번호를 바꾸려고 하는 경우')
    def post(self):
        """Change User's Password"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return change_password(res['email'],data = data)
        else:
            return res



@api.route('/dropout')
@api.expect(parser)
class UserDropOut(Resource):
    @api.expect(drop, validate=True)
    @api.response(201, '회원 탈퇴 되었습니다.')
    @api.response(402, '입력한 form에서 이름이 일치하지 않은 경우')
    @api.response(401, '비밀번호가 일치하지 않습니다.')
    @api.doc('회원이 서비스를 탈퇴하는 경우')
    def post(self):
        """Drop User's data"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return dropout(res['email'],data = data)
        else:
            return res
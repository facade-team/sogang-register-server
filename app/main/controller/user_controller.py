# user 모델과 관련된 모든 수신, HTTP요청을 처리.

from flask import request
from flask_restx import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, verify_a_user, can_use,gen_secret_code, get_user,allow_email,report

from app.main.service.auth_helper import Auth

# user dto
api = UserDto.api
_user = UserDto.user
verify_model = UserDto.user_verify
user_email = UserDto.user_email
major_email = UserDto.major_email
report_email = UserDto.report_email

parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('')
@api.expect(parser)
class Users(Resource):
    @api.doc('user 정보 조회')
    def get(self):
        '''user 정보 조회'''
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            return get_user(res['email'])
        else:
            return res

@api.route('/majoremail')
@api.expect(parser)
class Users(Resource):
    @api.expect(major_email, validate=True)
    @api.response(201, '회원정보 수정 완료되었습니다.')
    @api.doc('전공 변경 + email 수신 동의,비동의 전환 api')
    def post(self):
        '''해당 user의 전공 변경 + email 수신 동의/비동의 전환 api'''
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return allow_email(res['email'],data = data)
        else:
            return res

@api.route('/register')
class NewUser(Resource):
    @api.expect(_user, validate=True)
    @api.response(201, '회원가입 되었습니다.')
    @api.response(401, '이미 가입된 email 주소입니다.')
    @api.response(402, '입력한 email 주소는 맞는 형식이 아닙니다.')
    @api.doc('회원가입 form 작성 후 가입하기 누르는 경우')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

@api.route('/canuse')
class UserList(Resource):
    @api.expect(user_email, validate=True)
    @api.response(201, '사용 가능한 email 입니다.')
    @api.response(401, '중복된 email 입니다.')
    @api.response(402, '입력한 email 주소는 맞는 형식이 아닙니다.')
    @api.doc('가입할 수 있는 email인지 체크')
    def post(self):
        """중복된 email인지 / 올바른 email form 인지 체크."""
        data = request.json
        return can_use(email=data['email'])

@api.route('/gensecret')
class User(Resource):
    @api.doc('generate secret code and send to user email')
    @api.expect(user_email, validate=True)
    @api.response(201, '인증 코드 발송 성공')
    @api.response(401, '해당 email이 존재하지 않습니다.')
    @api.doc('해당 user의 email로 secret code 전송')
    def post(self):
        """email body에 넣어서 요청시 해당 email로 secret 코드 전송"""
        data = request.json
        return gen_secret_code(email=data['email'])

@api.route('/confirmsecret')
class UserVerify(Resource):
    @api.expect(verify_model, validate=True)
    @api.response(201, '해당 유저 이메일 인증 성공')
    @api.response(401, '잘못된 인증 코드를 입력했습니다.')
    @api.response(402, '해당하는 이메일이 존재하지 않습니다.')
    @api.doc('email로 발송된 인증코드 인증')
    def post(self):
        """Verify a new User """
        # request는 email이랑 code로 일단 해놓음
        data = request.json
        # 넘기는 건 타겟 유저의 email 주소임
        return verify_a_user(data)

@api.route('/reportemail')
@api.expect(parser)
class Report(Resource):
    @api.expect(report_email, validate=True)
    @api.response(201, '문의 내용 전송 완료')
    @api.doc('문의하기')
    def post(self):
        '''Send report to facade team'''
        data = request.json
        auth_header = request.headers.get('Authorization')
        if auth_header == 'None' or auth_header == None or auth_header == 'null':
            return report(data['email'],data,False)
        else:
            res = Auth.middleware(data=auth_header)
            if res['status'] == 'success':
                return report(res['email'],data,True)
            else:
                return res
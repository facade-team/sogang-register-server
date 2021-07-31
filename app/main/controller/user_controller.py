# user 모델과 관련된 모든 수신, HTTP요청을 처리.

from flask import request
from flask_restx import Resource

from ..util.dto import UserDto
from ..service.user_service import save_new_user, verify_a_user, can_use,gen_secret_code
from ..service.privacy_service import random_generator

# user dto
api = UserDto.api
_user = UserDto.user
verify_model = UserDto.user_verify
user_email = UserDto.user_email

@api.route('/register')
class NewUser(Resource):
    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('회원가입 form 작성 후 가입하기 누르는 경우')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

@api.route('/canuse')
class UserList(Resource):
    @api.expect(user_email, validate=True)
    @api.response(201, 'Email can be used.')
    @api.doc('가입할 수 있는 email인지 체크')
    def post(self):
        """Can I use this email? - body에 email만 담고 나머지 안 넣어도 돌아감 """
        data = request.json
        return can_use(email=data['email'])

@api.route('/gensecret')
class User(Resource):
    @api.doc('generate secret code and send to user email')
    @api.expect(user_email, validate=True)
    @api.response(201, 'Email send')
    @api.doc('해당 user의 email로 secret code 전송')
    def post(self):
        """email body에 넣어서 요청시 해당 email로 secret 코드 전송"""
        data = request.json
        return gen_secret_code(email=data['email'])

@api.route('/confirmsecret')
class UserVerify(Resource):
    @api.expect(verify_model, validate=True)
    @api.response(201, 'Verify email well done.')
    @api.doc('email로 발송된 인증코드 인증')
    def post(self):
        """Verify a new User """
        # request는 email이랑 code로 일단 해놓음
        data = request.json
        # 넘기는 건 타겟 유저의 email 주소임
        return verify_a_user(data)

# @api.route('/mailer')
# class UserList(Resource):
#     @api.doc('회원가입 후 email로 인증코드 전송')
#     @api.marshal_list_with(_user, envelope='data')
#     def get(self):
#         """List all registered users"""
#         return get_all_users()

# login, logout 가져와서 추가해야됨


# @api.route('/')
# class UserList(Resource):
#     @api.doc('list_of_registered_users')
#     @api.marshal_list_with(_user, envelope='data')
#     def get(self):
#         """List all registered users"""
#         return get_all_users()

#     @api.expect(_user, validate=True)
#     @api.response(201, 'User successfully created.')
#     @api.doc('create a new user')
#     def post(self):
#         """Creates a new User """
#         data = request.json
#         return save_new_user(data=data)


# @api.route('/<id>')
# @api.param('id', 'The User identifier')
# @api.response(404, 'User not found.')
# class User(Resource):
#     @api.doc('get a user')
#     @api.marshal_with(_user)
#     def get(self, id):
#         """get a user given its identifier"""
#         user = get_a_user(id)
#         if not user:
#             api.abort(404)
#         else:
#             return user

from flask import request
from flask_restx import Resource

from ..util.dto import JoinTable

# user dto
api = JoinTable.api
subject_id = JoinTable.subject

@api.route('/favorites')
class NewUser(Resource):
    @api.doc('list of user favorite subjects')
    @api.marshal_list_with(subject_id, envelope='data')
    def get(self): #get method
        """List all registered users"""
        return 'get_all_users'


@api.route('/favorites/add')
class NewUser(Resource):
    @api.expect(JoinTable, validate=True)
    @api.response(201, '회원가입 되었습니다.')
    @api.doc('회원가입 form 작성 후 가입하기 누르는 경우')
    def post(self):
        """Creates a new User """
        data = request.json
        return 'temp'

@api.route('/favorites/del')
class NewUser(Resource):
    @api.expect(JoinTable, validate=True)
    @api.response(201, '회원가입 되었습니다.')
    @api.doc('회원가입 form 작성 후 가입하기 누르는 경우')
    def post(self):
        """Creates a new User """
        data = request.json
        return 'temp'(data=data)

@api.route('/') # 실제로는 /user 이다. UserDto에서 정의한 내용.
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self): #get method
        """List all registered users"""
        return '() # service에서 정의한 함수 import해서 사용'


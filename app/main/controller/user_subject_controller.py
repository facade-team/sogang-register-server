from flask import request
from flask_restx import Resource

from ..util.dto import JoinTable
from ..service.user_subject_service import get_subjects, del_subjects, add_subjects
from app.main.service.auth_helper import Auth

# user dto
api = JoinTable.api
subject_id = JoinTable.subject

@api.route('/favorites')
class NewUser(Resource):
    @api.doc('list of user favorite subjects')
    @api.marshal_list_with(subject_id, envelope='data')
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            return get_subjects(res['email'])


@api.route('/favorites/add')
class NewUser(Resource):
    @api.expect(subject_id, validate=True)
    @api.response(201, '즐겨찾기에 해당 과목이 추가되었습니다.')
    @api.doc('토큰 인증 후 즐겨찾기 테이블에 해당 과목 추가')
    def post(self):
        """Add new favorite subject"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return add_subjects(res['email'],data)

@api.route('/favorites/del')
class NewUser(Resource):
    @api.expect(subject_id, validate=True)
    @api.response(201, '회원가입 되었습니다.')
    @api.doc('토큰 인증 후 즐겨찾기 테이블에 해당 과목 삭제')
    def post(self):
        """Delete favorite subject from table"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return del_subjects(res['email'],data)


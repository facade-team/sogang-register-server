from flask import request
from flask_restx import Resource

from ..util.dto import Complete
from ..service.user_subject_service import get_subjects, del_subjects, add_subjects
from app.main.service.auth_helper import Auth

# user dto
api = Complete.api
subject_id = Complete.subject

@api.route('/completed')
class NewUser(Resource):
    @api.doc('list of user completed subject codes')
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            return get_subjects(res['email'])


@api.route('/completed/update')
class NewUser(Resource):
    @api.expect(subject_id, validate=True)
    @api.response(201, '즐겨찾기에 추가, 혹은 업데이트 되었습니다.')
    @api.doc('토큰 인증 후 수강완료 테이블에 해당 과목 코드 추가')
    def post(self):
        """Add new favorite subject"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return add_subjects(res['email'],data)

@api.route('/completed/del')
class NewUser(Resource):
    @api.response(201, '수강완료에 등록된 과목 코드 중 특정 과목 코드를 삭제했습니다.')
    @api.doc('해당 유저의 특정 수강완료 과목 삭제')
    def get(self):
        """Delete completed subject from table"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            return del_subjects(res['email'])


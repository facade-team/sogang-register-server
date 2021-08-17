from flask import request
from flask_restx import Resource

from ..util.dto import Complete
from ..service.user_complete_service import get_subjects, del_subjects, add_subjects
from app.main.service.auth_helper import Auth

# user dto
api = Complete.api
subject_id = Complete.subject

parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/')
@api.expect(parser)
class NewUser(Resource):
    @api.doc('list of user completed subject codes')
    def get(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            return get_subjects(res['email'])
        else:
            return res


@api.route('/add')
@api.expect(parser)
class NewUser(Resource):
    @api.expect(subject_id, validate=True)
    @api.response(201, '수강완료 과목에 추가했습니다.')
    @api.doc('토큰 인증 후 수강완료 테이블에 해당 과목 코드 추가')
    def post(self):
        """Add new completed subject"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return add_subjects(res['email'],data)
        else:
            return res

@api.route('/del')
@api.expect(parser)
class NewUser(Resource):
    @api.expect(subject_id, validate=True)
    @api.response(201, '수강완료 과목에서 삭제되었습니다.')
    @api.doc('토큰 인증 후 수강완료 테이블에 해당 과목 코드 삭제')
    def post(self):
        """Delete new completed subject"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return del_subjects(res['email'],data)
        else:
            return res


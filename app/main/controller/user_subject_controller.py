from flask import request
from flask_restx import Resource

from ..util.dto import JoinTable
from ..service.user_subject_service import get_subjects, del_subjects, add_subjects,del_subject, add_subject
from app.main.service.auth_helper import Auth

# user dto
api = JoinTable.api
subject_id = JoinTable.subject
sub = JoinTable.sub

parser = api.parser()
parser.add_argument('Authorization', location='headers')

@api.route('/')
@api.expect(parser)
class NewUser(Resource):
    @api.doc('list of user favorite subjects')
    @api.response(201, '해당 유저의 즐겨찾기 목록 조회 완료.')
    @api.response(202, '즐겨찾기에 아직 아무것도 등록 안됨')
    def get(self):
        """Get favorite subjects from table"""
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            return get_subjects(res['email'])
        else:
            return res

# @api.route('/update')
# @api.expect(parser)
# class NewUser(Resource):
#     @api.expect(subject_id, validate=True)
#     @api.response(201, '즐겨찾기에 추가, 혹은 업데이트 되었습니다.')
#     @api.response(202, '사용자의 이메일 인증이 완료되지 않았습니다.')
#     @api.doc('토큰 인증 후 즐겨찾기 테이블에 해당 과목 추가')
#     def post(self):
#         """Add new favorite subject"""
#         # get auth token
#         auth_header = request.headers.get('Authorization')
#         res = Auth.middleware(data=auth_header)
#         if res['status'] == 'success':
#             data = request.json
#             return add_subjects(res['email'],data)
#         else:
#             return res

@api.route('/del')
@api.expect(parser)
class NewUser(Resource):
    @api.response(201, '즐겨찾기에 등록된 모든 과목을 삭제했습니다.')
    @api.doc('해당 유저의 모든 즐겨찾기 삭제')
    def get(self):
        """Delete all favorite subject from table"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            return del_subjects(res['email'])
        else:
            return res

@api.route('/update/add')
@api.expect(parser)
class NewUser(Resource):
    @api.expect(sub, validate=True)
    @api.response(201, '해당 과목을 즐겨찾기에 추가하였습니다.')
    @api.response(202, '사용자의 이메일 인증이 완료되지 않았습니다.')
    @api.response(401, '에러, res 확인')
    @api.response(402, '이미 즐겨찾기에 추가된 과목입니다.')
    @api.doc('토큰 인증 후 즐겨찾기 테이블에 해당 과목 추가')
    def post(self):
        """Add new favorite subject"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return add_subject(res['email'],data)
        else:
            return res

@api.route('/update/del')
@api.expect(parser)
class NewUser(Resource):
    @api.expect(sub, validate=True)
    @api.response(201, '즐겨찾기에 등록된 모든 과목을 삭제했습니다.')
    @api.response(201, '즐겨찾기에 등록된 해당 과목을 삭제했습니다.')
    @api.response(401, '즐겨찾기에 등록된 과목이 아닙니다.')
    @api.response(500, '에러, res 확인')
    @api.doc('토큰 인증 후 즐겨찾기 테이블에 해당 과목 삭제')
    def post(self):
        """Delete favorite subject from table"""
        # get auth token
        auth_header = request.headers.get('Authorization')
        res = Auth.middleware(data=auth_header)
        if res['status'] == 'success':
            data = request.json
            return del_subject(res['email'],data)
        else:
            return res
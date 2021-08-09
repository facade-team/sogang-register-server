from flask import request
from flask_restx import Resource

from ..util.dto import SubjectDto
from ..service.subject_service import get_all_data, get_data_by_option, get_departments

api = SubjectDto.api
_subject = SubjectDto.subject
_option = SubjectDto.option

@api.route('')
class SearchTable(Resource):
  @api.doc('현재 학기 개설교과목 정보를 전부 조회')
  def get(self):
    """현재 학기 학부 개설교과목 정보를 전부 조회"""
    return get_all_data()

@api.route('/department')
@api.param('semester', 'The semester identifier')
@api.param('year', 'The year identifier')
@api.response(403, 'Table not found.')
class Department(Resource):
  @api.response(201, 'Success')
  @api.doc('개설교과목 학부 정보 조회')
  def get(self):
    """개설교과목 학부 정보 조회"""
    year = request.args.get('year', '21')
    semester = request.args.get('semester', '2')
    return get_departments(year, semester)

@api.route('/option')
class Option(Resource):
  @api.doc('검색 옵션을 포함하여 개설교과먹 정보 조회')
  @api.expect(_option, validate=True)
  def post(self):
    """검색 옵션을 포함하여 개설교과먹 정보 조회"""
    data = request.json
    return get_data_by_option(data)
from flask import request
from flask_restx import Resource

from ..util.dto import SubjectDto
from ..service.subject_service import get_all_data, get_professors_list, get_data_by_department, get_data_by_grade, get_data_by_credit, get_data_by_keyword

api = SubjectDto.api
_subject = SubjectDto.subject
_grade = SubjectDto.grade
_credit = SubjectDto.credit
_keyword = SubjectDto.keyword

@api.route('/')
class SearchTable(Resource):
  @api.doc('2021학년도 2학기 학부 개설교과목 정보를 전부 조회')
  @api.marshal_list_with(_subject, envelope='data')
  def get(self):
    """2021학년도 2학기 학부 개설교과목 정보를 전부 조회"""
    return get_all_data()

@api.route('/department/<string:department>')
@api.param('department', 'The Subject identifier')
@api.response(404, 'Subject not found.')
class Department(Resource):
  @api.response(201, 'Success')
  @api.doc('전공 옵션으로 개설교과목 정보 조회')
  def get(self, department):
    """전공 옵션으로 개설교과목 정보 조회"""
    return get_data_by_department(department)

@api.route('/grade')
class Grade(Resource):
  @api.doc('학년 옵션으로 개설교과목 정보 조회')
  @api.expect(_grade, validate=True)
  def post(self):
    """학년 옵션으로 개설교과목 정보 조회"""
    data = request.json
    return get_data_by_grade(data)

@api.route('/credit')
class Credit(Resource):
  @api.doc('학점 옵션으로 개설교과목 정보 조회')
  @api.expect(_credit, validate=True)
  def post(self):
    """학점 옵션으로 개설교과목 정보 조회"""
    data = request.json
    return get_data_by_credit(data)
  
@api.route('/keyword')
class Keyword(Resource):
  @api.doc('검색어 옵션으로 개설교과목 정보 조회')
  @api.expect(_keyword, validate=True)
  def post(self):
    """검색어 옵션으로 개설교과목 정보 조회"""
    data = request.json
    return get_data_by_keyword(data)

@api.route('/professor')
class Professor(Resource):
  @api.doc('교수진 목록을 전부 조회')
  def get(self):
    """교수진 목록을 전부 조회"""
    return get_professors_list()

'''
@api.route('/test')
class Professor(Resource):
  @api.doc('test1')
  def get(self):
    """test1"""
    test1 = request.args.get('test1', None)
    test2 = request.args.get('test2', None)
    return 'test1 : ' + test1 + ', test2 : ' + test2

@api.route('/test/<test2>')
class Professor(Resource):
  @api.doc('test2')
  def get(self, test2):
    """test2"""
    return 'test2 : ' + test2
'''
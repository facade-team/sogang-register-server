from flask import request
from flask_restx import Resource

from ..util.dto import SearchDto
from ..service.search_service import get_all_data

api = SearchDto.api
_subject = SearchDto.subject

@api.route('/')
class SearchTable(Resource):
  @api.doc('개설교과목 정보를 전부 조회')
  #@api.marshal_list_with(_subject, envelope='data')
  def get(self):
    """개설교과목 정보를 전부 조회"""
    return get_all_data()
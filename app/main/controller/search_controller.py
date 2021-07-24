from flask import request
from flask_restx import Resource

from ..util.dto import SearchDto
from ..service.search_service import get_all_data

api = SearchDto.api

@api.route('/')
class SearchTable(Resource):
  @api.doc('개설교과목 정보를 전부 조회')
  def get(self):
    """개설교과목 정보를 전부 조회"""
    return get_all_data()
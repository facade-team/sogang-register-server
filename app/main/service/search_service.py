def get_all_data():
  # 여기에 조회 관련된 비즈니스 로직 작성
  
  if True:
    response_object = {
              'status': 'success',
              'message': '조회 성공입니다',
          }
    return response_object, 201
  else :
    response_object = {
              'status': 'fail',
              'message': '조회 실패입니다.',
          }#
  return response_object, 401
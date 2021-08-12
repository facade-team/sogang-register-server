from main import db
import pandas as pd
from sqlalchemy.sql import text
zip_cols = (
  'subject_id',
  '과목명',
  '학과',
  '강의계획서',
  '학점',
  '강의실',
  '교수진',
  '수강대상',
  '과목설명',
  '비고',
  '대면여부',
  '강의언어',
  '수업시간_강의실'
)
zip_res = (
  '요일1',
  '요일2',
  '시간1',
  '시간2',
)

query_cols = 'subject_id, 과목명, 학과, 강의계획서, 학점, 강의실, 교수진, 수강대상, 과목_설명, 비고, 대면여부, 강의언어, 수업시간_강의실'


def get_all_data():
    #cur.execute("SELECT {} FROM s21_2".format(query_cols))
    cur = db.session.execute(text("SELECT {} FROM s21_2;".format(query_cols)))
    res = []
    temp = {}
    test = {}
    for elem in cur:
      temp = dict(zip(zip_res,parsing(elem[-1])))
      test = dict(zip(zip_cols, elem))
      test.update(temp)

      res.append(test)
      #res.append(dict(zip(zip_cols, elem)))
    db.session.close()
    response_object = {
        'status': 'success',
        'message': '학부 목록 조회에 성공하였습니다.',
        'data': res
    }
    return response_object

def get_professors_list():
    #cur.execute("""SELECT 교수진 FROM s21_2""")
    cur = db.session.execute(text("SELECT 교수진 FROM s21_2"))
    res = []
    total_professor_list = []
    for elem in cur:
      total_professor_list.append(elem[0])
    unique_professor_list = list(pd.Series(total_professor_list).unique())
    
    for professor in unique_professor_list:
      if professor != "\xa0":
        res.append(dict(zip(['교수진'], [professor])))
    #print(len(res))
    db.session.close()
    return res

def set_department_query_string(department):
  return "department LIKE '%{}%'".format(department)

def set_credit_query_string(credits):
  if len(credits) == 1:
    credit = '학점 = '+str(credits[0])
  elif len(credits) == 2:
    credit = '학점 = '+str(credits[0])+' OR 학점 = '+str(credits[1])
  else:
    credit = '학점 = '+str(credits[0])+' OR 학점 = '+str(credits[1])+' OR 학점 = '+str(credits[2])
  return credit

def set_grade_query_string(grades):
  '''
  # 한 개 학년일 경우
  if len(grades) == 1:
      grade = '수강대상 = "'+str(grades[0])+'학년"'
  # 전학년일 경우    
  elif len(grades) == 4:
      grade = '수강대상 = "전학년"'
  # 2개 ~ 3개 학년일 경우
  else:
      grade = '수강대상 = "'
      for i in range(len(grades) - 1):
        grade += str(grades[i])+','
      grade += str(grades[len(grades) - 1])+'학년"'
  '''
  grade = '수강대상 LIKE "%전%"'
  
  for i in range(len(grades)):
    grade += ' or 수강대상 LIKE "%{}%"'.format(str(grades[i]))
  return grade

def set_keyword_query_string(searchby, keyword):
  return "{} LIKE '%{}%'".format(searchby, keyword)

'''
def check_department_form(department):
  if not department in departments_text_list:
    return False
  return True
'''

def check_credit_form(credits):
  if len(credits) == 0 or len(credits) > 3:
    return False
  return True

def check_grade_form(grade):
  if len(grade) == 0 or len(grade) > 4:
    return False
  return True

def check_keyword_form(searchby, keyword):
  if not searchby in ['과목명', '과목번호', '교수진', '강의실']:
    return False
  if searchby == None or keyword == None:
    return False
  return True

def get_data_by_option(data):
  year = data['year']
  semester = data['semester']
  department = None
  credit = None
  grade = None
  searchby = None
  keyword = None
  
  error_response_object = {
      'status': 'fail',
      'message': 'payload 형식이 잘못되었습니다.'
  }
  
  if year not in ['18', '19', '20', '21'] or semester not in ['1','2','s','w'] or (year == '21' and semester == 'w'):
    response_object = {
        'status': 'fail',
        'message': '잘못된 학년도와 학기 입니다.'
    }
    return response_object, 402
  
  if 'department' in data:
    department = data['department']
    department = set_department_query_string(department)
  if 'credit' in data:
    credit = data['credit']
    if not check_credit_form(credit):
      credit = None
      return error_response_object, 402
    else:
      credit = set_credit_query_string(credit)
  if 'grade' in data:
    grade = data['grade']
    #print(grade)
    if not check_grade_form(grade):
      grade = None
      return error_response_object, 402
    else:
      grade = set_grade_query_string(grade)
  if 'searchby' in data and 'keyword' in data:
    searchby = data['searchby']
    keyword = data['keyword']
    if not check_keyword_form(searchby, keyword):
      searchby = None
      keyword = None
      return error_response_object, 402
    else:
      searchby = set_keyword_query_string(searchby, keyword)
  
  payloads = [department, credit, grade, searchby]
  tabale_name = 's{}_{}'.format(year, semester)
  
  # 옵션이 몇 개 인지 확인하여 query String 완성
  optionNumber = 0
  query = ' WHERE '
  for option in payloads:
    if option != None:
        if optionNumber > 0:
          optionNumber += 1
          query += ' AND ({})'.format(option)
        else:
          optionNumber += 1
          query += '({})'.format(option)
  
  if optionNumber == 0:
    query = ''
    
  #cur.execute("SELECT {} FROM {}{}".format(query_cols, tabale_name, query))
  cur = db.session.execute(text("SELECT {} FROM {}{}".format(query_cols, tabale_name, query)))
  res = []
  temp = {}
  test = {}
  for elem in cur:
    temp = dict(zip(zip_res,parsing(elem[-1])))
    test = dict(zip(zip_cols, elem))
    test.update(temp)

    #res.append(dict(zip(zip_cols, elem)))
    res.append(test)
  db.session.close()
  response_object = {
      'status': 'success',
      'message': '개설교과목 조회에 성공하였습니다.',
      'data': res
  }
  return response_object

def parsing(time_place):
  # 강의실 뽑기
  # / 있는지 확인
  # 있을 경우 왼쪽 오른쪽 따로 저장
  # 없을 경우 , 기준으로 요일 저장 후 시간 저장
  time = time_place
  day1 = ''
  day2 = ''
  time1 = ''
  time2 = ''

  if time == '\xa0':
    return (day1,day2,time1,time2)

  if '[' in time_place:
    # 강의실 정보 있음
    i = time_place.rfind('[')
    time = time_place[:i]

  if '/' in time:
    left = time.split('/')[0]
    right = time.split('/')[1]

    day1 = left.split(' ')[0]
    time1 = left.split(' ')[1]
    day2 = right.split(' ')[1]
    time2 = right.split(' ')[2]
    result = (day1,day2,time1,time2)
  else:
    if ',' in time:
      i = time.find(',')
      day1 = time[0]
      day2 = time[2]
      time1 = time.split(' ')[1]
      result = (day1,day2,time1,time1)
    else:
      print(time.split(' '))
      day1 = time.split(' ')[0]
      time1 = time.split(' ')[1]
      result = (day1,day1,time1,time1)

  return result

def get_departments(year, semester):
  if year not in ['18', '19', '20', '21'] or semester not in ['1','2','s','w'] or (year == '21' and semester == 'w'):
    response_object = {
        'status': 'fail',
        'message': '잘못된 학년도와 학기 입니다.'
    }
    return response_object, 403
  text_col = 's{}_{}_text'.format(year, semester)
  id_col = 's{}_{}_id'.format(year, semester)
  cur = db.session.execute(text("SELECT {}, {} FROM departments".format(text_col, id_col)))
  res = []
  for elem in cur:
      if elem[0] != None:
        res.append({
          'text': elem[0],
          'id': elem[1]
        })
  db.session.close()
  response_object = {
      'status': 'success',
      'message': '학부 목록 조회에 성공하였습니다.',
      'data': res
  }
  return response_object
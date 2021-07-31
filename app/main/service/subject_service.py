from main import db
from main.model.subject import Subject
from main import cur, con
import pandas as pd
columns = (
    'id',
    '학년도',
    '학기',
    '소속',
    '학과',
    '과목번호',
    '분반',
    '과목명',
    '강의계획서',
    '학점',
    '수업시간_강의실',
    '시간',
    '교수진',
    '수강생수',
    '영어강의',
    '중국어강의',
    '공학인증',
    '국제학생',
    'Honors과목',
    '홀짝구분',
    '승인과목',
    '시험일자',
    '수강대상',
    '권장학년',
    '수강신청_참조사항',
    '과목_설명',
    '비고',
    'subject_id',
    '전인교육원'
)

zip_cols = (
  'subject_id',
  '과목명',
  '학과',
  '강의계획서',
  '학점',
  '요일',
  '시작시간',
  '종료시간',
  '강의실',
  '교수진',
  '수강대상',
  '과목설명',
  '비고',
  '대면여부',
  '강의언어'
)

query_cols = 'subject_id, 과목명, 학과, 강의계획서, 학점, 요일, 시작시간, 종료시간, 강의실, 교수진, 수강대상, 과목_설명, 비고, 대면여부, 강의언어'


def get_all_data():
    if True:
      response_object = {
                'status': 'success',
                'message': '조회 성공입니다',
              }
      cur.execute("SELECT {} FROM s21_2".format(query_cols))
      res = []
      for elem in cur:
          res.append(dict(zip(zip_cols, elem)))
      return res
    else :
      response_object = {
                'status': 'fail',
                'message': '조회 실패입니다.',
            }
    return response_object, 401

def get_professors_list():
    cur.execute("""SELECT 교수진 FROM s21_2""")
    res = []
    total_professor_list = []
    for elem in cur:
      total_professor_list.append(elem[0])
    unique_professor_list = list(pd.Series(total_professor_list).unique())
    
    for professor in unique_professor_list:
      if professor != "\xa0":
        res.append(dict(zip(['교수진'], [professor])))
    print(len(res))
    return res
  
def get_data_by_department(department):
  cur.execute("SELECT {} FROM s21_2 WHERE 학과 = '{}'".format(query_cols, department))
  res = []
  for elem in cur:
      res.append(dict(zip(zip_cols, elem)))
  return res

def get_data_by_grade(data):
  grades = data['grade']
  # payload에 학년이 안담겼을 경우
  if len(grades) == 0:
      return 'error!'
  # 한 개 학년일 경우
  elif len(grades) == 1:
      grade = str(grades[0])+'학년'
  # 전학년일 경우    
  elif len(grades) == 4:
      grade = '전학년'
  # 2개 ~ 3개 학년일 경우
  else:
      grade = ''
      for i in range(len(grades) - 1):
        grade += str(grades[i])+','
      grade += str(grades[len(grades) - 1])+'학년'
  cur.execute("SELECT {} FROM s21_2 WHERE 수강대상 = '{}'".format(query_cols, grade))
  res = []
  for elem in cur:
      res.append(dict(zip(zip_cols, elem)))
  return res

def get_data_by_credit(data):
  credits = data['credit']
  # payload에 학점이 안담겼을 경우
  if len(credits) == 0:
    return 'error!'
  elif len(credits) == 1:
    credit = '학점 = '+str(credits[0])
  elif len(credits) == 2:
    credit = '학점 = '+str(credits[0])+' OR 학점 = '+str(credits[1])
  else:
    credit = '학점 = '+str(credits[0])+' OR 학점 = '+str(credits[1])+' OR 학점 = '+str(credits[2])
  cur.execute("SELECT {} FROM s21_2 WHERE {}".format(query_cols, credit))
  res = []
  for elem in cur:
      res.append(dict(zip(zip_cols, elem)))
  return res

def get_data_by_keyword(data):
  option = data['option']
  keyword = data['keyword']
  if not option in ['과목명', '과목번호', '교수진', '강의실']:
    return "error! option must be one of '과목명', '과목번호', '과목코드', '강의실'"
  cur.execute("SELECT {} FROM s21_2 WHERE {} LIKE '%{}%'".format(query_cols, option, keyword))
  res = []
  for elem in cur:
      res.append(dict(zip(zip_cols, elem)))
  return res

def set_credit_query_string(credits):
  if len(credits) == 1:
    credit = '학점 = '+str(credits[0])
  elif len(credits) == 2:
    credit = '학점 = '+str(credits[0])+' OR 학점 = '+str(credits[1])
  else:
    credit = '학점 = '+str(credits[0])+' OR 학점 = '+str(credits[1])+' OR 학점 = '+str(credits[2])
  return credit

def set_grade_query_string(grades):
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
  return grade

def set_keyword_query_string(searchby, keyword):
  return "{} LIKE '%{}%'".format(searchby, keyword)

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
  
  if 'department' in data:
    department = data['department']
  if 'credit' in data:
    credit = data['credit']
    if not check_credit_form(credit):
      credit = None
      return 'Wrong format!'
    else:
      credit = set_credit_query_string(credit)
  if 'grade' in data:
    grade = data['grade']
    print(grade)
    if not check_grade_form(grade):
      grade = None
      return 'Wrong format!'
    else:
      grade = set_grade_query_string(grade)
  if 'searchby' in data and 'keyword' in data:
    searchby = data['searchby']
    keyword = data['keyword']
    if not check_keyword_form(searchby, keyword):
      searchby = None
      keyword = None
      return 'Wrong format!'
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
  
  print(query)
  
  cur.execute("SELECT {} FROM {}{}".format(query_cols, tabale_name, query))
  res = []
  for elem in cur:
      res.append(dict(zip(zip_cols, elem)))
  return res
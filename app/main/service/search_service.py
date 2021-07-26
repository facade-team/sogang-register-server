from main import db
from main.model.subject import Subject
from main import cur, con
import datetime
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

test_columns = (
  'subject_id',
  '과목명',
  '강의계획서',
  '학점',
  '수업시간_강의실',
  '교수진',
  '권장학년',
  '비고',
  '전인교육원'
)

def get_all_data():
  # 여기에 조회 관련된 비즈니스 로직 작성
  
  if True:
    response_object = {
              'status': 'success',
              'message': '조회 성공입니다',
            }
    #subject = Subject.query.filter_by(subject_id='21-2-ENG2001-01').first()
    #print(subject)
    # return Subject.query.filter_by(subject_id='21-2-ENG2001-01').first()
    #return Subject.query.all()
    
    start = datetime.datetime.now()
    # cur.execute("""SELECT subject_id, 과목명, 강의계획서, 학점, 수업시간_강의실, 교수진, 권장학년, 비고, 전인교육원 FROM total_data""")
    cur.execute("""SELECT * FROM total_data LIMIT 40, 40""")
    print("query execution time: ", datetime.datetime.now()-start)

    start_ = datetime.datetime.now()
    res = []
    for elem in cur:
        res.append(dict(zip(columns, elem)))
    print("Jsonify execution time: ", datetime.datetime.now()-start_)
    # con.close()
    print("total time: ",  datetime.datetime.now()-start)
    return res
  else :
    response_object = {
              'status': 'fail',
              'message': '조회 실패입니다.',
          }
  return response_object, 401
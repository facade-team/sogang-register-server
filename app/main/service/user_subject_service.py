from main import db
from main.model.user_subject import UserSubject
from main.model.user import User
from sqlalchemy.sql import text
#('21-2-ENG2001-01', '영문학개론', '영미어문전공', '조회', 3, '', '김희진', '전학년', '\xa0', '2021-2학기 신규강사 채용 예정', '비대면', '영어', '월,수 16:30~17:45')
query_cols = 'subject_id, 과목명, 학과, 강의계획서, 학점, 강의실, 교수진, 수강대상, 과목_설명, 비고, 대면여부, 강의언어, 수업시간_강의실, 요일1, 요일2, 시간1, 시간2'
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
  '수업시간_강의실',
  '요일1',
  '요일2',
  '시간1',
  '시간2'
)

zip_res = (
  '요일1',
  '요일2',
  '시간1',
  '시간2',
)
def get_subjects(user_email):
    try:
        # Join table에서 해당 유저의 모든 즐겨찾기 과목 검색
        user = UserSubject.query.filter_by(email=user_email).all()
        #user = db.session.query(UserSubject.subject_id).filter(UserSubject.email == user_email).all()
        if user:
            # 배열로 먼저 가져온 다음 순차적으로 하나씩 뽑아서 response 완성하자
            res = []
            for i in user:
                # 어떤 table 결정
                splitdata = i.subject_id.split('-')
                #target_table = 's' + splitdata[0] + '_' + splitdata[1]
                target_table = ('s%s_%s' % (splitdata[0], splitdata[1]))

                # 테이블에서 해당 id 조회
                cur = db.session.execute(text("SELECT {} FROM {} WHERE subject_id='{}'".format(query_cols, target_table, i.subject_id)))
                # 리턴 오브젝트에 추가 후 한번에 리턴
                for elem in cur:
                    if elem != None:
                        res.append(dict(zip(zip_cols, elem)))
                db.session.close()  # session close add
            db.session.close()
            response_object = {
                'status': 'success',
                'message': '해당 유저의 즐겨찾기 목록 조회 완료',
                'data':res
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'success',
                'message': '즐겨찾기에 아직 아무것도 등록 안됨',
                'data': None
            }
            return response_object, 202
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def add_subjects(user_email, data):
    # Join table에 해당 유저의 id + subject_id로 추가
    # 존재하는 유저인지 검증
    try:
        user = User.query.filter_by(email=user_email).first()
        if user.verify_on == True:
            subjectlist = data['sub_id']
            del_subjects(user_email)
            for i in subjectlist:
                new_favorite = UserSubject(
                    email = user_email,
                    subject_id = i
                )
                save_changes(new_favorite)
            db.session.close()
            response_object = {
                'status': 'success',
                'message': '즐겨찾기에 추가, 혹은 업데이트 되었습니다.'
            }
            return response_object, 201
        else:
            db.session.close()
            response_object = {
                'status': 'fail',
                'message': '사용자의 이메일 인증이 완료되지 않았습니다.'
            }
            return response_object, 202
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def del_subjects(user_email):
    try:
        # Join table에서 해당 유저의 해당 즐겨찾기 과목 전체 삭제
        user = UserSubject.query.filter_by(email=user_email).all()
        if user:
            # 몇 번 찾아서 지울건지 체크
            for i in user:
                db.session.delete(i)
                db.session.commit()
                db.session.close()
            response_object = {
                'status': 'success',
                'message': '즐겨찾기에 등록된 모든 과목을 삭제했습니다.'
            }
            db.session.close()
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': '즐겨찾기에 등록된 과목이 없습니다.'
            }
            db.session.close()
            return response_object
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def save_changes(data):
    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def del_subject(user_email,data):
    try:
        # Join table에서 해당 유저의 해당 즐겨찾기 과목 전체 삭제
        user = UserSubject.query.filter_by(email=user_email , subject_id=data['sub_id']).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            response_object = {
                'status': 'success',
                'message': '즐겨찾기에 등록된 해당 과목을 삭제했습니다.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': '즐겨찾기에 등록된 과목이 아닙니다.'
            }
            return response_object, 401
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()

def add_subject(user_email, data):
    # Join table에 해당 유저의 id + subject_id로 추가
    # 존재하는 유저인지 검증
    try:
        user = User.query.filter_by(email=user_email).first()
        if user.verify_on == True:
            # 이미 같은 sub_id가 있다면 그냥 아무것도 안함
            try:
                if not UserSubject.query.filter_by(subject_id = data['sub_id'],email=user_email).first():
                    new_favorite = UserSubject(
                        email = user_email,
                        subject_id = data['sub_id']
                    )
                    save_changes(new_favorite)
                    response_object = {
                        'status': 'success',
                        'message': '해당 과목을 즐겨찾기에 추가하였습니다.'
                    }
                    return response_object, 201
                else:
                    response_object = {
                        'status': 'fail',
                        'message': '이미 즐겨찾기에 추가된 과목입니다.'
                    }
                    return response_object, 402
            except Exception as e:
                response_object = {
                        'status': 'fail',
                        'message': str(e)
                    }
                return response_object, 401
            finally:
                db.session.close()
        else:
            db.session.close()
            response_object = {
                'status': 'fail',
                'message': '사용자의 이메일 인증이 완료되지 않았습니다.'
            }
            return response_object, 202
    except Exception as e:
        response_object = {
            'status': 'error',
            'message': str(e)
        }
        return response_object, 500
    finally:
        db.session.close()
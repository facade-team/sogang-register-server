
from main import db
from main.model.user_subject import UserSubject
from main.model.user import User

def get_subjects(user_email):
    # Join table에서 해당 유저의 모든 즐겨찾기 과목 검색
    user = UserSubject.query.filter_by(email=user_email).first()
    if user:
        # 배열로 먼저 가져온 다음 순차적으로 하나씩 뽑아서 response 완성하자
        fb_list = user.subject_id.split(' ')
        print(fb_list)
        
        response_object = {
            'status': 'success',
            'message': '해당 유저의 즐겨찾기 목록 조회 완료'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'success',
            'message': '즐겨찾기에 아직 아무것도 등록 안됨'
        }
        return response_object, 201

def add_subjects(user_email, data):
    # Join table에 해당 유저의 id + subject_id로 추가
    # 존재하는 유저인지 검증
    user = User.query.filter_by(email=user_email).first()
    notfirst = UserSubject.query.filter_by(email=user_email).first()
    # db에 추가 - 처음 등록하는경우 or update하는 경우로 분기
    # 두 테이블에 모두 email이 존재한다 - update
    # user 테이블에만 email이 존재한다 - add
    # 둘 다 없다 - error
    if user:
        subjectlist = ' '.join(data['sub_id'])
        if notfirst:
            # update
            #count_favorites(notfirst.subject_id)
            notfirst.subject_id = subjectlist
            db.session.commit()
            db.session.close()
        else:
            #add
            new_favorite = UserSubject(
                email = user_email,
                subject_id = subjectlist
            )
            save_changes(new_favorite)
        response_object = {
            'status': 'success',
            'message': '즐겨찾기에 추가, 혹은 업데이트 되었습니다.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': '등록된 사용자가 아닙니다.'
        }
        return response_object, 201

def del_subjects(user_email):
    # Join table에서 해당 유저의 해당 즐겨찾기 과목 전체 삭제
    user = UserSubject.query.filter_by(email=user_email).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        db.session.close()
        response_object = {
            'status': 'success',
            'message': '즐겨찾기에 등록된 모든 과목을 삭제했습니다.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': '즐겨찾기에 등록된 과목이 없습니다.'
        }
        return response_object

def save_changes(data):
    db.session.add(data)
    db.session.commit()
    db.session.close()

def count_favorites(favorites):
    fb_list = favorites.split(' ')
    c =len(fb_list) 
    if c < 11 :
        return c
    else :
        return 11

# def get_a_user(public_id):
#     return User.query.filter_by(public_id=public_id).first()

from sqlalchemy.sql.elements import Null
from main import db
from main.model.user_subject import UserSubject
from main.model.user import User

def get_subjects(user_email):
    # Join table에서 해당 유저의 모든 즐겨찾기 과목 검색
    user = UserSubject.query.filter_by(email=user_email)
    if user:
        print(user)
    return 'hello'

def add_subjects(user_email, data):
    # Join table에 해당 유저의 id + subject_id로 추가
    # 존재하는 유저인지 검증
    user = User.query.filter_by(email=user_email).first()
    if user:
        print(user)
    return 'hello'

def del_subjects(user_email, data):
    # Join table에서 해당 유저의 해당 즐겨찾기 과목 삭제
    user = UserSubject.query.filter_by(email=user_email)
    if user:
        print(user)
    return 'hello'

def save_changes(data):
    db.session.add(data)
    db.session.commit()

# def get_a_user(public_id):
#     return User.query.filter_by(public_id=public_id).first()
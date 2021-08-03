
from sqlalchemy.sql.elements import Null
from main import db
from main.model.user import User

import re

# 회원가입한 회원 정보를 user모델(즉, user테이블에 넣기)
def save_new_user(data):
    # 맞는 email 형식인지 먼저 체크
    return 'hello'

def save_changes(data):
    db.session.add(data)
    db.session.commit()

# def get_a_user(public_id):
#     return User.query.filter_by(public_id=public_id).first()
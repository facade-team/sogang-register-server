from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='sogang-register related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'major':  fields.List(fields.String(description='user major'),required=True),
        'allow_email': fields.Boolean(required=True, description='allow email alert or not')
    })
    # 새로운 user의 email 인증과 관련해서 request를 email, access code 두 개로 하려고 하는데 괜찮겠지?
    user_verify = api.model('user_verify', {
        'email': fields.String(required=True, description='user email address'),
        'script': fields.String(required=True, description='access code sent to user email'),
    })
    user_email = api.model('user_email', {
        'email': fields.String(required=True, description='user email address'),
    })
    major_email = api.model('major_alert', {
        'major':  fields.List(fields.String(description='user major'),required=True),
        'allow_email': fields.Boolean(required=True, description='allow email alert or not')
    })
    report_email = api.model('report_email', {
        'email': fields.String(required=True, description='user email address'),
        'title': fields.String(required=True, description='title'),
        'script': fields.String(required=True, description='body'),
    })
    
class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })

class PrivacyDto:
    api = Namespace('privacy', description='find email, find password')
    privacy = api.model('privacy', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
    })
    changepwd = api.model('changepwd', {
        'old_password': fields.String(required=True, description='old password'),
        'new_password': fields.String(required=True, description='new password'),
    })
    drop = api.model('dropout', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='password'),
    })

class JoinTable:
    api = Namespace('favorites', description='Favorite subjects in here')
    subject = api.model('sub_id', {
        'sub_id': fields.List(fields.String(description='add and delete subject id in join table'), required=True),
    })
    subject = api.model('sub_id', {
        'sub_id': fields.List(fields.String(description='add and delete subject id in join table'), required=True),
    })
    sub = api.model('sub', {
        'sub_id': fields.String(required=True,description='add and delete subject id in join table'),
    })

class Complete:
    api = Namespace('complete', description='Attended subjects in here')
    subject = api.model('sub_code', {
        'sub_id': fields.String(required=True, description='subject code'),
    })

class SubjectDto:
    api = Namespace('subject', description='db search related operations')
    subject = api.model('subject', {
        'subject_id': fields.String(required=True, description='test'),
        '과목명': fields.String(required=True, description='test'),
        '학과': fields.String(required=True, description='test'),
        '강의계획서': fields.String(required=True, description='test'),
        '학점': fields.Integer(required=True, description='test'),
        '요일': fields.String(required=True, description='test'),
        '시작시간': fields.String(required=True, description='test'),
        '종료시간': fields.String(required=True, description='test'),
        '강의실': fields.String(required=True, description='test'),
        '교수진': fields.String(required=True, description='test'),
        '수강대상': fields.String(required=True, description='test'),
        '과목설명': fields.String(required=True, description='test'),
        '비고': fields.String(required=True, description='test'),
        '대면여부': fields.String(required=True, description='test'),
        '강의언어': fields.String(required=True, description='test'),
    })
    option = api.model('option', {
      'year': fields.String(required=True, description='학년도 (ex. 21, 20, 19, ...)'), # '21' 
      'semester': fields.String(required=True, description='학기 (ex. 1, s, 2, w)'), #'2'
      'department': fields.String(required=False, description='소분류 ID(학과 ID) (ex. "WD0132")'), # '컴퓨터공학전공'
      'credit': fields.List(fields.Integer(required=False, description='학점 (ex. [1], [1,2,3], [2,3], ...)')), # [0,1,2,3] # 0은 기타
      'grade': fields.List(fields.Integer(required=False, description='학년(수강대상) (ex. [1], [1,2], [1,2,3,4], ...)')), # [0,1,2,3,4] # 0은 기타
      'searchby': fields.String(required=False, description='검색옵션 (ex. "과목명", "과목번호", "교수진", "강의실" 중 하나!)'), # '과목명' # ['과목명', '과목번호', '교수진', '강의실'] 중 하나
      'keyword': fields.String(required=False, description='검색어 (notice. searchby와 같이 넘겨줘야한다.)'), #'장형수'
      'day': fields.List(fields.String(required=False, description='요일 (ex. ["월"], ["월","화"], ["화","수"], ...)')), # 해당 요일에 수업이 해당되기만 하면 무조건 출력. ex)수업이 월,수인 경우 "월" 만 넘겨줘도 출력.
      'time': fields.List(fields.String(required=False, description='시간 (ex. ["09:00","11:45"], ["12:00","13:15"],...)')), # 해당 시간대에 수업이 포함되어 있으면 출력. 배열의 첫 번째 인자는 탐색할 조건의 시작시간, 두 번째 인자는 종료시간이다.
    })
# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



t_departments = db.Table(
    'departments',
    db.Column('id', db.BigInteger, index=True),
    db.Column('s20_1_text', db.Text),
    db.Column('s20_1_id', db.Text),
    db.Column('s20_s_text', db.Text),
    db.Column('s20_s_id', db.Text),
    db.Column('s20_2_text', db.Text),
    db.Column('s20_2_id', db.Text),
    db.Column('s20_w_text', db.Text),
    db.Column('s20_w_id', db.Text),
    db.Column('s21_1_text', db.Text),
    db.Column('s21_1_id', db.Text),
    db.Column('s21_s_text', db.Text),
    db.Column('s21_s_id', db.Text),
    db.Column('s21_2_text', db.Text),
    db.Column('s21_2_id', db.Text)
)



t_s20_1 = db.Table(
    's20_1',
    db.Column('id', db.BigInteger, index=True),
    db.Column('학년도', db.Text),
    db.Column('학기', db.Text),
    db.Column('소속', db.Text),
    db.Column('학과', db.Text),
    db.Column('과목번호', db.Text),
    db.Column('분반', db.Text),
    db.Column('과목명', db.Text),
    db.Column('강의계획서', db.Text),
    db.Column('학점', db.BigInteger),
    db.Column('수업시간_강의실', db.Text),
    db.Column('시간', db.Text),
    db.Column('교수진', db.Text),
    db.Column('수강생수', db.Text),
    db.Column('영어강의', db.Text),
    db.Column('중국어강의', db.Text),
    db.Column('공학인증', db.Text),
    db.Column('국제학생', db.Text),
    db.Column('Honors과목', db.Text),
    db.Column('홀짝구분', db.Text),
    db.Column('승인과목', db.Text),
    db.Column('시험일자', db.Text),
    db.Column('수강대상', db.Text),
    db.Column('권장학년', db.Text),
    db.Column('수강신청_참조사항', db.Text),
    db.Column('과목_설명', db.Text),
    db.Column('비고', db.Text),
    db.Column('subject_id', db.Text),
    db.Column('department', db.Text),
    db.Column('요일', db.Text),
    db.Column('시작시간', db.Text),
    db.Column('종료시간', db.Text),
    db.Column('강의실', db.Text),
    db.Column('대면여부', db.Text),
    db.Column('강의언어', db.Text)
)



t_s20_2 = db.Table(
    's20_2',
    db.Column('id', db.BigInteger, index=True),
    db.Column('학년도', db.Text),
    db.Column('학기', db.Text),
    db.Column('소속', db.Text),
    db.Column('학과', db.Text),
    db.Column('과목번호', db.Text),
    db.Column('분반', db.Text),
    db.Column('과목명', db.Text),
    db.Column('강의계획서', db.Text),
    db.Column('학점', db.BigInteger),
    db.Column('수업시간_강의실', db.Text),
    db.Column('시간', db.Text),
    db.Column('교수진', db.Text),
    db.Column('수강생수', db.Text),
    db.Column('영어강의', db.Text),
    db.Column('중국어강의', db.Text),
    db.Column('공학인증', db.Text),
    db.Column('국제학생', db.Text),
    db.Column('Honors과목', db.Text),
    db.Column('홀짝구분', db.Text),
    db.Column('승인과목', db.Text),
    db.Column('시험일자', db.Text),
    db.Column('수강대상', db.Text),
    db.Column('권장학년', db.Text),
    db.Column('수강신청_참조사항', db.Text),
    db.Column('과목_설명', db.Text),
    db.Column('비고', db.Text),
    db.Column('subject_id', db.Text),
    db.Column('department', db.Text),
    db.Column('요일', db.Text),
    db.Column('시작시간', db.Text),
    db.Column('종료시간', db.Text),
    db.Column('강의실', db.Text),
    db.Column('대면여부', db.Text),
    db.Column('강의언어', db.Text)
)



t_s20_s = db.Table(
    's20_s',
    db.Column('id', db.BigInteger, index=True),
    db.Column('학년도', db.Text),
    db.Column('학기', db.Text),
    db.Column('소속', db.Text),
    db.Column('학과', db.Text),
    db.Column('과목번호', db.Text),
    db.Column('분반', db.Text),
    db.Column('과목명', db.Text),
    db.Column('강의계획서', db.Text),
    db.Column('학점', db.BigInteger),
    db.Column('수업시간_강의실', db.Text),
    db.Column('시간', db.Text),
    db.Column('교수진', db.Text),
    db.Column('수강생수', db.Text),
    db.Column('영어강의', db.Text),
    db.Column('중국어강의', db.Text),
    db.Column('공학인증', db.Text),
    db.Column('국제학생', db.Text),
    db.Column('Honors과목', db.Text),
    db.Column('홀짝구분', db.Text),
    db.Column('승인과목', db.Text),
    db.Column('시험일자', db.Text),
    db.Column('수강대상', db.Text),
    db.Column('권장학년', db.Text),
    db.Column('수강신청_참조사항', db.Text),
    db.Column('과목_설명', db.Text),
    db.Column('비고', db.Text),
    db.Column('subject_id', db.Text),
    db.Column('department', db.Text),
    db.Column('요일', db.Text),
    db.Column('시작시간', db.Text),
    db.Column('종료시간', db.Text),
    db.Column('강의실', db.Text),
    db.Column('대면여부', db.Text),
    db.Column('강의언어', db.Text)
)



t_s20_w = db.Table(
    's20_w',
    db.Column('id', db.BigInteger, index=True),
    db.Column('학년도', db.Text),
    db.Column('학기', db.Text),
    db.Column('소속', db.Text),
    db.Column('학과', db.Text),
    db.Column('과목번호', db.Text),
    db.Column('분반', db.Text),
    db.Column('과목명', db.Text),
    db.Column('강의계획서', db.Text),
    db.Column('학점', db.BigInteger),
    db.Column('수업시간_강의실', db.Text),
    db.Column('시간', db.Text),
    db.Column('교수진', db.Text),
    db.Column('수강생수', db.Text),
    db.Column('영어강의', db.Text),
    db.Column('중국어강의', db.Text),
    db.Column('공학인증', db.Text),
    db.Column('국제학생', db.Text),
    db.Column('Honors과목', db.Text),
    db.Column('홀짝구분', db.Text),
    db.Column('승인과목', db.Text),
    db.Column('시험일자', db.Text),
    db.Column('수강대상', db.Text),
    db.Column('권장학년', db.Text),
    db.Column('수강신청_참조사항', db.Text),
    db.Column('과목_설명', db.Text),
    db.Column('비고', db.Text),
    db.Column('subject_id', db.Text),
    db.Column('department', db.Text),
    db.Column('요일', db.Text),
    db.Column('시작시간', db.Text),
    db.Column('종료시간', db.Text),
    db.Column('강의실', db.Text),
    db.Column('대면여부', db.Text),
    db.Column('강의언어', db.Text)
)



t_s21_1 = db.Table(
    's21_1',
    db.Column('id', db.BigInteger, index=True),
    db.Column('학년도', db.Text),
    db.Column('학기', db.Text),
    db.Column('소속', db.Text),
    db.Column('학과', db.Text),
    db.Column('과목번호', db.Text),
    db.Column('분반', db.Text),
    db.Column('과목명', db.Text),
    db.Column('강의계획서', db.Text),
    db.Column('학점', db.BigInteger),
    db.Column('수업시간_강의실', db.Text),
    db.Column('시간', db.Text),
    db.Column('교수진', db.Text),
    db.Column('수강생수', db.Text),
    db.Column('영어강의', db.Text),
    db.Column('중국어강의', db.Text),
    db.Column('공학인증', db.Text),
    db.Column('국제학생', db.Text),
    db.Column('Honors과목', db.Text),
    db.Column('홀짝구분', db.Text),
    db.Column('승인과목', db.Text),
    db.Column('시험일자', db.Text),
    db.Column('수강대상', db.Text),
    db.Column('권장학년', db.Text),
    db.Column('수강신청_참조사항', db.Text),
    db.Column('과목_설명', db.Text),
    db.Column('비고', db.Text),
    db.Column('subject_id', db.Text),
    db.Column('department', db.Text),
    db.Column('요일', db.Text),
    db.Column('시작시간', db.Text),
    db.Column('종료시간', db.Text),
    db.Column('강의실', db.Text),
    db.Column('대면여부', db.Text),
    db.Column('강의언어', db.Text)
)



t_s21_2 = db.Table(
    's21_2',
    db.Column('id', db.BigInteger, index=True),
    db.Column('학년도', db.Text),
    db.Column('학기', db.Text),
    db.Column('소속', db.Text),
    db.Column('학과', db.Text),
    db.Column('과목번호', db.Text),
    db.Column('분반', db.Text),
    db.Column('과목명', db.Text),
    db.Column('강의계획서', db.Text),
    db.Column('학점', db.BigInteger),
    db.Column('수업시간_강의실', db.Text),
    db.Column('시간', db.Text),
    db.Column('교수진', db.Text),
    db.Column('수강생수', db.Text),
    db.Column('영어강의', db.Text),
    db.Column('중국어강의', db.Text),
    db.Column('공학인증', db.Text),
    db.Column('국제학생', db.Text),
    db.Column('Honors과목', db.Text),
    db.Column('홀짝구분', db.Text),
    db.Column('승인과목', db.Text),
    db.Column('시험일자', db.Text),
    db.Column('수강대상', db.Text),
    db.Column('권장학년', db.Text),
    db.Column('수강신청_참조사항', db.Text),
    db.Column('과목_설명', db.Text),
    db.Column('비고', db.Text),
    db.Column('subject_id', db.Text),
    db.Column('department', db.Text),
    db.Column('요일', db.Text),
    db.Column('시작시간', db.Text),
    db.Column('종료시간', db.Text),
    db.Column('강의실', db.Text),
    db.Column('대면여부', db.Text),
    db.Column('강의언어', db.Text)
)



t_s21_s = db.Table(
    's21_s',
    db.Column('id', db.BigInteger, index=True),
    db.Column('학년도', db.Text),
    db.Column('학기', db.Text),
    db.Column('소속', db.Text),
    db.Column('학과', db.Text),
    db.Column('과목번호', db.Text),
    db.Column('분반', db.Text),
    db.Column('과목명', db.Text),
    db.Column('강의계획서', db.Text),
    db.Column('학점', db.BigInteger),
    db.Column('수업시간_강의실', db.Text),
    db.Column('시간', db.Text),
    db.Column('교수진', db.Text),
    db.Column('수강생수', db.Text),
    db.Column('영어강의', db.Text),
    db.Column('중국어강의', db.Text),
    db.Column('공학인증', db.Text),
    db.Column('국제학생', db.Text),
    db.Column('Honors과목', db.Text),
    db.Column('홀짝구분', db.Text),
    db.Column('승인과목', db.Text),
    db.Column('시험일자', db.Text),
    db.Column('수강대상', db.Text),
    db.Column('권장학년', db.Text),
    db.Column('수강신청_참조사항', db.Text),
    db.Column('과목_설명', db.Text),
    db.Column('비고', db.Text),
    db.Column('subject_id', db.Text),
    db.Column('department', db.Text),
    db.Column('요일', db.Text),
    db.Column('시작시간', db.Text),
    db.Column('종료시간', db.Text),
    db.Column('강의실', db.Text),
    db.Column('대면여부', db.Text),
    db.Column('강의언어', db.Text)
)



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    username = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String(120))
    registered_on = db.Column(db.DateTime, nullable=False)
    major = db.Column(db.String(120))
    public_id = db.Column(db.String(100), unique=True)
    verify_on = db.Column(db.Integer, nullable=False)
    verify_code = db.Column(db.String(20))

from .. import db
from sqlalchemy import PrimaryKeyConstraint

class t_departments(db.Model):
    
    __tablename__ = 'departments'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.BigInteger, primary_key=True, index=True)
    s18_1_text = db.Column(db.Text)
    s18_1_id = db.Column(db.Text)
    s18_s_text = db.Column(db.Text)
    s18_s_id = db.Column(db.Text)
    s18_2_text = db.Column(db.Text)
    s18_2_id = db.Column(db.Text)
    s18_w_text = db.Column(db.Text)
    s18_w_id = db.Column(db.Text)
    s19_1_text = db.Column(db.Text)
    s19_1_id = db.Column(db.Text)
    s19_s_text = db.Column(db.Text)
    s19_s_id = db.Column(db.Text)
    s19_2_text = db.Column(db.Text)
    s19_2_id = db.Column(db.Text)
    s19_w_text = db.Column(db.Text)
    s19_w_id = db.Column(db.Text)
    s20_1_text = db.Column(db.Text)
    s20_1_id = db.Column(db.Text)
    s20_s_text = db.Column(db.Text)
    s20_s_id = db.Column(db.Text)
    s20_2_text = db.Column(db.Text)
    s20_2_id = db.Column(db.Text)
    s20_w_text = db.Column(db.Text)
    s20_w_id = db.Column(db.Text)
    s21_1_text = db.Column(db.Text)
    s21_1_id = db.Column(db.Text)
    s21_s_text = db.Column(db.Text)
    s21_s_id = db.Column(db.Text)
    s21_2_text = db.Column(db.Text)
    s21_2_id = db.Column(db.Text)

class BaseMixin(object):
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.BigInteger, primary_key=True, index=True)
    학년도 = db.Column(db.Text)
    학기 = db.Column(db.Text)
    소속 = db.Column(db.Text)
    학과 = db.Column(db.Text)
    과목번호 = db.Column(db.Text)
    분반 = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    수업시간_강의실 = db.Column(db.Text)
    시간 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강생수 = db.Column(db.Text)
    영어강의 = db.Column(db.Text)
    중국어강의 = db.Column(db.Text)
    공학인증 = db.Column(db.Text)
    국제학생 = db.Column(db.Text)
    Honors과목 = db.Column(db.Text)
    홀짝구분 = db.Column(db.Text)
    승인과목 = db.Column(db.Text)
    시험일자 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    권장학년 = db.Column(db.Text)
    수강신청_참조사항 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    subject_id = db.Column(db.Text)
    department = db.Column(db.Text)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)

#2018
class s18_1(BaseMixin, db.Model):
  __tablename__ = 's18_1'
  
class s18_2(BaseMixin, db.Model):
  __tablename__ = 's18_2'
  
class s18_s(BaseMixin, db.Model):
  __tablename__ = 's18_s'
  
class s18_w(BaseMixin, db.Model):
  __tablename__ = 's18_w'
  
#2019
class s19_1(BaseMixin, db.Model):
  __tablename__ = 's19_1'
  
class s19_2(BaseMixin, db.Model):
  __tablename__ = 's19_2'
  
class s19_s(BaseMixin, db.Model):
  __tablename__ = 's19_s'
  
class s19_w(BaseMixin, db.Model):
  __tablename__ = 's19_w'
  
#2020
class s20_1(BaseMixin, db.Model):
  __tablename__ = 's20_1'
  
class s20_2(BaseMixin, db.Model):
  __tablename__ = 's20_2'
  
class s20_s(BaseMixin, db.Model):
  __tablename__ = 's20_s'
  
class s20_w(BaseMixin, db.Model):
  __tablename__ = 's20_w'
  
#2021
class s21_1(BaseMixin, db.Model):
  __tablename__ = 's21_1'
  
class s21_2(BaseMixin, db.Model):
  __tablename__ = 's21_2'
  
class s21_s(BaseMixin, db.Model):
  __tablename__ = 's21_s'
  
'''
class t_s20_1(db.Model):
    __tablename__ = 's20_1'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.BigInteger, primary_key=True, index=True)
    학년도 = db.Column(db.Text)
    학기 = db.Column(db.Text)
    소속 = db.Column(db.Text)
    학과 = db.Column(db.Text)
    과목번호 = db.Column(db.Text)
    분반 = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    수업시간_강의실 = db.Column(db.Text)
    시간 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강생수 = db.Column(db.Text)
    영어강의 = db.Column(db.Text)
    중국어강의 = db.Column(db.Text)
    공학인증 = db.Column(db.Text)
    국제학생 = db.Column(db.Text)
    Honors과목 = db.Column(db.Text)
    홀짝구분 = db.Column(db.Text)
    승인과목 = db.Column(db.Text)
    시험일자 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    권장학년 = db.Column(db.Text)
    수강신청_참조사항 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    subject_id = db.Column(db.Text)
    department = db.Column(db.Text)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)

class t_s20_2(db.Model):
    __tablename__ = 's20_2'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.BigInteger, primary_key=True, index=True)
    학년도 = db.Column(db.Text)
    학기 = db.Column(db.Text)
    소속 = db.Column(db.Text)
    학과 = db.Column(db.Text)
    과목번호 = db.Column(db.Text)
    분반 = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    수업시간_강의실 = db.Column(db.Text)
    시간 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강생수 = db.Column(db.Text)
    영어강의 = db.Column(db.Text)
    중국어강의 = db.Column(db.Text)
    공학인증 = db.Column(db.Text)
    국제학생 = db.Column(db.Text)
    Honors과목 = db.Column(db.Text)
    홀짝구분 = db.Column(db.Text)
    승인과목 = db.Column(db.Text)
    시험일자 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    권장학년 = db.Column(db.Text)
    수강신청_참조사항 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    subject_id = db.Column(db.Text)
    department = db.Column(db.Text)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)

class t_s20_s(db.Model):
    __tablename__ = 's20_s'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.BigInteger, primary_key=True, index=True)
    학년도 = db.Column(db.Text)
    학기 = db.Column(db.Text)
    소속 = db.Column(db.Text)
    학과 = db.Column(db.Text)
    과목번호 = db.Column(db.Text)
    분반 = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    수업시간_강의실 = db.Column(db.Text)
    시간 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강생수 = db.Column(db.Text)
    영어강의 = db.Column(db.Text)
    중국어강의 = db.Column(db.Text)
    공학인증 = db.Column(db.Text)
    국제학생 = db.Column(db.Text)
    Honors과목 = db.Column(db.Text)
    홀짝구분 = db.Column(db.Text)
    승인과목 = db.Column(db.Text)
    시험일자 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    권장학년 = db.Column(db.Text)
    수강신청_참조사항 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    subject_id = db.Column(db.Text)
    department = db.Column(db.Text)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)

class t_s20_w(db.Model):
    __tablename__ = 's20_w'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.BigInteger, primary_key=True, index=True)
    학년도 = db.Column(db.Text)
    학기 = db.Column(db.Text)
    소속 = db.Column(db.Text)
    학과 = db.Column(db.Text)
    과목번호 = db.Column(db.Text)
    분반 = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    수업시간_강의실 = db.Column(db.Text)
    시간 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강생수 = db.Column(db.Text)
    영어강의 = db.Column(db.Text)
    중국어강의 = db.Column(db.Text)
    공학인증 = db.Column(db.Text)
    국제학생 = db.Column(db.Text)
    Honors과목 = db.Column(db.Text)
    홀짝구분 = db.Column(db.Text)
    승인과목 = db.Column(db.Text)
    시험일자 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    권장학년 = db.Column(db.Text)
    수강신청_참조사항 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    subject_id = db.Column(db.Text)
    department = db.Column(db.Text)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)

class t_s21_1(db.Model):
    __tablename__ = 's21_1'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.BigInteger, primary_key=True, index=True)
    학년도 = db.Column(db.Text)
    학기 = db.Column(db.Text)
    소속 = db.Column(db.Text)
    학과 = db.Column(db.Text)
    과목번호 = db.Column(db.Text)
    분반 = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    수업시간_강의실 = db.Column(db.Text)
    시간 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강생수 = db.Column(db.Text)
    영어강의 = db.Column(db.Text)
    중국어강의 = db.Column(db.Text)
    공학인증 = db.Column(db.Text)
    국제학생 = db.Column(db.Text)
    Honors과목 = db.Column(db.Text)
    홀짝구분 = db.Column(db.Text)
    승인과목 = db.Column(db.Text)
    시험일자 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    권장학년 = db.Column(db.Text)
    수강신청_참조사항 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    subject_id = db.Column(db.Text)
    department = db.Column(db.Text)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)

class t_s21_2(db.Model):
    __tablename__ = 's21_2'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.BigInteger, primary_key=True, index=True)
    학년도 = db.Column(db.Text)
    학기 = db.Column(db.Text)
    소속 = db.Column(db.Text)
    학과 = db.Column(db.Text)
    과목번호 = db.Column(db.Text)
    분반 = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    수업시간_강의실 = db.Column(db.Text)
    시간 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강생수 = db.Column(db.Text)
    영어강의 = db.Column(db.Text)
    중국어강의 = db.Column(db.Text)
    공학인증 = db.Column(db.Text)
    국제학생 = db.Column(db.Text)
    Honors과목 = db.Column(db.Text)
    홀짝구분 = db.Column(db.Text)
    승인과목 = db.Column(db.Text)
    시험일자 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    권장학년 = db.Column(db.Text)
    수강신청_참조사항 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    subject_id = db.Column(db.Text)
    department = db.Column(db.Text)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)

class t_s21_s(db.Model):
    __tablename__ = 's21_s'
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.BigInteger, primary_key=True, index=True)
    학년도 = db.Column(db.Text)
    학기 = db.Column(db.Text)
    소속 = db.Column(db.Text)
    학과 = db.Column(db.Text)
    과목번호 = db.Column(db.Text)
    분반 = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    수업시간_강의실 = db.Column(db.Text)
    시간 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강생수 = db.Column(db.Text)
    영어강의 = db.Column(db.Text)
    중국어강의 = db.Column(db.Text)
    공학인증 = db.Column(db.Text)
    국제학생 = db.Column(db.Text)
    Honors과목 = db.Column(db.Text)
    홀짝구분 = db.Column(db.Text)
    승인과목 = db.Column(db.Text)
    시험일자 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    권장학년 = db.Column(db.Text)
    수강신청_참조사항 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    subject_id = db.Column(db.Text)
    department = db.Column(db.Text)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)
'''
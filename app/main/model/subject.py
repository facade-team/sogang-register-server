from .. import db

class Subject(db.Model):
    
    __tablename__ = 'total_data'
    __table_args__ = {'extend_existing': True} 
    
    id = db.Column(db.Integer, primary_key=True)
    subject_id = db.Column(db.Text)
    과목명 = db.Column(db.Text)
    강의계획서 = db.Column(db.Text)
    학점 = db.Column(db.BigInteger)
    요일 = db.Column(db.Text)
    시작시간 = db.Column(db.Text)
    종료시간 = db.Column(db.Text)
    강의실 = db.Column(db.Text)
    교수진 = db.Column(db.Text)
    수강대상 = db.Column(db.Text)
    과목_설명 = db.Column(db.Text)
    비고 = db.Column(db.Text)
    대면여부 = db.Column(db.Text)
    강의언어 = db.Column(db.Text)
    전인교육원 = db.Column(db.BigInteger)

    
    def __repr__(self):
        return '<Subject (%r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r)>' % (self.id, self.subject_id, self.과목명, self.강의계획서, self.학점, self.요일, self.시작시간, self.종료시간, self.강의실, self.교수진, self.수강대상, self.과목_설명, self.비고, self.대면여부, self.강의언어, self.전인교육원)
  
'''  
  학년도 = db.Column(db.Text)
  학기 = db.Column(db.Text)
  소속 = db.Column(db.Text)
  학과 = db.Column(db.Text)
  과목번호 = db.Column(db.Text)
  분반 = db.Column(db.Text)
  수업시간_강의실 = db.Column(db.Text)
  시간 = db.Column(db.Text)
  수강생수 = db.Column(db.Text)
  영어강의 = db.Column(db.Text)
  중국어강의 = db.Column(db.Text)
  공학인증 = db.Column(db.Text)
  국제학생 = db.Column(db.Text)
  Honors과목 = db.Column(db.Text)
  홀짝구분 = db.Column(db.Text)
  승인과목 = db.Column(db.Text)
  시험일자 = db.Column(db.Text)
  권장학년 = db.Column(db.Text)
  수강신청_참조사항 = db.Column(db.Text)
'''
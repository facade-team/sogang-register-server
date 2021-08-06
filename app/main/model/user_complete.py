from .. import db

class UserComplete(db.Model):
    """ UserComplete Model for storing completed subject"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    subject_id = db.Column(db.Text, unique=False, nullable=False)
    
    __tablename__ = 'user_complete'
    __table_args__ = {'extend_existing': True}
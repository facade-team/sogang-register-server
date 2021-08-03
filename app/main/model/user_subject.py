from .. import db

class UserSubject(db.Model):
    """ User Model for storing user related details """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    subject_id = db.Column(db.Text, unique=False, nullable=False)
    
    __tablename__ = 'user_subject'
    __table_args__ = {'extend_existing': True}
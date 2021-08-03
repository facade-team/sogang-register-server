from .. import db

class User(db.Model):
    """ User Model for storing user related details """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subject_id = db.Column(db.String(120), unique=True, nulable=True)
    
    __tablename__ = 'user_subject'
    __table_args__ = {'extend_existing': True}
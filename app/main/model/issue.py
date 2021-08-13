from .. import db

class Report(db.Model):
    """ User Model for storing user related details """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=False, nullable=False)
    title = db.Column(db.String(50), unique=False, nullable=False)
    script = db.Column(db.String(500), unique=False, nullable=False)
    useremail = db.Column(db.String(120), unique=False, nullable=True)
    
    __tablename__ = 'issue_report'
    __table_args__ = {'extend_existing': True}
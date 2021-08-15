from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
#import MySQLdb
from .config import config_by_name, mailConfig, host_name, username, password, database_name
# mail 관련 config, import
from flask_mail import Mail

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
mail = Mail()

# MySQLdb Connection Setting
#con = MySQLdb.connect(host=host_name, user=username, password=password, database=database_name, charset='utf8')
#cur = con.cursor();

def create_app(config_name): 
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    # SQLALCHEMY_POOL_SIZE 추가
    app.config['SQLALCHEMY_POOL_SIZE'] = 10
    app.config['SQLALCHEMY_MAX_OVERFLOW'] = 10
    app.config['SQLALCHEMY_POOL_RECYCLE'] = 30
    db.init_app(app)
    flask_bcrypt.init_app(app)
    #CORS(app)
    CORS(app, resources={r'*': {'origins': 'http://sogang-sincheong.com/'}})
    #CORS(app, resources={r'*': {'origins': '*'}})


    #mail 관련 config - main/config에 추가, mount
    # mail config
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = mailConfig[0]
    app.config['MAIL_PASSWORD'] = mailConfig[1]
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail.init_app(app)

    return app 
  
  

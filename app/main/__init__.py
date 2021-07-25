from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name, mailConfig

# mail 관련 config, import
from flask_mail import Mail

db = SQLAlchemy()
flask_bcrypt = Bcrypt()
mail = Mail()

def create_app(config_name): 
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

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
  
  
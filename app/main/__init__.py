from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

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
    mail.init_app(app)

    return app 
  
  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import pymysql
import MySQLdb

from .config import config_by_name, host_name, username, password, database_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

# MySQLdb Connection Setting
con = MySQLdb.connect(host=host_name, user=username, password=password, database=database_name, charset='utf8')
cur = con.cursor();

def create_app(config_name): 
    # 실제 실행
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)
    return app 
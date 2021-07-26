from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import pymysql
import MySQLdb

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

# test below
host_name = "docker-mysql-test.cpabptw8fwxo.us-east-2.rds.amazonaws.com"
username = "user"
password = "password"
database_name = "CRAWLING_TEST"
con = MySQLdb.connect(host=host_name, user=username, password=password, database=database_name, charset='utf8')
cur = con.cursor();

def create_app(config_name): 
    # 실제 실행
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    flask_bcrypt.init_app(app)

    return app 
  
  
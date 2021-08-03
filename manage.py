import os
import unittest
import sys
# app 폴더를 패키지로 인식하게끔 path 등록
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/app')

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, user_subject #model을 정의한 폴더 import
from app.main.model.subjects import t_departments, t_s20_1, t_s20_2, t_s20_s, t_s20_w, t_s21_1, t_s21_2, t_s21_s

# 환경 변수에서 필요한 매개 변수를 사용하여 응용 프로그램 인스턴스를 생성 초기에 만들어진 기능 - dev, prod, test. 환경 변수에 아무것도 설정되지 않은 경우 기본값 dev이 사용됩니다.
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev') 

app.register_blueprint(blueprint)

app.app_context().push()


manager = Manager(app) #Flask-Script를 통해 모든 데이터베이스 마이그레이션 명령을 노출. dbMigrateCommandadd_commandmanager

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
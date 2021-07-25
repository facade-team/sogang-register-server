from flask_mail import Message
from main import mail
from ..config import mailConfig

def sendmail(data):
    # target email 주소
    print(mail)
    print(mailConfig)
    
    client = data['email']

    msg = Message('Hello', sender = 'peter.hyunjae@gmail.com', recipients = [client])
    msg.body = "Hello Flask message sent from Flask-Mail"

    try:
       mail.send(msg)
       print('성공')
       return "성공"
    except Exception as e:
        print(e)
        print('실패')
        return "실패"
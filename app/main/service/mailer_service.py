from flask_mail import Message
from main import mail

def sendmail():
    msg = Message('Hello', sender = 'peter.hyunjae@gmail.com', recipients = ['peterhyunjae@naver.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"

    try:
       mail.send(msg)
    except Exception as e:
        print(e)
        return "send wrong"

    return "Sent"
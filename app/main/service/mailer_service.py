from flask_mail import Message
from main import mail

# email 보내기
def sendmail(data):
    # target email 주소
    client = data['email']

    msg = Message('Hello', sender = 'peter.hyunjae@gmail.com', recipients = [client])

    # 랜덤 인증 코드 생성 / 인증 링크 생성 후 전송 - redirect로 인증하게 하는 방법 (이것도 만료 시간 해놓아야 될듯)
    # 랜덤 인증 코드에 대해 세션 만료 시간 부여 (ex - 3분 안에 입력해야됨)
    # 인증

    msg.body = "Hello Flask message sent from Flask-Mail"

    try:
        mail.send(msg)
        return "성공"
    except Exception as e:
        print(e)
        return "실패"
from flask_mail import Message
from main import mail

# email 보내기
def sendmail(data):
    # target email 주소
    client = data['email']
    script = data['script']
    purpose = data['purpose']

    msg = Message('[Team Facade] - 서강신청 서비스입니다', sender = 'teamfacadesogang@gmail.com', recipients = [client])
 
    if purpose == 'register':
        msg.body = '이메일 인증 코드입니다. 인증란에 입력해 주세요. [ ' + script + ' ]'
    else:
        msg.body = '임시비밀번호 입니다. 로그인 후 비밀번호를 변경해 주세요. [ ' + script + ' ]'

    try:
        mail.send(msg)
        return "성공"
    except Exception as e:
        print(str(e))
        return "실패"

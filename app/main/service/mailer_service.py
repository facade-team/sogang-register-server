from flask_mail import Message
from main import mail

# email 보내기
def sendmail(data):
    # target email 주소
    client = data['email']
    script = data['script']
    purpose = data['purpose']

    print('email : ',client)
    print('email script : ', script)

    msg = Message('[Team Facade] - 서강신청 서비스입니다', sender = 'peter.hyunjae@gmail.com', recipients = [client])

    # 랜덤 인증 코드 생성 / 인증 링크 생성 후 전송 - redirect로 인증하게 하는 방법 (이것도 만료 시간 해놓아야 될듯)
    # 랜덤 인증 코드에 대해 세션 만료 시간 부여 (ex - 3분 안에 입력해야됨)
    # 인증

    #msg.body = "Hello Flask message sent from Flask-Mail"
    
    if purpose == 'register':
        msg.body = '이메일 인증 코드입니다. 인증란에 입력해 주세요. [ ' + script + ' ]'
    else:
        msg.body = '임시비밀번호 입니다. 로그인 후 비밀번호를 변경해 주세요. [ ' + script + ' ]'

    # return 'hello'

    try:
        mail.send(msg)
        return "성공"
    except Exception as e:
        print(e)
        return "실패"
# 🏫 Sogang-Register Server
서강대학교 개설교과목 정보 조회 서비스의 백엔드 서버 입니다.
여러 REST API를 제공하고 있습니다.

# ☁️ Deployed Environment
AWS EC2 우분투 서버에 REST API Server를 Docker를 이용해 배포했습니다.

# 🔧 Don't forget

* 개발 시작 전에 어떤 branch에 있는지 체크하기
* 중간중간에 꼭 commit 남기기
* push 하기 전에는 pull 하기
* 작업중인 위치가 container 내부인지, loacal인지 확인하기
* model이 바뀔 경우 꼭 update 날리기
* 잘 까먹는 명령어 checkout / add - commit - push

# Run

```bash
docker run - dp 5000:5000 -v "$(PWD):/home" -e FLASK_ENV=development sonic886/sogang-register
```

```
ctrl + shift + p 로 container 연결
```

# 🔧 Tech Stack
* Python Flask
  * REST API 개발 및 서버를 위한 웹 프레임워크
* Docker
  * 손쉬운 프로젝트 빌드 및 배포를 위한 수단
* AWS EC2
  * 배포용 서버 인스턴스
* AWS RDS
  * MySQL 데이터베이스 서버를 위한 인스턴스

# 📃 API List
## Auth
- [] Create account
- [] Request Secret
- [] Confirm Secret
- [] Login
- [] Log out
## User
- [] Register favorite subjects
- [] Register finished subjects
## Search
- [] Search all subjects

# 📞 Contact us
- 김승우 : seungwookim99
- 김현재 : itsnowkim
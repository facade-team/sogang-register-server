# 🏫 Sogang-Register Server

<p align='center'>
  <img align="center" src="/Logo.png" />
</p>
서강대학교 개설교과목 정보 조회 서비스의 백엔드 서버 입니다.

항상 시간표를 짜기 전, 수강신청을 하기 전 들어가는
'개설교과목정보 사이트'를 사용하며 느꼈던 문제점들을
조금이나마 개선하기 위해 시작하게 된 서비스입니다.

여러 REST API를 제공하고 있습니다.

# 🔧 Tech Stack

## Infra
<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a></div>
  </td>
  <td>
   <div align="center"><a href="https://www.docker.com/" target="_blank"> <img src="https://www.docker.com/sites/default/files/d8/2019-07/vertical-logo-monochromatic.png" alt="docker" width="40" height="40"/> </a></div>
  </td>
 </tr>
  <tr>
    <td align = "center">Git</td>
    <td align = "center">Docker</td>
  </tr>
</tbody></table>

## REST API

<table><tbody>
 <tr>
  <td width="75">
   <div align="center"><a href="https://www.python.org/" target="_blank"> <img src="https://www.python.org/static/community_logos/python-powered-h.svg" alt="Python" width="40" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg" alt="Flask" width="40" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://swagger.io/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Swagger-logo.png" alt="swagger" width="40" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://www.linux.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg" alt="linux" width="40" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://aws.amazon.com/ko/ec2/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/AWS_Simple_Icons_Compute_Amazon_EC2_Instances.svg" alt="AWS EC2" width="40" height="40"/> </a></div>
  </td>
  <td width="75">
   <div align="center"><a href="https://jwt.io" target="_blank"> <img src="https://jwt.io/img/pic_logo.svg" alt="jwt" width="40" height="40"/> </a></div>
  </td>
   <tr>
    <td align = "center">Python</td>
    <td align = "center">Flask</td>
     <td align = "center">Swagger</td>
     <td align = "center">Linux</td>
     <td align = "center">AWS EC2</td>
     <td align = "center">JWT</td>
  </tr>
 </tr>
 </tbody></table>

### Database

<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://www.mysql.com/" target="_blank"> <img src="https://www.mysql.com/common/logos/logo-mysql-170x115.png" alt="mysql" width="40" height="40"/> </a></div>
  </td>
  <td>
   <div align="center"><a href="https://aws.amazon.com/ko/rds/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/f/fc/AWS_Simple_Icons_Database_Amazon_RDS.svg" alt="aws rds" width="40" height="40"/> </a></div>
  </td>
 </tr>
  <tr>
    <td align = "center">MySQL</td>
    <td align = "center">AWS RDS</td>
  </tr>
</tbody></table>

### Crawler
<table><tbody>
 <tr>
  <td>
   <div align="center"><a href="https://www.python.org/" target="_blank"> <img src="https://www.python.org/static/community_logos/python-powered-h.svg" alt="Python" width="40" height="40"/></a></div>
  </td>
   <td>
   <div align="center"><a href="https://pandas.pydata.org/" target="_blank"> <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" alt="pandas" width="40" height="40"/> </a></div>
  </td>
   <td>
   <div align="center"><a href="https://www.selenium.dev/" target="_blank"> <img src="https://camo.githubusercontent.com/4b95df4d6ca7a01afc25d27159804dc5a7d0df41d8131aaf50c9f84847dfda21/68747470733a2f2f73656c656e69756d2e6465762f696d616765732f73656c656e69756d5f6c6f676f5f7371756172655f677265656e2e706e67" alt="selenium" width="40" height="40"/> </a></div>
  </td>
  <td>
   <div align="center"><a href="https://www.crummy.com/software/BeautifulSoup/" target="_blank"> <img src="https://user-images.githubusercontent.com/41292977/90748632-0f016700-e2f0-11ea-83ca-3cf2d80759ca.png" alt="beautiful soup" width="40" height="40"/> </a></div>
  </td>
 </tr>
  <tr>
    <td align = "center">Python</td>
    <td align = "center">Pandas</td>
    <td align = "center">Selenium</td>
    <td align = "center">BeautifulSoup</td>
  </tr>
</tbody></table>

# 🔧 Proejct Setup / and Organization

## Project structure

functional structure 구조를 사용하여 어떤 동작을 하는지에 따라 파일 구조를 구분하였습니다.

> We used functional structure to organize the files of the project by what they do.

```
.
├── app
│   ├── __init__.py
│   ├── main
│   │   ├── config.py
│   │   ├── controller
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── model
│   │   │   └── __init__.py
│   │   └── service
│   │       └── __init__.py
│   └── test
│       └── __init__.py
├── manage.py
└── requirements.txt
```

## Install required packages

사용한 패키지들은 `requirements.txt` 에 선언되어 있습니다.

```bash
pip install -r requirements.txt
```

## Config settings

here is an example:
```python
import os

host_name = 'yourhostname.com'
username = "name"
password = "password"
database_name = "your database name"

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = 'your secret key'
  algo = 'HS256'
  DEBUG = False
  
class DevelopmentConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'your databae url'
  DEBUG = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'your database url'
  DEBUG = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
  dev=DevelopmentConfig,
  prod=ProductionConfig,
) 

key = Config.SECRET_KEY
algorithm = Config.algo

mailConfig = ['youremail@email.com','email-password']

```

## Build

```bash
# $(pwd) = project root directory
docker build -t yourdockerusername/dockerfilename .
```
## Run

```bash
docker run -dp 5000:5000 yourdockerusername/dockerfilename
```

# 📃 API List

## Auth
- Create account
- Request Secret Code to User Email
- Confirm Secret Code
- Login
- Logout
- Search User Email
- Password Reset
- Password Change
- User withdrawal

## User
- Get User Favorite Subjects
- Register Favorite subjects
- Get User completed subjects
- Register completed subjects
- Delete Favorite Subjects
- Delete Completed Subjects
- Send report(Q&A) to our team

## Search
- Search all Subjects
- Search all Department at Selected Semester
- Search all Subjects by Search Options
- Search Updated Time

# 📞 Contact us
```
김승우 : seungwookim99
<a href='https://www.instagram.com/keemsw__/'>
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=Instagram&logoColor=white&link=https://www.instagram.com/keemsw__/"/>
</a>
<a href='mailto:sonicdx886@gmail.com'>
  <img src="https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=sonic886@gmail.com"/>
</a>
```

> 김현재 : itsnowkim
[📧 Email](peterhyunjae@naver.com)

이 소스는 제 6회 대한민국 SW 융합 해커톤에서 내가 개발한 백엔드 부분 내용이다.
결과적으로 이 소스코드는 '우수상'을 받는 데에 기여하였다.
우리 소스의 주제는 '층간소음 완화를 통한 소통 활성화'이다.

이 소스코드는 Python Django와 MySQL에 기반을 두고 있다.
그리고, 이 코드를 클라우드에 배포하기 위해 AWS EC2, RDS와 함께 연동하였다.
클라우드 환경(EC2)에서 Django를 활용하여 서버를 실행하였고, local에서 프로그래밍 후 본 github repository에 push하였다.
그리고 이 내용들을 클라우드에서 pull(클라우드는 오직 pull받기만 한다)하여 계속해서 업데이트하였다.

데이터베이스 테이블 구조를 먼저 설명하는게 편할 것 같다.
테이블은 총 3개이다. Home테이블, Status테이블, Notice테이블

쉽게 말해서 Home테이블은 집의 상태를 보여준다. 우리집에 센서가 언제부터 언제까지 작동하도록 되어 있으며, 우리 아파트의 주소와 우리집 구체적은 호수를 포함한다.
Status테이블은 센서를 통해 실시간으로 받은 데이터를 전송받는 테이블이다. 몇시에 도착한 센서 정보는 어느정도 수치의 소음, 진동 값을 포함하고 있는지를 보여준다.
이 때에 그 센서 값이 어떤 집의 내용을 포함하는지가 있어야 하기 때문에 foreignkey로 연결하였다.
Notice테이블은 어플리케이션에서 보여주는 공지내용을 보여준다. 공지가 언제 올라왔으며 이는 어떤 내용을 포함하는지, 간단한 내용을 보여준다.


Django Rest Framework에 대해 간단히 설명하자면, Python을 이용하여 쉽게 서버를 만들 수 있는 Framework이다.
Django는 여러가지 Python 파일들로 구성되게 된다. 간단히 구성 파일들에 대해 설명해보도록 하겠다.
1. Settings.py : 전체적인 세팅을 말하는 것이다. 포함된 라이브러리나, 데이터베이스 host, user, password 등의 정보를 담고 있다. 이 소스코드 속 데이터베이스 관련 정보로는 나의 개인 AWS EC2 정보를 담았으며, 현재는 그 인스턴스가 종료되어 있는 상태이다. 또한 이 소스코드에는 추가적으로 Web과 백엔드가 연동하는 과정에서 발생하는 Cross Domain을 완화하기 위한 코드가 더해졌다.
2. models.py : 데이터베이스 스키마 구조를 담고있다고 보면 된다. models.py를 수정하고, 이를 이용하여 migration하게 되면 DB에 자동으로 반영되게 된다. 이 때에 중요한 개념이 바로 migration인데, 그 과정에서 manage.py 파일을 거치게 된다.
3. views.py : 쉽게 말해서 API를 만드는 파이썬 파일이라고 보면 될 것 같다. 이 파일에 입력한 내용을 통해서 프론트가 그 내용을 받아 자신이 원하는 기능을 보여줄 수 있다.
4. urls.py : views.py와 연동되어 RestAPI의 기능을 보여준다. views.py에 속한 여러가지 기능들을 url로 나타내어주는 역할을 한다.
5. manage.py : 어쩌면 가장 중요할 수도 있지만, 가장 간단한 파이썬 파일이다. 코드는 매우 짧다고 보면 된다. 이를 이용하여 여러가지 기능들을 수행할 수 있다. 해당 기능들을 나열해 보겠다.
    - python manage.py runserver : 서버를 실행시키는 용도를 하는 command line 명령어이다.
    - python manage.py makemigrations : 데이터베이스 테이블 스키마를 변경시켰을 때 그것을 문서화하기 위한 작업이라고 보면 될 것이다.
    - python manage.py migrate : models.py 파일을 전체적으로 훑으면서 데이터베이스에 수정된 내용을 반영하는 command line 명령어이다. 이 때에 변경된 내                                  없다면, 그냥 "no changes ..." 라는 내용이 나타날 것이다.
지금까지 전체적인 Django의 개념에 대해 설명하였다.

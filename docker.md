# Docker

## Feature

- ✔컨테이너 상호작용 가능
- ✔volume 옵션으로 로컬코드와 개발서버를 연동
- ✔db컨테이너 죽으면 날라가기때문에 로컬에 저장할 것
- ✔docker run과 함께 설정한 장황한 옵션들을 도커 컴포즈로 - 설정해놓음
- •Dockerfile -> Dockerfile-dev : 서버구성
- •docker build -> docker-compose build : 이미지 생성
- •docker run 옵션들 -> docker-compose.yml : 옵션들(인스턴스 - 변수들)
- •docker run -> docker-compose up : 인스턴스 생성, 컨테이너 - 생성과 실행 동시에?
- ✔한 서비스(컨테이너)에 여러 컨테이너가 포함가능

## Command

- docker pull ubuntu:latest\
  이미지 받기
- docker run --name 컨테이너이름 이미지이름 실행할파일\
  컨테이너 - 생성
- docker ps\
  모든 컨테이너 목록 출력
- docker start 컨테이너이름or컨테이너ID\
  컨테이너 시작
- docker restart 컨테이너이름or컨테이너ID
- docker attach 컨테이너이름or컨테이너ID\
  시작한 컨테이너에 - 접속, CTRL P, CTRL Q하면 정지하지않고 쉘 빠져나옴
- docker exec 컨테이너이름or컨테이너ID echo "외부에서 컨테이너에 - 명령 실행"
- docker stop 컨테이너이름
- docker rm 컨테이너이름
- docker rmi 이미지이름:태그\
  태그 생략시 모든 이미지이름을 삭제
- docker build --tag 이름:버젼\
  작성한 Dockerfile로 이미지 생성, - --tag로 이미지 이름지정, 버젼생략 시 latest가 디폴트
- docker images\
  이미지 목록 출력
- docker run --name 이름 -d -p 80:80 -v /root/data:/data 이미지명\
  -d: 백그라운드로 실행, -p: 호스트80과 컨테이너80 포트를 - 연결하고 외부노출시킴 -> localhost:80으로 접속\
  -v: 호스트의 /root/data 디렉토리를 컨테이너의 /data - 디렉토리에 연결

- Example
  - docker build . -f Dockerfile.dev -t clientimages\
    현재경로에서, - 파일지정, clientimages이름으로 이미지 생성(태그지정 마지막에 - 적어야함)
  - docker run --name clientcontainer -d -p 3000:80 clientimages

## docker-compose Command

- docker-compose up -d\
  서비스생성 + 이미지 빌드 + 서비스 실행, - -d: 백그라운드 실행
- docker-compose ps\
  실행중 서비스 확인
- docker-compose stop
- docker-compose start
- docker-compose down --volume\
  서비스 초기화(서비스, 네트워크 - 삭제), 볼륨까지 삭제
- docker-compose down --volume --rmi all
- docker-compose exec 컨테이너이름 명령어
- docker-compose logs 컨테이너이름 -f\
  -f: 팔로잉

- docker-compose.yml
- ports옵션 과 env_file옵션에 세팅한 파일 내 PORT 은 동일 ?
- dockerfile의 expose - they’ll only be accessible to linked - services, 어쨋든 컨테이너끼리 통신

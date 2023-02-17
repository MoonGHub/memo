# Docker

CYCLE\
DockerFile > Image > Container

## Command

### 생성

- `docker build . -f DockerFile -t imagename`\
  DockerFile로 이미지 생성
- `docker pull ubuntu:latest`\
  이미지 받기
- `docker build --tag 이미지이름:버젼`\
  작성한 DockerFile로 이미지 생성\
  버젼 생략 시 latest가 디폴트

### 실행

- `docker run --name 컨테이너이름 -d -p 80:80 -v /root/data:/data 이미지명 실행파일명`\
  컨테이너 생성 및 실행
  - -d: 백그라운드로 실행
  - -p: 호스트80과 컨테이너80 포트를 - 연결하고 외부노출시킴 -> localhost:80으로 접속
  - -v: 호스트의 /root/data 디렉토리를 컨테이너의 /data 디렉토리에 연결
- `docker start 컨테이너이름or컨테이너ID`
- `docker restart 컨테이너이름or컨테이너ID`
- `docker stop 컨테이너이름`

### 삭제

- `docker rm 컨테이너이름`
- `docker rmi 이미지이름:태그`\
  태그 생략시 모든 이미지이름을 삭제
  - -f: --force

### 기타

- `docker ps`\
  모든 컨테이너 목록 출력
- `docker images`\
  이미지 목록 출력
- `docker attach 컨테이너이름or컨테이너ID`\
  시작한 컨테이너에 접속, CTRL P, CTRL Q하면 정지하지않고 쉘을 빠져나옴
- `docker exec 컨테이너이름or컨테이너ID echo "외부에서 컨테이너에 - 명령 실행"`

### Example

- `docker build . -f DockerFile.dev -t clientimages`\
  현재 경로에서 파일지정\
  clientimages이름으로 이미지 생성(태그지정 마지막에 적어야함)
- `docker run --name clientcontainer -d -p 3000:80 clientimages`

---

## docker-compose

- `docker-compose down --volume --rmi all`\
  서비스 초기화(서비스, 네트워크 삭제)
  - --volume: 볼륨 삭제
  - --rmi all: 싹 다 지움
- `docker-compose up -d`\
  `docker-compose -f docker-compose.teamcity.yml up`\
  서비스생성 > 이미지 빌드 > 컨테이너 생성 및 실행(서비스 실행)
  - -d: 백그라운드 실행
  - --platform linux/amd64: m1인 경우 옵션 추가
- `docker-compose ps`\
- `docker-compose stop`
- `docker-compose start`
- `docker-compose exec 컨테이너이름 명령어`
- `docker-compose logs 컨테이너이름 -f`\
  - -f: 팔로잉

### Question

- ports옵션 과 env_file옵션에 세팅한 파일 내 PORT 은 동일 ?
- DockerFile의 expose - they’ll only be accessible to linked - services, 어쨋든 컨테이너끼리 통신?
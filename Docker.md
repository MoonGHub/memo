# Docker

> CYCLE: DockerFile > Image > Container(=이미지 인스턴스)

- [Install](#install)
- [Command](#command)
  - [생성](#생성)
  - [실행](#실행)
  - [삭제](#삭제)
  - [기타](#기타)
  - [Docker Hub](#docker-hub)
- [docker-compose](#docker-compose)
- [PBL](#pbl)
- [docker swarm](#docker-swarm)

## Install

1. `curl -fsSL https://get.docker.com -o get-docker.sh`
2. `sh get-docker.sh`
3. `docker info` 또는 `systemctl status docker` 또는 `snap services`
4. `apt install docker-compose`

---

## Command

### 생성

- `docker build . -f DockerFile -t imagename`: DockerFile로 이미지 생성
  - ex) `docker build . -f ./apps/web/app.tetherbit/ci-cd/dev/Dockerfile -t answlgus1122/app:app.tetherbit-dev --no-cache --progress=plain`
  - ex) `docker build . -f DockerFile.dev -t clientimages`\
     현재 경로에서 파일지정, clientimages이름으로 이미지 생성(태그지정 마지막에 적어야함)
- `docker pull ubuntu:latest`: 이미지 받기
- `docker build --tag 이미지이름:버젼`: 작성한 DockerFile로 이미지 생성하며, 버젼 생략 시 latest가 디폴트

#### 네트워크

> - docker-compose를 사용하는 경우, 기본적으로 bridge 네트워크가 사용됨
> - 개별적으로 실행하는 경우 같은 네트워크를 지정해야 컨테이너끼리 통신이 가능

- `docker network create my-network`
- `docker network ls`
- `docker network inspect 네트워크이름`

<br />

### 실행

- `docker run --name 컨테이너이름 --restart=always -d -p 80:80 -v /root/data:/data 이미지명 실행파일명`: 컨테이너 생성 및 실행
  - `-d`: 백그라운드로 실행
  - `-p`: 호스트80과 컨테이너80 포트를 - 연결하고 외부노출시킴 -> localhost:80으로 접속
  - `-v`: 호스트의 /root/data 디렉토리를 컨테이너의 /data 디렉토리에 연결
  - ex) `docker run --name dev -d --network my-network answlgus1122/app:app.tetherbit-dev`
  - ex) `docker run --name clientcontainer -d -p 3000:80 clientimages`
- `docker start 컨테이너이름or컨테이너ID`
- `docker restart 컨테이너이름or컨테이너ID`
- `docker stop 컨테이너이름`

#### 업데이트

- `docker update --restart=always 컨테이너이름`

<br />

### 삭제

- `docker rm 컨테이너이름`
- `docker rmi 이미지이름:태그`: 태그 생략시 모든 이미지이름을 삭제
  - `-f`: --force
  - ex) `docker rm dev &&  docker rmi answlgus1122/app:app.tetherbit-dev`
- `docker container prune --force`
- `docker image prune --force`
  - `-all`: 사용중인 이미지도 삭제
- `docker builder prune --force`: 빌드 캐시 제거
- `docker volume prune --force`
- `docker system prune -a --volumes --force`: 미사용 오브젝트 모두 제거

### 기타

- `docker ps -a`: 모든 컨테이너 목록 출력
- `docker images`: 이미지 목록 출력
- `docker attach 컨테이너이름or컨테이너ID`: 컨테이너에 접속
  - 실행시의 foreground 환경이 보여짐
  - CTRL P, CTRL Q하면 정지하지않고 쉘을 빠져나옴
- `docker exec 컨테이너이름or컨테이너ID echo "외부에서 컨테이너에 - 명령 실행"`: 외부에서 컨테이너에 명령 전달
- `docker exec -it 컨테이너이름or컨테이너ID /bin/sh`: 컨테이너에 접속
  - `-i`: 표준입출력 STDIN를 열겠다는 의미
  - `-t`: 가상 tty(pesudo tty)를 통해 접속하겠다는 의미
- `docker logs 컨테이너이름`: 해당 컨테이너에 출력된 로그 확인
  - `-f`: follow

### Docker Hub

- 검색 및 다운로드
  - `docker search nginx`
  - `docker pull nginx:latest`: 태그 생략 가능
- 이미지 업로드 및 다운로드
  - `docker login`
  - `docker tag <IMAGE_ID> <NEW_IMAGE_NAME>:<NEW_TAG>`: 로컬 이미지의 이름 및 태그 변경
    - `docker tag app_nginx answlgus1122/app:nginx`
    - `docker tag mysql:8.0 answlgus1122/app:mysql`
  - `docker push answlgus1122/app:myapp`: 도커 허브의 repository에 업로드
  - `docker pull -a answlgus1122/app`: 도커 허브에서 다운로드

---

## docker-compose

- `docker-compose down --volume --rmi all`: 서비스 초기화(서비스, 네트워크 삭제)
  - `--volume`: 볼륨 삭제
  - `--rmi all`: 싹 다 지움
- `docker-compose -p 프로젝트명 up -d`\
  `docker-compose -f docker-compose.teamcity.yml up`\
  _서비스생성 > 이미지 빌드 > 컨테이너 생성 및 실행(서비스 실행)_
  - `-p`: image이름으로 '현재 디렉토리 명\_'가 붙는데, 이것을 수정
  - `-d`: 백그라운드 실행
  - `--platform linux/amd64`: m1인 경우 옵션 추가
- `docker-compose ps`
- `docker-compose stop`
  - `docker-compose stop 컨테이너이름`
  - `docker-compose rm -fsv 컨테이너이름`
    - `-f`: force
    - `-s`: stop
    - `-v`: volume
- `docker-compose start`
- `docker-compose restart`
- `docker-compose exec 컨테이너이름 명령어`: 개별 서비스 컨트롤
- `docker-compose logs 컨테이너이름 -f`: 해당 컨테이너에 출력된 로그 확인
  - `-f`: follow

---

## PBL

- 인스턴스 실행 시, `--build` 옵션을 주면 docker-compose의 경우 dockerfile내의 `RUN`과 같은 명령어도 수행 됨
- dockerfile의 `COPY`에서 디렉토리로 복사하는 경우, `/` 를 붙여줘야 함
- `env_file`옵션은 컨테이너 내부 환경 변수 설정
- DockerFile의 `EXPOSE`는 포트 사용을 명시적으로 나타기위한 메타데이터
- DockerFile실행 시의 CLI의 `-v`옵션 또는 `docker-compose.yml`의 `volumes`옵션을 설정 시, `로컬경로:컨테이너경로`로 마운트되며\
  `:`사용하지 않고 단일경로로 설정 시, 설정한 로컬경로를 컨테이너의 동일 경로로 마운트
  - `:ro`: Read-Only 마운트
  - `:rw`: Read-Write

---

## docker swarm

- docker swarm init
- docker swarm join-token worker
- docker swarm leave --force

- docker node ls
- docker node demote NODE
- docker node rm NODE

- docker stack deploy -c docker-stack.yml stack_name
- docker stack ls
- docker stack rm STACK

- docker service ps stack_name_ser/Users/moong/workspace/drill-git/Users/moong/workspace/drill-git/mysql.sql/mysql.sqlvice_name
- docker service ls

- docker stack deploy -c docker-stack.development.yml app

- --Docker-compose up failing because "port is already allocated"

- docker-compose down
- docker rm -fv $(docker ps -aq)
- lsof -i -P -n | grep 5432

출처: https://nayha.tistory.com/625 [Nayha]

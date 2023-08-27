# OS - Jenkins

## 도커로 설치

1. `docker pull jenkins/jenkins:lts`
2. ```sh
   sudo docker run -d -p 8282:8080 \
     -v /jenkins:/var/jenkins_home \
     -v /var/run/docker.sock:/var/run/docker.sock \
     --name jenkins -u root \
     jenkins/jenkins:lts
   ```
3. `docker exec -it jenkins /bin/sh`
4. 젠킨스 내 도커설치
   - alphine이 아닌 경우 [참고](../Docker.md#install)
   - alphine인 경우
     1. `apk update && apk upgrade`
     2. `apk add docker && apk add docker-compose`

<br />

## Jenkins - Git Repo 연동

### SSH Key 등록

1. `ssh-keygen`로 key 생성(나머지 Enter로 패스)
2. Git에 등록
   1. Git 해당 Repo의 설정 > Deploy Keys > Add deploy key
   2. 1.에서 생성한 id_rsa.pub의 내용을 복사/붙여넣기 (ssh-rsa로 시작)
3. Jenkins에 등록
   1. Dashboard > Manage Jenkins > Configure Global Security > Git Host Key Verification Configuration. 에서(제일 아래)\
      Accept first connection 선택
   2. Dashboard > Manage Jenkins > Credentials > System > Global credentials (unrestricted) > Add Credentials
      - Kind: SSH Username with private key
      - Global (Jenkins, nodes, items, all child items, etc) 선택
      - Username: 키 선택시의 표시 이름
      - Private Key > Enter directly > 1.에서 생성한 id_rsa의 내용을 복사/붙여넣기 (-----BEGIN 으로 시작)
   3. `ssh -T git@github.com` 실행

<br />

### Jenkins 아이템 생성

1. Freestyle project
2. General >
   - GitHub project > Project url: 해당 Repo의 URL
3. 소스코드 관리 > Git >

   - Repository Url: Clone할 때의 SSH URL
   - Credentials: 추가한 키 선택
   - Branch Specifier: \*/main

4. 빌드 유발 > GitHub hook trigger for GITScm polling 선택
5. 빌드 환경 > Delete workspace before build starts 선택
6. Build Steps > Execute shell
   ```sh
   cd ./apps/web/io.yougram/docker
   bash jenkins-build-step.sh
   ```
   <br />

### Git Hook 등록

1. 해당 Git repo의 설정 > Webhooks
2. Payload URL 입력
3. Content type: application/json
4. Just the push event, Active 선택(디폴트)
5. HAproxy설정 추가 - [참고](./OPNsense.md#haproxy---리버스-프록시-설정)

## ETC

### Jenkins 재실행

브라우저에서 `Jenkins URL/restart` 또는 도커 명령어로 재실행

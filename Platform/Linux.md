# Platform - Linux

## Shortcut

- `Ctrl l`: Clear Terminal

---

## Command

- man
- history
- mv
- cp
- rm
- ls
- tar
- file
- tee
- grep
  - -i: 대소문자 구분 없이
  - -E: egrep과 동일하게 확장된 정규식 사용이 가능
  - -v: 일치하는 라인을 제외하고 출력
- egrep
  - grep보다 확장된 정규식 사용이 가능
  - -v: 일치하는 라인을 제외하고 출력
- head tail
- tr
- sed
- cut
- wc
- od
- split
- md5, sha256, sha512
- find
- vim
  - 다음 찾기
    - `/{검색어}`
    - 엔터
    - `n`
  - 이전 찾기
    - `/{검색어}`
    - 엔터
    - `N`
  - 찾기 유지
    - `:noh`
    - 엔터
    - `/{검색어}`
    - 엔터
- ps
- top
- nice
- renice
- jobs
- uptime
- kill
- killall
- pkill
- pgrep
- systemctl
- snap
- netstat
  - -a: 모든 연결 및 수신 대기 포트 표시
  - -n: 주소나 포트 형식을 숫자로 표시
  - -l: listen중인 포트 표시
  - -c: 매 초마다 실행
- `more [파일명]`
  파일을 읽어 화면 단위로 끊어서 출력(지나간 내용 다시 볼 수 없음)

<br />

- FHS
- 프롬프트 단축기
- 파일검색
- 문자열검색
- 메타캐릭터&기술자
- 환경변수

---

## Ubuntu(22.04.1 live server amd64)

[참고](https://blog.dalso.org/article/ubuntu-22-04-lts-server-install)
[참고](https://as-you-say.tistory.com/181)

> 설치 시, 주의 사항

1. Profile setup
   - Your name: 사용자의 실제 이름 또는 관리자의 이름
     - 노출 되는 곳 없음(아마)
     - Your Pick a username과 동일히 작성
   - Your server's name: 프롬프트의 유저명@{이부분}
     - 마침표(.) 입력 불가
     - 언더바는 입력은 되지만 생략댐
   - Your Pick a username: 사용자의 시스템 로그인 아이디. 프롬프트의 {이부분}@서버명
     - 언더바 인식 됨
     - 초기 계정의 로그인 아이디
2. 추가적 설치는 불필요

**설치 후, 업데이트 및 필요 패키지 설치**

```shell
apt update
apt upgrade
apt install curl net-tools
apt-get update && apt-get install apt-file -y && apt-file update && apt-get install vim -y
```

- 기타 Command
  - `sudo passwd root`: Root계정 패스워드 설정
  - `sudo su` or `sudo -`: Root계정 전환(설치 직후는 패스워드 설정이 필요)
  - `uname -a` 또는 `uname -r`: 커널 버전 확인

> 설치 후, 재설치 방법

1. F2로 Bios 진입
2. 부팅 순서에서 CD를 최상위로 설정
3. 재부팅

---

## PBL - 여러 설정 및 명령어

### 방화벽 및 SSH 설정, 접속(Ubuntu/Debian)

#### 방화벽 설정

- `ufw status`
- `ufw enable`\
  방화벽 활성화
  ```text
  # 실행 후, ufw status
  Status: active
  ```
- `ufw disable`

#### 방화벽 SSH 설정

- `systemctl status ssh`\
  ssh 서비스 실행 확인
- `ss -tuln | grep ssh`\
  ssh 접속 포트 확인
- `ufw allow ssh`\
  SSH 포트(기본값은 22번) 허용

  ```text
  # 실행 후, ufw status
  Status: active

  To  Action  From
  --  ----    ----
  22/tcp  ALLOW Anywhere
  22/tcp (v6) ALLOW Anywhere (v6)
  ```

- `ufw deny ssh`\
  SSH 포트 거부

> ~~**일반계정 비밀번호 ssh접속 허용**~~\
> ~~/etc/ssh/sshd_config에서 PasswordAuthentication yes 주석 해제~~

> **root계정 ssh 접속 허용**\
> /etc/ssh/sshd_config에서 PermitRootLogin 라인 주석 해제

#### 접속

- `ssh username@host`
- `ssh -i [pem/file/path] ubuntu@3.35.129.200`
  - `*.pem`파일의 권한은 `chmod 400` 부여
  - 서버 아이피가 동일 하며, 서버를 다시 설치 했을 경우 ~/.ssh/known_hosts 를 제거

#### 접속 IP 제한

<br />

### 권한 설정

#### 도커

- `ls -l /var/run/docker.sock`\
  그룹명 확인
- `sudo usermod -aG docker [username]`\
  그룹(docker)에 유저 추가
- `grep docker /etc/group`\
  그룹(docker)에 [username]이 추가되었는지 확인
- `systemctl restart docker` 또는 `newgrp docker`
  - restart시에는 도커 컨테이너 재실행 필요
  - newgrp은 바로 적용
- 해당 유저로 재 로그인하여 확인

<br />

### **apt** vs **yum**

`apt`: Debian 및 Ubuntu에서 사용

- 아래 명령어들의 결합
  - `apt-get`: 패키지 설치, 업데이트 및 제거
  - `apt-cache`: 패키지 조회
  - `dpkg`: 시스템에 설치된 패키지 조회

`yum`: Redhat계열에서 사용

- Redhat계열 Linux
  - Red Hat Enterprise
  - Fedora
  - CentOS

<br />

### 쉘 확인

`grep root /etc/passwd`: root사용자에 대한 정보 확인\
`cat /etc/shells`: 현재 사용 가능한 쉘 확인

<br />

### background 실행 및 foreground, background 전환

- background로 실행\
  `명령어 &`: background 실행 - 끝에 `&`를 붙여줌

- background로 전환

  1. `ctrl z`: 중지 상태로 변경
  2. `jobs`
  3. `bg %[jobs의 task number]`\
     ex) `bg %2`

- foreground로 전환
  1. `jobs`
  2. `fg %[jobs의 task number]`\
     ex) `fg %1`

<br />

### 재부팅 및 종료

재부팅: `sudo reboot` 또는 `sudo shutdown -r now`\
종료: `sudo shutdown -h now` 또는 `sudo poweroff`

<br />

### 부트로더 GNU GRUB 진입 방법

1. `sudo vim /etc/default/grub`
2. 아래와 같이 해당 값을 변경
   ```
   GRUB_TIMEOUT_STYLE=menu
   GRUB_TIMEOUT=10
   ```
3. `sudo update-grub`
4. 재부팅

<br />

### **service** vs **systemctl**

최근 리눅스 버전에서는 init데몬 대신에 systemd데몬을 사용하여 프로세스를 관리

- `service`: init데몬 사용\
  사용법)
  - `service 서비스명 status`
  - `service 서비스명 start`
- `systemctl`: systemd데몬 사용
  사용법)
  - `systemctl status 서비스명`

<br />

### 서비스 등록

#### initd

#### systemd

1. 서비스 유닛 파일 생성

   - `/etc/systemd/system/myapp.service`

     ```ini
     [Unit]
     Description=My App Service
     After=network.target # 네트워크가 준비된 다음에 이 서비스를 시작

     [Service]
     WorkingDirectory=/var/services
     ExecStart=/usr/bin/node myapp/index.js
     # ExecStart=/usr/bin/java -jar myapp/myapp-0.0.1-SNAPSHOT.jar
     User=ubuntu
     SuccessExitStatus=143 # 128 + 15(SIGTERM)
     Restart=on-failure
     Environment=NODE_ENV=production

     [Install]
     WantedBy=multi-user.target # systemd의 대상, CLI 기반 시스템/서버 모드일 때 사용
     ```

2. 권한 부여
   - `sudo chmod 644 /etc/systemd/system/myapp.service`
3. 서비스 인식
   - `sudo systemctl daemon-reload`
4. 서비스 실행 및 확인
   - `sudo systemctl start myapp`
   - `sudo systemctl status myapp`
5. 서비스 자동 실행(부팅시)
   - `sudo systemctl enable myapp`

**로그 확인**

- `sudo journalctl -u {서비스명}.service -f`
  - `-u`: 서비스 지정
  - `-f`: 실시간

<br />

### LVM(Logical Volume Manager) 볼륨 사이즈 확장

<br />

### 특정 (네트워크)포트 확인 및 종료

- 사용 중인 포트 확인
  ```shell
    sudo lsof -i :8081
    sudo kill -9 PID
  ```
- 네트워크 포트 확인
  ```shell
  netstat -na | grep -i 7777
  ```

<br />

### 타임존 한국표준시(KST)로 변경

1. 현재 시간 확인 (현재 타임존)
   - `date`
2. 현재 타임존 확인
   - `ls -al /etc/localtime`
3. 타임존을 한국 표준시(KST)로 변경
   - `ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime`
4. 변경된 타임존 확인
   - `ls -al /etc/localtime`
5. 현재 시간 확인 (현재 타임존)
   - `date`

<br />

### 용량/메모리 확인

- `swapon -s`: swap 메모리 확인
- `df -h`
- `du -h`
  - -s: 디렉토리의 사용량만 표시
  - ex) `du -sh *`: 현재 경로 내의 폴더, 파일의 용량 표시

<br />

### [한글 설치(ubuntu live server)](https://epicarts.tistory.com/30)

<!--
- `apt-get isntall language-pack-ko`
- `locale-gen ko.KR.UTF-8`
- `vim /etc/default/locale`\
  추가 `LANG=ko_KR.UTF-8`
- `vim /etc/environment`\
  추가
  ```shell
  LANG=ko_KR.UTF8
  LANGUAGE=ko_KR:ko:en_GB:en
  ```
- `reboot` -->

<br />

### preflight의 OPTIONS 응답 확인

`curl -X OPTIONS -i <요청 URL>`

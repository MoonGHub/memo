# OS - Linux

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

---

- FHS
- 프롬프트 단축기
- 파일검색
- 문자열검색
- 메타캐릭터&기술자
- 환경변수

---

## LVM(Logical Volume Manager) 볼륨 사이즈 확장

---

## Ubuntu

설치 후, 업데이트 및 필요 패키지 설치

```shell
apt update
apt install net-tools

4. sudo apt install apt-transport-https ca-certificates curl software-properties-common
5. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
6. sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
7. sudo apt update
8. apt-cache policy docker-ce
docker-ce:
  Installed: (none). —> 도커가 아직 설치 안됨
9. sudo apt install docker-ce
10. sudo systemctl status docker


```

- 기타 Command
  - `sudo passwd root`: Root계정 패스워드 설정
  - `sudo su` or `sudo -`: Root계정 전환(설치 직후는 패스워드 설정이 필요)
  -

### 🦋 SSH 접속

- Lightsail
  1. 서버 아이피가 동일 하며, 서버를 다시 설치 했을 경우 ~/.ssh/known_hosts 를 제거
  2. ssh -i /Users/moong/Downloads/LightsailDefaultKey-ap-northeast-2.pem ubuntu@3.35.129.200

### 🦋 **apt** vs **yum**

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

### 🦋 쉘 확인

`grep root /etc/passwd`: root사용자에 대한 정보 확인\
`cat /etc/shells`: 현재 사용 가능한 쉘 확인

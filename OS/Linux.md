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
- systemctl
- snap

---

- FHS
- 프롬프트 단축기
- 파일검색
- 문자열검색
- 메타캐릭터&기술자
- 환경변수

---

### 🦋 **service** vs **systemctl**

최근 리눅스 버전에서는 init데몬 대신에 systemd데몬을 사용하여 프로세스를 관리

- `service`: init데몬 사용\
  사용법)
  - `service 서비스명 status`
  - `service 서비스명 start`
- `systemctl`: systemd데몬 사용
  사용법)
  - `systemctl status 서비스명`

### 🦋 LVM(Logical Volume Manager) 볼륨 사이즈 확장

---

## Ubuntu

설치 후, 업데이트 및 필요 패키지 설치

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

---

### 🦋 SSH 접속

- Lightsail
  1. 서버 아이피가 동일 하며, 서버를 다시 설치 했을 경우 ~/.ssh/known_hosts 를 제거
  2. `ssh -i pem파일경로 ubuntu@3.35.129.200`

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

### 🦋 background 실행 및 foreground, background 전환

background로 실행\
`명령어 &`: background 실행 - 끝에 `&`를 붙여줌

background로 전환

1. `ctrl z`: 중지 상태로 변경
2. `jobs`
3. `bg %[jobs의 task number]`\
   ex) `bg %2`

foreground로 전환

1. `jobs`
2. `fg %[jobs의 task number]`\
   ex) `fg %1`

### 🦋 재부팅 및 종료

재부팅: `sudo reboot` 또는 `sudo shutdown -r now`\
종료: `sudo shutdown -h now`

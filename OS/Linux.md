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

---

- FHS
- 프롬프트 단축기
- 파일검색
- 문자열검색
- 메타캐릭터&기술자
- 환경변수

---

## Ubuntu(22.04.1 live server amd64)

> 설치 시, 주의 사항

1. Profile setup
   Your name: 용도를 몰라 Your Pick a username와 동일하게 설정\
   Your server's name: 프롬프트의 유저명@{이부분}, 콤마와 언더바는 인식이 안됨\
   Your Pick a username: 프롬프트의 {이부분}@서버명
2. 추가적 설치는 불필요

<br />

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

> 설치 후, 재설치 방법

1. F2로 Bios 진입
2. 부팅 순서에서 CD를 최상위로 설정
3. 재부팅

---

<br />

## 여러 설정 및 명령어

### SSH 접속

- Lightsail
  1. 서버 아이피가 동일 하며, 서버를 다시 설치 했을 경우 ~/.ssh/known_hosts 를 제거
  2. `ssh -i pem파일경로 ubuntu@3.35.129.200`
  - Permissions 관련 에러가 발생 시, `chmod 400 pem파일`로 권한 변경 후, 재시도

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

<br />

### 재부팅 및 종료

재부팅: `sudo reboot` 또는 `sudo shutdown -r now`\
종료: `sudo shutdown -h now` 또는 `sudo poweroff`

<br />

### 부트로더 GNU GRUB 진입 방법

1. `sudo vim /etc/default/grub`
2. 아래와 같이 해당 값을 변경
   ```config
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

1. initd

2. systemd

<br />

### LVM(Logical Volume Manager) 볼륨 사이즈 확장

<br />

### 특정 (네트워크)포트 확인 및 종료

사용 중인 포트 확인

```shell
sudo lsof -i :8081
sudo kill -9 PID
```

<br />

네트워크 포트 확인

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

### 용량/메모리 확인

- `swapon -s`: swap 메모리 확인
- `df -h`
- `du -h`
  - -s: 디렉토리의 사용량만 표시

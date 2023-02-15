# Git - ETC

### 🦋 SSH Key gen 생성

`ssh-keygen -m PEM -t rsa -b 4096 -C answlgus1122@gmail.com`

- -f ~/.ssh/moonghub_rsa: 위치 및 파일 명 지정(rsa를 여러개 사용 시)
- 파일명을 임의 지정 시, 아래와 같은 설정이 필요
  1. config 파일 생성\
     **~/.ssh/config**
     ```conf
     # Git 계정 내꺼
     Host moonghub_rsa
       HostName github.com
       IdentityFile ~/.ssh/moonghub_rsa
     ```
  2. `eval $(ssh-agent -s)`
  3. `ssh-add ~/.ssh/moonghub_rsa`
  4. `ssh -T git@moonghub_rsa`

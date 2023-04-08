# GIT - ETC

### 🦋 SSH Key gen 생성

`ssh-keygen -m PEM -t rsa -b 4096 -C answlgus1122@gmail.com`

- -f ~/.ssh/moonghub_rsa: 위치(기본- ~/.ssh/) 및 파일 명 지정(rsa를 여러개 사용 시)
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

<br />

### 🦋 이슈 브랜치 자동 생성 및 삭제

1. robvanderleek/create-issue-branch 을 이용\
   Issue -> Create branch -> Create pr

   - 할당자와 label을 부여하여 이슈 생성
   - label만 부여해 이슈를 생성하고, 나중에 할당자를 부여

2. Settings > General > Automatically delete head branches 체크
3. 로컬에서 브랜치 동기화는 [참고](./Grammar.md#동기화)

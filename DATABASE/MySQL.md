# DATABASE - MySQL

- [기본 명령어](#기본-명령어)
  - [유저](#유저)
  - [데이터 베이스](#데이터-베이스)
    - [덤프](#덤프)
  - [테이블](#테이블)
- [Docker](#docker)
- [Advanced](#advanced)
  - [동시성](#동시성)
- [PBL](#pbl)
  - [전역 SQL 모드](#전역-sql-모드)

## 기본 명령어

- `mysql -u {유저명} -p [{DB명}]`: 패스워드 입력으로 mysql접속
- `SHOW VARIABLES LIKE '%VERSION%'`: 서버 버전 확인

### 유저

- 생성 및 권한 부여

  - `create user moong@localhost identified by 'moong';`
  - `grant all privileges on *.* to user@localhost;`
  - `grant all privileges on DB이름.* to user@localhost;`
  - `flush privileges;`

- 권한 표시

  - `show grants for moong@localhost;`
  - `show grants for current_user;`

- 비밀번호 변경
  - `alter user 'moong'@'localhost' identified with mysql_native_password by 'moong';`\

### 데이터 베이스

- `show databases;`
- `use database_name;`

#### 덤프

- `mysqldump -u {유저명} -p {DB명} > /root/dump/dump1.sql`: 덤프 추출
- `mysql -u {유저명} -p {DB명} < /root/dump/dump1.sql`: 덤프 복구

<br />

### 테이블

> 명명 규칙
>
> - 테이블: 소문자, 언더스코어, 복수형, 축약X, 능동형\
> - 칼럼: 접미어 활용, fk는 fk-부모테이블 등

- `show tables;`
- `desc table_name;`

---

## Docker

- `docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=1234 -v /Users/moon/Downloads/docker_backup:/root/docker_backup -d -p 3306:3306 mysql:latest`

---

## Advanced

### 동시성

#### 경합 방지

트랜잭션에서 `SELECT ... FOR UPDATE`를 사용하여 특정 행에 대해 배타적 잠금(X-Lock) 획득하고 `COMMIT`되거나 `ROLLBACK`되어 잠금을 해제할 때까지,
동일한 행을 수정하려는 다른 트랜잭션은 대기(Blocking)

---

## PBL

### 전역 SQL 모드

설정 조회: `SELECT @@GLOBAL.sql_mode;`
기본 설정: `ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION`

- `ONLY_FULL_GROUP_BY`: GROUP BY 구문을 사용할 때, SELECT 절에 포함된 모든 열은 반드시 GROUP BY에 포함되거나 집계 함수(SUM, COUNT, 등)에 포함되어야 함
- `STRICT_TRANS_TABLES`: 잘못된 데이터를 삽입할 경우 에러를 발생시키고 쿼리를 실패시킴 (엄격 모드)
- `NO_ZERO_IN_DATE`: _yyyy-00-00_, _yyyy-mm-00_ 같이 월/일이 0인 날짜 입력을 허용하지 않음
- `NO_ZERO_DATE`: _0000-00-00_ 같이 전체가 0인 날짜를 허용하지 않음
- `ERROR_FOR_DIVISION_BY_ZERO`: 0으로 나누기가 발생하면 에러를 발생
- `NO_ENGINE_SUBSTITUTION`: 테이블 생성 시 지정한 ENGINE이 사용 불가능하면, 대체 엔진으로 자동 전환하지 않고 에러 발생

**수정 필요시, 설정 파일을 마운트 - Docker**

1. 설정 파일 작성`(./{local_path}/mysql.cnf)`
   ```text
   [mysqld]
   sql_mode=NO_ENGINE_SUBSTITUTION
   ```
2. 볼륨 옵션으로 마운트
   `./{local_path}/mysql.cnf:/etc/mysql/conf.d/mysql.cnf:ro`

<br />

### Can't connect to local MySQL server through socket '/tmp/mysql.sock'

- `/opt/homebrew/Cellar/mysql/버전/bin/mysql_config --socket`: socket의 위치 확인
- `brew services list`: mysql의 status 확인
- `brew services start mysql`: 시작 시, **/tmp/mysql.sock** 파일이 생성 됨
  - 또는 `/opt/homebrew/Cellar/mysql/버전/bin/mysqld` 직접 실행

**Error: Failure while executing; `/bin/launchctl bootstrap gui/501 /Users/moong/Library/LaunchAgents/homebrew.mxcl.mysql@8.4.plist` exited with 5.**
**Invalid MySQL server downgrade: Cannot downgrade from**

1. `brew stop mysql@8.4`
2. `sudo rm -f /tmp/mysql.sock /tmp/mysqlx.sock`
3. `rm -rf /opt/homebrew/var/mysql`
4. `rm -rf /opt/homebrew/etc/my.cnf`
5. `sudo rm -f /Library/LaunchDaemons/homebrew.mxcl.mysql@8.4.plist`
6. `brew uninstall mysql@8.4`
7. `brew cleanup`
8. `sudo chown -R "$(whoami):admin" /opt/homebrew/`
9. `brew install mysql@8.4`
10. `brew services start mysql@8.4`
11. `ls /tmp/mysql.sock` 생성 확인

<br />

### DBeaver Access denied for user 'XXX@localhost' ...

`default-authentication-plugin`가 `mysql_native_password`로 설정 되어있으며, DBeaver에서 접속이 안될 경우,

- `sudo vim /opt/homebrew/etc/my.cnf`
- 아래 값으로 수정
  ```text
  bind-address = 0.0.0.0
  mysqlx-bind-address = 0.0.0.0
  ```
- ~~`brew services restart mysql@8.0`~~ `brew services stop mysql@8.0`
- `brew services list` 했을 때, Status 가 none 또는 stopped 이어야함

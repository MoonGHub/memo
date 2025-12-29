# DATABASE - MySQL

- [기본 명령어](#기본-명령어)
  - [유저](#유저)
  - [데이터 베이스](#데이터-베이스)
    - [덤프](#덤프)
  - [테이블](#테이블)
- [Docker](#docker)
- [Advanced](#advanced)
  - [동시성](#동시성)
    - [경합 방지](#경합-방지)
- [PBL](#pbl)
  - [전역 SQL 모드](#전역-sql-모드)
  - [[실행] unable to lock ./ibdata1 error](#실행-unable-to-lock-ibdata1-error)
  - [[덤프 복구] Can't connect to local MySQL server through socket '/tmp/mysql.sock'](#덤프-복구-cant-connect-to-local-mysql-server-through-socket-tmpmysqlsock)
    - [`--host`의 기본값은 `localhost` -> 호스트의 `/tmp/mysql.sock`를 통해 접속](#--host의-기본값은-localhost---호스트의-tmpmysqlsock를-통해-접속)
    - [또는 --protocol=TCP 옵션 지정](#또는---protocoltcp-옵션-지정)
  - [[DBeaver 접속] Access denied for user 'XXX@localhost' ...](#dbeaver-접속-access-denied-for-user-xxxlocalhost-)
    - [8.0](#80)
    - [8.4 >=](#84-)
  - [Plugin 'mysql_native_password' is not loaded (8.4 >)](#plugin-mysql_native_password-is-not-loaded-84-)
    - [DBeaver](#dbeaver)
    - [도커](#도커)
    - [8.0에서 업그레이드 시](#80에서-84--업그레이드-시)

---

## 기본 명령어

- `mysql -u {유저명} -p {DB명}`: 패스워드 입력으로 mysql접속
- `SHOW VARIABLES LIKE '%VERSION%'`: 서버 버전 확인

### 유저

- 로그인 가능 계정 정보
  - `SELECT user, host, plugin FROM mysql.user;`
    - host
      - `%`: 모든 호스트 허용 (wildcard)
      - `localhost`: 로컬 소켓에서만 허용
      - `127.0.0.1`: TCP 로컬만 허용
- 생성 및 권한 부여

  - `create user moong@localhost identified by 'moong';`
  - `grant all privileges on *.* to user@localhost;`
  - `grant all privileges on DB이름.* to user@localhost;`
  - `flush privileges;`

- 권한 표시
  - `show grants for moong@localhost;`
  - `show grants for current_user;`
- 비밀번호 변경
  - (8.0) `ALTER USER 'moong'@'localhost' IDENTIFIED WITH mysql_native_password BY 'moong';`
  - (8.4>=) `ALTER USER '계정'@'localhost' IDENTIFIED WITH caching_sha2_password BY '새비번';`
  - `flush privileges;`

### 데이터 베이스

- `show databases;`
- `use database_name;`

#### 덤프

추출

- `mysqldump -u {유저명} -p {DB명} > /root/dump/dump1.sql`: 덤프 추출

복구

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

### [실행] unable to lock ./ibdata1 error

아래 명령어 입력 후, mysql 재실행

- `killall -9 mysql`
- `killall -9 mysqld`
- `killall -9 mysqld_safe`

<br />

### [덤프 복구] Can't connect to local MySQL server through socket '/tmp/mysql.sock'

#### **`--host`의 기본값은 `localhost` -> 호스트의 `/tmp/mysql.sock`를 통해 접속**

- `/opt/homebrew/Cellar/mysql/버전/bin/mysql_config --socket`: socket의 위치 확인
- `brew services list`: mysql의 status 확인
- `brew services start mysql`: 시작 시, **/tmp/mysql.sock** 파일이 생성 됨
  - 또는 `/opt/homebrew/Cellar/mysql/버전/bin/mysqld` 직접 실행

**Error: Failure while executing; `/bin/launchctl bootstrap gui/501 /Users/moong/Library/LaunchAgents/homebrew.mxcl.mysql@8.4.plist` exited with 5.**
**Invalid MySQL server downgrade: Cannot downgrade from**

> MySQL은 downgrade를 지원하지 않음

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

#### **또는 --protocol=TCP 옵션 지정**

- Access denied 가 뜰 경우, root 유저로 시도

<br />

### [DBeaver 접속] Access denied for user 'XXX@localhost' ...

#### **8.0**

`default-authentication-plugin`가 `mysql_native_password`로 설정 되어있으며, DBeaver에서 접속이 안될 경우

- `sudo vim /opt/homebrew/etc/my.cnf`
- 아래 값으로 수정
  ```text
  bind-address = 0.0.0.0
  mysqlx-bind-address = 0.0.0.0
  ```
- ~~`brew services restart mysql@8.0`~~ `brew services stop mysql@8.0`
- `brew services list` 했을 때, Status 가 none 또는 stopped 이어야함(?)
- `ls /tmp/mysql.sock` 이 없어야 함(?)

#### **8.4 >=**

루트 계정에서 `SELECT user, host, plugin FROM mysql.user;`시에,
아래 처럼 host에 `localhost`가 없으면 접속 불가

```text
+------------------+-----------+-----------------------+
| user             | host      | plugin                |
+------------------+-----------+-----------------------+
| root             | %         | caching_sha2_password |
```

- `ALTER USER '계정'@'localhost' IDENTIFIED WITH caching_sha2_password BY '새비번';`
- `flush privileges;`

또는

- `--host=127.0.0.1`(Unix socket이 아닌 TCP 연결) 옵션 지정
- 또는 `--host=localhost --protocol=TCP`로 지정

<br />

### Plugin 'mysql_native_password' is not loaded (8.4 >)

> 기본 인증 플러그인이 `mysql_native_password`에서 `caching_sha2_password`로 변경됨

#### DBeaver

- 드라이버 속성 `defaultAuthenticationPlugin`을 `mysql_native_password`에서 `caching_sha2_password`로 변경

#### 도커

- `command: --default-authentication-plugin=mysql_native_password` 제거

#### 8.0에서 8.4 >= 업그레이드 시

1. **버전 업그레이드 전, 덤프 생성 필수**
2. 기존 컨테이너 제거
3. 새 버전으로 컨테이너 생성 후
4. 덤프 복구
   - 원격 툴 실행 시, `--host=localhost` 사용 불가, `--host=127.0.0.1`로 사용
   - 또는 원격 툴(DBeaver)에서 `Extra command args`에서 `--protocol=TCP`를 추가 지정 (`--host=localhost --protocol=TCP`)
   - 또는 호스트 터미널에서 `docker exec -i {컨테이너명} mysql -u {계정명} -p'{패스워드}' {데이터베이스명} < {덤프파일명}.sql`

# DATABASE - MySQL

## 유저

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

---

## 데이터 베이스

- `show databases;`
- `use database_name;`

## 테이블

> 명명 규칙
>
> - 테이블: 소문자, 언더스코어, 복수형, 축약X, 능동형\
> - 칼럼: 접미어 활용, fk는 fk-부모테이블 등

- `show tables;`
- `desc table_name;`

<br />

## 백업 및 불러들이기

### 백업

`...`

<br />

### 불러들이기

`mysql -uroot -p1234 testdb < /root/docker_backup/test.sql`

<br />

## Docker

`docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=1234 -v /Users/moon/Downloads/docker_backup:/root/docker_backup -d -p 3306:3306 mysql:latest`

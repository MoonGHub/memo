# Database - MySQL

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

- 음
  - 읍

## 테이블

- `show tables;`
- `desc table_name;`

- 음
  - 음

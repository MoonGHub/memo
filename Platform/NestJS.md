# Platform - Nest JS

- [Basic](#basic)
  - [어노테이션](#어노테이션)
- [TypeORM](#typeorm)
  - [Query Builder](#query-builder)
  - [Repository find 옵션](#repository-find-옵션)
  - [조건 연산자](#조건-연산자)

## Basic

...

## 어노테이션

- `@MessagePattern(topic)`: 메시지를 수신할 패턴 지정하며, 해당 키로 메세지 수신시 실행

---

## TypeORM

### Query Builder

- `Brackets`: `(... OR ...) AND ...`와 같은 복합 조건의 우선순위가 필요할 때 사용

### Repository find 옵션

- `Between`
- `Not`

### 조건 연산자

- `BETWEEN A AND B`: 시간 비교일 때, 동일 값도 포함함

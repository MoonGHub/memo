# DATABASE - NoSQL

| 종류              | 설명                                     | 예시 DB          |
| ----------------- | ---------------------------------------- | ---------------- |
| Key / Value DB    | 키(Key)에 해당하는 값(Value)만 저장      | Redis, DynamoDB  |
| Column Family DB  | 열(Column) 단위로 데이터 저장            | Cassandra, HBase |
| Document based DB | JSON 형태의 문서(Document)로 데이터 저장 | MongoDB          |
| Graph based DB    | 노드와 엣지로 구성된 그래프 구조         | Neo4j, ArangoDB  |

### PACELC란?

- P: Partition tolerance - 네트워크 분할 발생 시(네트워크 연결이 끊어져 통신이 불가능해지는 상황을 의미)
- A: Availability - 가용성 보장
- C: Consistency - 일관성 보장
- E: Else - 분할이 없는 정상 상태 시
- L: Latency - 지연 시간
- C: Consistency - 일관성

PACELC 기반 데이터베이스: `몽볼카피`

- `MongoDB`: PA/EC
- `VoltDB`
- `Cassandra`: PA/EL
- `PNUTS`

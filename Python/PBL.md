# Python - PBL

## 코루틴(coroutine)

> 협력형 멀티 태스킹 방식 - 지연되는 동안 다른 일을 함

### 제너레이터

- range

<br />

### 네이티브 코루틴(async/await 코루틴)

> asyncio.run()에 async 함수를 전달하여 사용

- asyncio
  - run
  - sleep
  - create_task\
    해당 작업을 비동기로 작업
  - gather\
    각 작업을 비동기로 작업

<br />

## 병렬처리와 동시성

연산과 같은 작업(CPU bound)에서는 스레드를 늘려 요청을 처리하여도 동일 프로세스이기 때문에 처리의 한계가 있음.\
때문에 프로세스를 늘려야 함(병렬처리)

> 워커 또는 작업 프로세스를 늘릴 경우, 무결성에 주의

그 외의 작업(I/O bound)에서는 비동기로, 또는 스레드를 늘려 작업

### I/O bound

- 입출력 작업
  - 디스크 작업
  - 디비 접근
  - 네트워크 통신 등

<br />

- threading
  - 스레드 방식
  - 순서 운영체제 의존
- asyncio
  - 협력형 멀티 태스킹 방식(지연되는 동안 다른 일을 함 - 동일 프로세스)
  - 단일 스레드
  - 순서 사용자 지정 가능
  - `asyncio.get_event_loop().run_in_executor`와 `concurrent.futures.ThreadPoolExecutor()`를 통해 멀티 스레드 구현

<br />

### CPU bound

- 연산 작업

<br />

- multiprocessing
  - 개별 프로세스로 병렬처리
  - 프로세스 간 통신을 위한(무결성) 여러 자료구조 제공

<br />

# JavaScript - Built In Object

## String

- `charAt`
- `indexOf`: 없으면 -1
- `lastIndexOf`: 없으면 -1
- `match`: 없으면 null
- `replace`
- `search`: 해당 인덱스 반환
- `slice`
- `substring`
- `substr`
- `split`
- `toLowercase`
- `toUpperCase`
- `length`
- `concat`: 원본 유지
- `charCodeAt`: 문자를 ascii코드 값으로 변환
- `trim`: 전후 공백 제거
- `repeat`: 반복시킴
- `includes`

---

## Number

- `toString(16)`: 16진수 문자열
- `parseInt(hex, 16).toString(2)`: hex(16진수 문자열) -> 10진수 -> 2진수 문자열
- `toFixed`: 지정한 소수점 자리까지 표현, 지정수 + 1 자리에서 반올림, 문자열 반환
- `isNaN`: Number 여부 판단, Not a Number

---

## Array

- `join`
- `reverse`
- `sort`: 기본 오름차순
- `slice`
- `splice(idx, num, data...)`: `idx`부터 `num`개를 삭제 후, `data...`를 삽입
- `concat`: 원본 유지
- `pop`
- `push`
- `shift`
- `unshift`: 앞에서 넣음
- `length`
- `find`
- `findIndex`
- `filter`
- `forEach`
- `indexOf`
- `lastIndexOf`
- `reverse`
- `map`
- `join`
- `isArray`
- `reduce`
- `some`
- `every`
- `at`

---

## Boolean

...

---

## Date

- `getDate`
- `toLocaleDateString`

---

## Math

- `abs`: 절대 값을 반환
- `max`
- `min`
- `pow`: 제곱, `**`연산자와 동일
- `random`: 0~1사이 무작위 생성
- `round`: 반올림
- `ceil`
- `floor`
- `sqrt`: 제곱근 값
- `PI`: 상수

---

## RegExp

temp.txt 1346 line 정리..

- `(?! ...)`: 부정형 전방 탐색, 특정 패턴이 앞에 오지 않는 경우에만 매칭

---

## Function

- `prototype`: 생성자 함수가 생성할 객체의 프로토타입 정의 - 상속
- `apply`

  > func.apply(thisArg, [argsArray])

  - `thisArg`: 함수 내부의 `this`에 바인딩할 객체
  - `argsArray`: 함수에 전달할 `argument`의 배열

  ```javascript
  function request(url, options, callback) {...}
  var requestArgs = ['http ..', {...}, function(){...}];

  request.apply(null, requestArgs);
  // request.(...requestArgs)와 동일

  Array.prototype.slice.apply(arguments);
  // arguments.slice()와 동일

  [].slice.apply(arguments);
  // arguments.slice()와 동일
  ```

- `call`

  > func.call(thisArg, ...arg);

  - apply()와 기능은 같지만 apply()의 두번째 인자에서 배열 형태로 넘긴 것을 각각 하나의 인자로 넘긴다.

  ```javascript
  Person.apply(foo, [1, 2, 3]);
  Person.call(foo, 1, 2, 3);
  ```

  ```javascript
  function MyClass() {
    SuperClass.call(this);
    OtherSuperClass.call(this);
  }
  ```

- bind

---

## XMLHttpRequest // xhr는 크로스 도메인 문제를 해결 못함?

.open("GET", url + data(GET방식일때, 인코딩해줌), 옵션...) // 요청 초기화, 비동기 디폴트
.setRequestHeader("Content-type", "application/x-www-form-urlencoded;charset-UTF-8")
.send(data) // 요청 보낼때 호출, 보낼 데이터가 없으면 파라미터 생략

---

.onreadystatechange // 이벤트, readyState변경 시 발생
.onload // 이벤트, 응답 완료시 발생

---

.readyState // onload이벤트 사용시 불필요
0: open호출 전(UNINITIALIZED)
1: send호출 전(LOADING)
2: 처리 중(LOADED)
3: 부분적으로 응답(INTERACTIVE)
4: 응답 완료(COMPLETED)
.responseText // 응답받은 데이터의 참조 속성
.responseXML
.status

---

## JSON

- parse(str)

---

## Object

- propertyIsEnumerable(att) // 해당 속성이 존재하며 for/in으로 열거가능판단 false or true
- assign(target, ...sources)\
  첫 인수의 객체로 합쳐서(덮어씌움), 첫 인수를 반환
- keys(obj) // [] 반환
- values(obj) // [] 반환
- entries(obj) // [[]] 반환
- fromEntries(arr)
- defineProperty

  ```javascript
  function withValue(value) {
    var d =
      withValue.d ||
      (withValue.d = {
        enumerable: false,
        writable: false,
        configurable: false,
        value: null,
      });
    d.value = value;

    return d;
  }

  Object.defineProperty(obj, "key", withValue("static"));
  ```

  - enumerable\
    열거(for...in 또는 Object.keys 등)
  - configurable\
    설정
  - writable\
    변경
  - value
  - get\
    함수의 리턴 값으로 value를 대신하여 해당 key값을 반환
  - set

- create
- freeze

---

## 기본 제공 함수

- encodeURI('?query=값') // 유니코드로 인코딩, 영숫자 및 일부문자 제외
- encodeURIComponent('?query=값') // 영숫자만 제외, GET방식에 사용(form은 기본구현되있음)
- decodeURI('?query=%EA%B0%92')
- decodeURIComponent('?query=%EA%B0%92')
- parseInt('5.12')
- parseInt('5px') // 숫자로 시작해 첫 문자까지
- parseFloat('13.2%')
- String(123)
- Number('123')
- Boolean(1)
- isNaN('a') // is not a number, 문자존재 시 false
- eval('1+2') // 문자열을 코드로 처리, JSON은 JSON.parse를 사용하자
- JSON.parse('{"name":"man", "age":"12"}')

---

## [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)

> [server sent events(SSE)](../Python/FastApi.md#sseserver-sent-events)와 같이 사용

```javascript
// example

const eventSource = new EventSource(`http://localhost:8000`, {
  // withCredentials: true,
});

eventSource.addEventListener("message", (event) => {
  console.log(event.data);
});

eventSource.addEventListener("open", (event) => {});

eventSource.addEventListener("error", (error) => {
  console.error("SSE Error:", error);

  if (error.readyState == EventSource.CLOSED) {
    // Connection was closed.
  } else {
    eventSource.close();
  }
});

eventSource.addEventListener("Custom Event", (event) => {});
```

- addEventListener 이벤트
  - error
  - message
  - open

---

## [WebSocket](https://developer.mozilla.org/ko/docs/Web/API/WebSocket)

> [FastApi 참고](../Python/FastApi.md#websocket)

```javascript
// example

const ws = new WebSocket("ws://localhost:8000/ws");

ws.addEventListener("message", (event) => {
  console.log(event.data);
});
```

- addEventListener 이벤트
  - close
  - error
  - message
  - open

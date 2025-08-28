# JavaScript - Built In Object

- [Object](#object)
  - [defineProperty](#defineproperty)
- [String](#string)
- [Number](#number)
- [Array](#array)
- [Boolean](#boolean)
- [JSON](#json)
- [Date](#date)
- [Math](#math)
- [RegExp](#regexp)
  - [패턴](#패턴)
  - [String에서 패턴 찾기](#string에서-패턴-찾기)
- [Function](#function)
- [Intl](#intl)
- [XMLHttpRequest](#xmlhttprequest)
- [EventSource](#eventsource)
- [WebSocket](#websocket)
- [Built in Function](#built-in-function)

## Object

- `propertyIsEnumerable`: 해당 속성이 존재하며 for/in으로 열거 가능 여부
- `assign`
- `keys`
- `values`
- `entries`
- `fromEntries`
- `defineProperty`
- `create`
- `freeze`

### defineProperty

```javascript
let obj1 = {};
let obj2 = {};

function withValue(value) {
  const config =
    withValue.config ||
    (withValue.config = {
      enumerable: true, // for...in 또는 Object.keys 등 열거 가능 여부
      writable: false, // 변경 가능 여부
      configurable: false, // 설정 가능 여부
      value: null, // 실제 값
      // get: value를 대신 반환
      // set
    });

  return { ...config, value };
}

Object.defineProperty(obj1, "a", withValue("hello"));
Object.defineProperty(obj2, "b", withValue("world"));

console.log(obj1, obj2, withValue.config);
```

---

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
- `sort`: 기본 오름차순, `(a, b) => a-b` - 오름차순, `(a, b) => 0.5 - Math.random()` - 랜덤 배치
- `slice`
- `splice(idx, num, data...)`: `idx`부터 `num`개를 삭제 후, `data...`를 삽입, 삭제한 배열 반환
- `concat`: 원본 유지
- `pop`
- `push`
- `shift`
- `unshift`: 배열 첫 요소에 추가
- `length`
- `find`
- `findIndex`
- `filter`
- `forEach`
- `indexOf`
- `lastIndexOf`
- `map`
- `isArray`
- `reduce`
- `some`
- `every`
- `at`

---

## Boolean

...

---

## JSON

- `parse`

---

## Date

- `getDate`
- `new Date`
  - `new Date('2025-07-03')`: 설정 시간이 UTC 타임존으로 적용 => UTC는 '2025-07-03T00:00:00.000Z'
  - `new Date('2025-08-02T07:10:34.086021')`: 설정 시간이 로컬 타임존으로 적용 => UTC는 '2025-08-01T22:10:34.086Z'
  - `new Date('2025-08-02T07:10:34.086021Z')`: 설정 시간이 UTC 타임존으로 적용 => KST는 '2025. 8. 2. 오후 4:10:34'
- `toLocaleDateString`
  - 디폴트 타임존은 로컬 타임존
  - `new Date('2025-08-02').toLocaleString('en-US', { timeZone: 'UTC', hour12: false })`: '8/2/2025, 00:00:00'
  - `new Date('2025-08-02').toLocaleString('en-US', { timeZone: undefined, hour12: false })`: '8/2/2025, 09:00:00'

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
- `PI`: 파이 상수

---

## RegExp

> `new RegExp("패턴", "플래그");`

- `test`: true or false
- `exec`: 일치 문자열 반환

### 패턴

- `*`: 0개 이상
- `+`: 1개 이상
- `?`: 0개 또는 1개
- `\w`: 모든 문자
- `\W`: 대소문자,숫자 \_를 제외한 모든 문자
- `\d`: 숫자
- `\D`: 숫자를 제외한 모든 문자
- `\s`: 공백 문자(공백, 탭, 줄바꿈 등)
- `\S`: 공백 문자를 제외한 모든 문자
- `p{n}`: p가 n개인 문자열
- `[0-9]`: 0~9중의 하나
- `[a-z]`: a~z중 하나
- `[qwer]`: qwer 문자중 하나
- `[^abc]`: a 또는 b 또는 c가 아닌 문자
- `(qwer)`: "qwer" 연속 문자열
- `(a|b)`: a 또는 b
- `{m, n}`: m회 이상 n회 이하

**전방탐색**

- `(?=정규식)`: 정규식에는 매칭 조건에는 넣고 싶지만 리턴받고 싶지 않은 정규식
- `(?!정규식)`: 부정형 전방 탐색, 특정 패턴이 앞에 오지 않는 경우에만 매칭

**후방탐색**

- `(?<=정규식)`
- `(?<!정규식)`: 부정형

### String에서 패턴 찾기

- `str.search()`: 인덱스 반환
- `str.replace()`
- `str.match()`: 일치 문자열 반환(여러개면 배열로)

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

  `Math.max.apply(null,[3,4,5])`

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

- `bind`: this 바인딩

---

## Intl

Internationalization: 국제화

```javascript
const dateFormat = new Intl.DateTimeFormat("ko", {
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
});

console.log(dateFormat.format(new Date()));
```

---

## XMLHttpRequest

> `new XMLHttpRequest();`로 생성하여 사용하며, 기본적으로 비동기

- `open(method, url)`
  - method: `GET`, `POST`, `PUT`, `DELETE`
- `setRequestHeader`
- `send`: 요청 호출
- `onreadystatechange`: readyState변경 시 발생
  - readyState
    - `0`: `UNSENT` - open 호출 전
    - `1`: `OPENED` - send 호출 전 => open
    - `2`: `HEADERS_RECEIVED` - 처리 중
    - `3`: `LOADING` - 부분적으로 응답 => onprogress
    - `4`: `DONE` - 응답 완료 => onload
- `response`: responseType에 자동 파싱
- `responseText`: 응답 데이터를 문자열 형태로 반환
- `responseXML`: 응답 데이터를 DOM 형태로 파싱하여 반환
- `status`: 응답 상태 값

예제

```javascript
const xhr = new XMLHttpRequest();

xhr.open("GET", "./sample.html");
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    console.log(xhr.responseText);

    document.body.innerHTML = xhr.responseText;
  }
};

xhr.send();
```

---

## [EventSource](https://developer.mozilla.org/en-US/docs/Web/API/EventSource)

> [server sent events(SSE)](../Python/FastApi.md#sseserver-sent-events)와 같이 사용

기본 이벤트

- open
- message
- error

```javascript
const eventSource = new EventSource(`http://localhost:8000`);

eventSource.addEventListener("open", (event) => {
  console.log("open :: ", event);
});

eventSource.addEventListener("message", (event) => {
  console.log("message :: ", event.data);
});

eventSource.addEventListener("error", (error) => {
  console.error("error :: ", error);

  if (error.readyState == EventSource.CLOSED) {
    // Connection was closed.
  } else {
    eventSource.close();
  }
});

eventSource.addEventListener("Custom Event", (event) => {});
```

---

## [WebSocket](https://developer.mozilla.org/ko/docs/Web/API/WebSocket)

> [FastApi 참고](../Python/FastApi.md#websocket)

기본 이벤트

- open
- message
- close
- error

```javascript
const ws = new WebSocket("ws://localhost:8000/ws");

ws.addEventListener("message", (event) => {
  console.log("message :: ", event.data);
});
```

---

## Built in Function

- `encodeURI`: 유니코드로 인코딩, 영숫자 및 일부문자 제외
- `encodeURIComponent`: 영숫자만 제외, rest GET방식에 사용(form은 기본구현)
- `decodeURI`
- `decodeURIComponent`
- `parseInt`: 숫자로 시작해 첫 문자까지 전까지 파싱
- `parseFloat`
- `String`
- `Number`
- `Boolean`
- `isNaN`: is Not a Number
- `eval`: 문자열을 코드로 처리
- `isFinite`: 유한수 여부
- `escape`: 16진수 아스키코드로 변환
- `unescape`: ISO-Latin-1로 변환

# JavaScript - Built In Object

## Math

- abs(num)
- max(num, ...)
- min(num, ...)
- pow(num, 제곱값)
- random() // 0~1사이 무작위 생성
- round(num) // 소숫점 한자리에서
- ceil(num)
  - .floor(num)
  - .sqrt(num) // 제곱근값
- PI

<br />

## Array

- join(delimiter)
- reverse()
- sort() // 오름차순
- slice(index1, index2) // index1앞까지, index2(포함)~끝 자름
- splice(index1, num, data, ...) // index1부터 num개를 삭제 후, data삽입
- concat(arr2) // 배열 합침
- pop()
- push(date)
- shift()
- unshift(data) // 앞에서 넣음
- length
- find(func) // 순회하며 true인 첫 번째 요소 반환
- findIndex(func)
- filter(func) // true인 요소 배열로 반환
- forEach((item, index)=>{...})
- indexOf(data)
- lastIndexOf(data)
- reverse() // 역순 정렬
- map((item, index)=>{...}) // 각 요소의 return값으로 배열 반환
- join(str)
- isArray(arr)
- reduce((acc, cur, index)=>{...})

<br />

## String

- charAt(index)
- indexOf(str2) // 없으면 -1
- lastIndexOf(str2) // 없으면 -1
- match(str2) // 없으면 null
- replace(target, str2)
- search(str2) // index반환
- slice(index1, index2) // index1앞까지, index2(포함)~끝을 자름
- / -1은 뒤에서 첫 번째 글자
- substring(index1, index2) // index1부터 index2이전
- substr(index, num) // index부터 num개의 문자 반환
- split(delimiter) // 배열반환
- toLowercase()
- toUpperCase()
- length
- concat(str2)
- charCodeAt(index) // index의 문자를 ascii코드 값으로 변환
- trim() // str의 전후 공백만 제거
- repeat(n) // n번 반복시킴
- includes(str)

<br />

## Number

- toString(16) // 16진수 문자열
- parseInt(hex, 16).toString(2) // 16진수 문자열 -> 10진수 -> 2진수 문자열
- toFixed(num) // 소수점 num자리까지 표현(num+1자리에서 반올림 됨)해 문자열로 반환
- isNaN(obj) // obj가 Number인지 판단

<br />

## Boolean

<br />

## RegExp

temp.txt 1346 line 정리..

- `(?! ...)`: 부정형 전방 탐색, 특정 패턴이 앞에 오지 않는 경우에만 매칭

<br />

## Date

- getDate()
- toLocaleDateString()

<br />

## Function

- prototype // 부모(상속) 지정
- apply

  > func.apply(thisArg, [argsArray])

  - thisArg: 함수 내부의 this에 바인딩할 객체
  - argsArray: 함수에 전달할 argument의 배열

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

- call

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

<br />

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

<br />

## JSON

- parse(str)

<br />

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

<br />

## Array

- some
- every
- at

<br />

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

<br />

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

<br />

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

# JavaScript - Object

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

## RegExp

- test(str) // true or false

## Date

- getDate()
- toLocaleDateString()

## Function

- prototype // 부모(상속) 지정

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

## JSON

- parse(str)

## Object

- propertyIsEnumerable(att) // 해당 속성이 존재하며 for/in으로 열거가능판단 false or true
- assign(obj...) // 첫 인수의 객체로 합쳐서, 첫 인수를 반환
- keys(obj) // [] 반환
- values(obj) // [] 반환
- entries(obj) // [[]] 반환
- fromEntries(arr)
- defineProperty

## Function

.call(thisArg[, arg1[, arg2[, ...]]])
// this 객체가 기존 함수를 호출할 때 할당될 수 있습니다, - 객체의 생성자 연결에 call 사용,

## Array

- Array.prototype.some
- Array.prototype.every

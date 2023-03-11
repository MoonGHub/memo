# JavaScript - ETC

### 🦋 이벤트 전파

캡처 -> 타깃 -> 버블링
캡처 : window에서 대상 요소까지
타켓 : 대상 요소에 도착한 대상 단계
버블링 : 대상요소에서 이벤트 캡처 후 상위요소로 이벤트 전파

<br />

### 🦋 DOM 요소 탐색의 반환 값들

#### HTMLCollection

getElementsByTagName
(인덱스접근이지만 배열이 아님)

#### NodeList

getElementsByClassName
querySelector() ..?
querySelectorAll() ..?

<br />

### 🦋 this의 context scope

function의 this는 전역this

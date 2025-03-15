# JavaScript - DOM

## document

### 문서 영역

- body
- cookie
- scrollHeight\
  문서의 실제 크기반환
- scrollWidth
- lastModified
- documentElement\
  문서 전체

<br />

### 요소 선택

- [form name]
- forms
- forms[index 또는 form name][input name]
- anchors
- layers
- images

<Br />

### 요소 조작

- createElement
- createTextNode
- write

<br />

## element

### 요소 정보

- id
- tagName
- nodeName
- nodeValue
- textContent
  - XSS방지
  - 주석, script, style도 포함됨
- nodeType
  - Node.ELEMENT_NODE -> 1
- style
  - width
  - backgroundColor
- classList
  - add
  - remove
  - toggle
  - contains
- getAttribute
- setAttribute
- hasAttribute
- removeAttribute

<br />

### 요소 선택

- querySelector
- querySelectorAll
- getElementById
- getElementsByTagName
- getElementsByClassName
- firstChild
- lastChild
- nextSibling\
   같은 레벨의 다음 노드
- previousSibling
- previousElementSibling
- childNodes
- parentNode
- offsetParent\
   static이 아닌 가장 가까운 부모요소
- outerHTML

<br />

### 요소 제어 및 조작

- [addEvenetListener](#addevenetlistener)
- removeEventListener
- append\
   태그 노드만 삽입 가능
- appendChild\
   태그 노드와 문자 노드 삽입 가능
- [insertAdjacentHTML](#insertAdjacentHTML)
- insertAdjacentElement
- insertAdjacentText
- removeChild
- [insertBefore](#insertbefore)
- replaceChild
- contains\
   자신을 포함하여 검색?
- hasChildNodes
- innerHTML\
   HTML파싱으로 속도가 떨어짐
- innerText\
   주석, script, style은 제외됨
- cloneNode
  - 파라미터로 Boolean을 받음
  - true: 해당 노드의 children까지 복제

<br />

### 요소 위치 및 크기

- clientHeight\
   요소 내부높이(border, 스크롤 제외)
- clientWidth
- scrollHeight\
   스크롤 이동 길이(뷰포트에서 사라진 요소 높이)
- offsetHeight\
   요소의 높이(border, 스크롤 포함)
- offsetWidth
- offsetTop\
   스크롤 이동 길이를 포함한 요소 위치
- offsetLeft
- getBoundingClientRect\

<br />

## Node

### textNode

- data
- appendData(data)
- deleteData(시작인덱스, 갯수)
- insertData(시작인덱스, data)
- replaceData(시작, 갯수, data)
- substringData(시작, 갯수)

<br />

---

## 요소들

### form

- reset
- submit
- checkValidity

<br />

---

## Function

### addEvenetListener

> addEvenetListener(eventType, handler, option...)

- eventType
  - mouseover
  - contextmenu\
    우클릭 메뉴
- handler
  > handler(event) {...}
  - event
    - type
    - stopPropagation
    - preventDefault
    - currentTarget\
       이벤트를 단 타겟
    - target\
       실제 타겟
    - altKey
    - ctrlKey
    - shiftKey
    - 마우스 이벤트(type - click)
      - clientX\
        뷰포트 기준의 마우스 좌표
      - clientY
      - pageX\
        문서 전체 기준의 마우스 좌표(스크롤 포함)
      - pageY
    - 키보드 이벤트(type - keydown)
      - key
        - "KeyD"
        - "Space"
        - "ArrowRight" 등
      - keyCode\
         아스키 코드

<br />

### insertBefore

> insertBefore(.., ..)

```javascript

```

<br />

### insertAdjacentHTML

> insertAdjacentHTML(option, ele)

- option
  - beforebegin
  - afterbegin
  - beforeend
  - afterend

```javascript

```

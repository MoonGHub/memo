# JavaScript - DOM

- [Document](#document)
- [Element](#element)
- [기타](#기타)

## Document

### 문서 영역

- `body`
- `cookie`
- `scrollHeight`: 문서의 실제 크기
- `scrollWidth`
- `lastModified`
- `documentElement`

### 요소 선택

- `[form name]`
- `forms`
- `forms[index 또는 form name][input name]`
- `anchors`
- `layers`
- `images`

### 노드 제어

- `createElement`
- `createTextNode`
- `write`

---

## Element

- `노드 종류`: ELEMENT_NODE(요소), TEXT_NODE(텍스트), COMMENT_NODE(주석) 등
- `NodeList`: 경우에 따라, 라이브 콜렉션 - DOM의 변경 사항을 실시간으로 콜렉션에 반영
- `HTMLCollection`: HTML 요소만 포함하며 항상 동적 - 문서가 바뀔 때 실시간으로 업데이트됨

### 요소 정보

- `id`
- `tagName`
- `nodeName`
- `nodeValue`
- `textContent`
  - XSS방지
  - 주석, script, style 등도 포함
- `nodeType`
  - Node.ELEMENT_NODE === 1
- `style`
- `classList`
  - `add`
  - `remove`
  - `toggle`
  - `contains`
- `getAttribute`
- `setAttribute`, `removeAttribute`
- `hasAttribute`

위치 및 크기

- `clientHeight`: 요소 내부높이(border, 스크롤 제외)
- `clientWidth`
- `scrollHeight`: 스크롤 이동 길이(뷰포트에서 사라진 요소 높이)
- `offsetHeight`: 요소의 높이(border, 스크롤 포함)
- `offsetWidth`
- `offsetTop`: 스크롤 이동 길이를 포함한 요소 위치
- `offsetLeft`
- `getBoundingClientRect`

### 요소 선택

- `querySelector`
- `querySelectorAll`
- `getElementById`
- `getElementsByTagName`
- `getElementsByClassName`
- `firstChild`
- `firstElementChild`
- `lastChild`
- `lastElementChild`
- `nextSibling`: 같은 레벨의 다음 노드
- `nextElementSibling`: 같은 레벨의 다음 요소 노드
- `previousSibling`
- `previousElementSibling`
- `childNodes`
- `parentNode`
- `offsetParent`: `position: static;`이 아닌 가장 가까운 부모요소 - 기준 좌표의 요소
- `outerHTML`

### 요소 제어

- `addEvenetListener`, `removeEventListener`
- `append`: 요소 노드만 삽입 가능
- `appendChild`: 모든 노드 삽입 가능
- `insertAdjacentHTML`
- `insertAdjacentElement`
- `insertAdjacentText`
- `removeChild`
- `insertBefore`
- `replaceChild`
- `contains`: 자신을 포함하여 검색?
- `hasChildNodes`
- `innerHTML`: HTML파싱으로 속도가 떨어짐
- `innerText`: 주석, script, style은 제외됨
- `cloneNode(boolen)`
  - `true`: 해당 노드의 children까지 복제

---

## 기타

### addEventListener listener의 `Event`

> 캡처 -> 타깃 -> 버블링

- `캡처`: window에서 대상 요소까지
- `타켓`: 이벤트 대상 요소
- `버블링`: 대상 요소에서 상위요소로 이벤트 전파

#### MouseEvent

- `clientX`: 뷰포트 기준의 마우스 좌표
- `clientY`
- `pageX`: 문서 전체 기준의 마우스 좌표(스크롤 포함)
- `pageY`

#### KeyboardEvent

- `altKey`
- `ctrlKey`
- `shiftKey`
- `key`
  - "KeyD"
  - "Space"
  - "ArrowRight"
  - 등
- `keyCode`: 아스키 코드

### insertAdjacentHTML(position, text)

- `position`
  - `beforebegin`: 요소 이전
  - `afterbegin`: 요소안 첫번째
  - `beforeend`: 요소안 마지막
  - `afterend`: 요소 다음
- `text`: HTML 혹은 XML로 파싱되고 트리에 삽입되는 문자열

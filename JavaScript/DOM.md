document
.getElementById(tagId)
.getElementsByTagName(tagName)
.querySelector(tagName)
.querySelectorAll(tagName)
.
문서영역조작
.body
.scrollHeight // 문서의 실제 크기반환
.scrollWidth
.cookie // 쿠키 값은 인코딩을 해주자, 문자열로 저장됨,
.forms

- forms[index] 또는 document[form name]
- document[form name][input name]
- forms[form name] .... ?

element
.style
.backgroundColor
.
.
.setAttribute(att, val)
.addEvenetListener(event, handler, option...)
element.addEventListener('mouseover', function(){
// ...1회용 코드
this.removeEventListener('mouseover', arguments.callee);
});
.removeEventListener(event, handler, option...)
.
노드선택자
.firstChild
.lastChild
.nextSibling // 같은 depth의 아래노드
.previousSibling
.childNodes[num]
.parentNode
요소제어
.append // 무조건 엘리먼트만 가능
.appendChild(ele) //문자 노드 삽입 가능
.
.
.
요소조작
.clientHeight // 요소 내부높이(border, 스크롤 제외)
.clientWidth
.offsetHeight // 요소의 높이(border, 스크롤 포함)
.offsetWidth
.offsetTop // 요소 위치
.offsetLeft
.nodeValue

--------------------------<태그 속성>
on~
click
submit
keypress
mousedown
mousemove
mouseup
mouseenter
mouseleave

draggable
"true" or "false"

<a>
    href=
        "#"     // 문서 상위로 스크롤 이동

<form>
    action

<input>
    type
        "submit"
        "text"
        "button"
        "checkbox"
        "radio"
    checked
        "checked"
    disabled
        "true" or "false"
    maxlength

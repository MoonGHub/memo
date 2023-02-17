#id
.classname

[type]
[type=value]
[type^=vaule] // 속성값이 value로 시작
[type$=value] // 속성값이 value로 끝
[type~=value] // 속성값 중에 value가 존재(완전일치)
[type*=value] // 속성값 중에 value를 포함하는 문자열을 가진 요소
[type!=value] // 불일치 요소

:nth-child(n) // n번째 자식요소
:nth-child(2n) // 짝수 번째 자식요소 모두, 2n -> even, 2n+1 -> odd
:first-child // 모두
:nth-last-child(n) // 뒤에서 시작하는 nth-child
:last-child // 모두
:nth-of-type(n) // 지정한 요소 전체 중에 n번째로 발견된 요소
:first-of-type // nth-of-type(1) 와 동일
:nth-last-of-type(n)
:last-of-type // nth-last-of-type(1)와 동일
:contains(str) // 텍스트 노드에 str문자열을 포함하는 요소
:only-child // 형제노드가 없는 요소
:empty // 하위노드가 없는 요소
:not

선택자
body div // space : 하위 모든 요소
div > span // > : 자식 노드(바로아래)의 모든요소
div + span // + : 다음 형제노드(nextSibling)
div ~ p // ~ : div이후에 있는 모든 형제요소 p

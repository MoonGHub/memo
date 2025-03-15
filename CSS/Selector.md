# CSS - Selector

### 🦋 결합자(Combinator)

`body div`: 하위 모든 div\
`div > span`: 자식 노드(바로아래)의 모든요소\
`div + span`: 다음 형제노드(nextSibling)\
`div ~ p`: div이후에 있는 모든 형제요소 p

<br />

### 🦋 속성(Attribute)

`[type]`\
`[type=value]`\
`[type^=vaule]`: 속성값이 value로 시작\
`[type$=value]`: 속성값이 value로 끝\
`[type~=value]`: 속성값 중에 value가 존재(완전일치)\
`[type*=value]`: 속성값 중에 value를 포함하는 문자열을 가진 요소\
`[type!=value]`: 불일치 요소

<br />

### 🦋 의사 클래스(Pseudo classes)

[참고](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes)

#### **:**

> 동적이거나 유동적이면서 어떤 요소의 전체에 영향을 줄 때 사용

`:nth-child(n)`: n번째 자식요소\
`:nth-child(2n)`: 짝수 번째 자식요소(2n -> even)

- `:nth-child(odd)`: 홀수 번째 자식요소(odd 또는 2n+1)
- `:nth-child(even)`: 짝수 번째 자식요소(even 또는 2n)

`:first-child`: 해당 요소가 부모 아래의 첫 번째 요소인 경우 해당\
`:first-of-type`: nth-of-type(1) 와 동일\
`:nth-of-type(n)`: 지정한 요소 전체 중에 n번째로 발견된 요소

`:last-child`: 해당 요소가 부모 아래의 마지막 요소인 경우 해당\
`:last-of-type`: nth-last-of-type(1)와 동일\
`:nth-last-of-type(n)`\
`:nth-last-child(n)`: 뒤에서 시작하는 nth-child ...?

`:contains(str)`: 텍스트 노드에 str문자열을 포함하는 요소\
`:only-child`: 형제노드가 없는 요소\
`:empty`: 하위노드가 없는 요소\
`:not`

`:disabled`\
`:enabled`

#### **::**

> 정적이면서 어떤 요소의 일부분에 영향을 줄 때 사용

`::after`\
`::before`

`::first-letter`: 첫 글자\
`::first-line`: 첫 라인

`::selection`: 드래그(선택) 시

<br />

## 미디어 쿼리

[참고](https://developer.mozilla.org/ko/docs/Web/CSS/Media_Queries/Using_media_queries#%EB%AF%B8%EB%94%94%EC%96%B4_%ED%8A%B9%EC%84%B1)

### HTML요소에 사용

```html
<link
  href="css/~.css"
  rel="stylesheet"
  type="text/css"
  media="screen and (min-width:321px) and (max-width:768px)"
/>
```

### CSS내에 사용

@import사용

```scss
@import url("css/~.css") screen and (min-width: 321px) and (max-width: 768px);
```

태그 사용

```scss
@media 미디어유형 | 미디어특성 | 미디어기능 [논리 연산자 미디어유형 | 미디어특성 | 미디어기능 ...] {
  // ...;
}

// ex)
@media screen and (max-width: 960px) {
  //...;
}

@media all and (device-width: 320px) and (device-height: 480px) {
  // ...;
}

@media all and (orientation: portrait) {
  // ...;
}

@media all and (aspect-ratio: 16/9) {
  // ...;
}
```

- 미디어유형
  - all
  - print
  - screen
  - speech
- 미디어 특성 예시
  - (orientation: landscape)
  - (prefers-color-scheme: dark)
- 미디어 기능 예시
  - (hover: hover)\
    모바일에서의 hover 제한
  - (prefers-reduced-motion: no-preference)\
    동작 모드
  - (prefers-reduced-motion: reduce)\
    동작 줄이기 모드
  - (max-width: 12450px)
- 논리 연산자
  - and
  - not
  - only
  - ,(쉼표)

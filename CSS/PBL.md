# CSS - PBL

`<link rel="stylesheet" type="text/css" href="sample />`

CSS 라이브러리 참고 사이트

- https://bennettfeely.com/
- https://www.cssscript.com/

<br />

## 크기

### 화면

뷰포트: 실제 내용이 표시되는 영역

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<!-- 뷰포트의 가로너비 = 단말기 가로너비 -->
```

<br />

### 요소

- 인라인 방식은 width와 height 값을 무시함
- `box-sizing: border-box;`\
  width 및 height 크기가 border크기를 포함하게 됨(디폴트: content-box;)

<br />

## 레이아웃

[참고](https://d2.naver.com/helloworld/6807203)

라이브러리

- http://gridstackjs.com/
- https://masonry.desandro.com/

<br />

### Flex

참고

- https://codepen.io/enxaneta/pen/adLPwv
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/

#### 정렬

- `flex-wrap: wrap;`\
  부모 크기 오버시 아래에 정렬

<br />

#### Flex내의 `flex: 1;`인 자식 요소가 부모에 맞춰 크기 줄어들게 하기

부모가 `flex-direction: row;`이며, 자식이 `flex: 1;`인 상황에서 가로 크기를 부모에 맞춰 줄어들게 할 때,\
자식요소에 `min-width: 0px;` 지정 필요

<br />

### Table

- `table-layout: fixed;`\
  테이블의 내부 요소가 커져도 th 및 td 크기를 고정 시킴

<br />

## 배경

### 영상

- 백그라운드 재생: tubular.js

<br />

## 이미지

### Background

- `background-clip: border-box;`\
  이미지의 영역이 border까지 확장됨

<br />

### SVG

[참고](https://svgontheweb.com/ko/)

- 요소 크기를 부모 크기에 맞추기(비율 유지 제거)\
  해당 파일 태그 내의 preserveAspectRatio값을 `preserveAspectRatio='none'`으로 변경

- 색 변경
  1. 해당 파일 태그 내의 fill값을 `fill="currentColor"`로 변경
  2. 구현 부의 style속성에 `{color :’red’}`와 같이 전달

#### 아이콘 사이트

- http://fontello.com/
- https://thenounproject.com/

<br />

## 텍스트

### 생략 표시(텍스트 길이가 부모요소보다 커질 경우)

```css
overflow: hidden;
text-overflow: ellipsis;
white-space: nowrap;

/* 라인 제한 */
/* white-space: pre-line; */
display: -webkit-box;
-webkit-box-orient: vertical;
-webkit-line-clamp: 3;
```

- 부모 요소의 길이가 정해져 있어야함
  - 길이 지정 또는 부모 요소에 `display: grid`(, `grid-auto-flow: column`)
  - table
    - td또는 td내 부모 요소에 `display: grid`(, `grid-auto-flow: column`)
    - td에 `max-width: 0`
      - 부모요소가 있을 경우 부모요소에 `display: flex`

<br />

### 그라디언트 효과

```css
background-image: linear-gradient(to right, #7dd3fc, #4f46e5);
background-clip: text;
color: transparent;
```

<br />

### EM

부모 요소의 px크기 = 자식 요소의 1em

<br />

## 마우스

### 스크롤

- 자동 포커싱

  ```css
  // 부모 요소
  overflow-y: auto;
  scroll-snap-type: y mandatory;

  // 자식 요소
  scroll-snap-align: start;
  ```

- 화면 내 부드러운 이동\
  `scroll-behavior: smooth;`

<br />

### 스크롤 적용

- flex내 요소가 스크롤인 경우

  ```css
  // 스크롤 대상 요소
  flex: auto;
  height: 0;
  overflow: auto;
  ```

- flex요소 내 `상위 - 중간 - 하위`구조에서 하위 요소가 스크롤인 경우

  ```css
  // 상위
  flex: auto;
  height: 0;

  // 중간
  display: flex;
  height: 100%; // 또는 flex: 1;
  overflow: hidden;
  // 방향은 상관 없음

  // 스크롤 대상 하위 요소에
  flex: 1 1 0;
  overflow-y: auto;
  ```

<br />

### 커서

- 드래그 제한 \
  `user-select: none`

<br />

## ETC

### 용어

- 플랫 디자인: 입체효과를 제거하고 단순화시킴으로 직관적인 인식이 가능케하는 2차원 디자인
- 머티리얼 디자인: 가상 빛을 이용한 입체효과로 입체감부여
- 캐러셀: 슬라이드
- 타이포그래피: 글자를 활용한 모든 디자인

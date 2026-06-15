# CSS - PBL

```html
<link rel="stylesheet" type="text/css" href="sample" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

**-webkit-**: 크롬, 사파리\
**-moz-**: 모질라, 파이어폭스\
**-ms-**: 익스플로러\
**-o-**: 오페라

- [참고 사이트](#참고-사이트)
- [레이아웃](#레이아웃)
  - [Box](#box)
  - [Flex](#flex)
    - [Flex내의 `flex: 1;`인 자식 요소가 부모에 맞춰 크기 줄어들게 하기](#flex내의-flex-1인-자식-요소가-부모에-맞춰-크기-줄어들게-하기)
  - [Grid](#Grid)
  - [Table](#table)
- [이미지](#이미지)
  - [SVG](#svg)
- [텍스트](#텍스트)
  - [생략](#생략)
  - [그라디언트](#그라디언트)
- [스크롤](#스크롤)
  - [스냅 포커싱](#스냅-포커싱)
  - [flex내 요소 스크롤 적용](#flex내-요소-스크롤-적용)
  - [스크롤 제한](#스크롤-제한)
    - [모달 아래 요소 스크롤 방지](#모달-아래-요소-스크롤-방지)
    - [당겨서 새로고침 방지](#당겨서-새로고침-방지)
    - [이전/다음 페이지 이동 방지(사파리)](#이전다음-페이지-이동-방지사파리)
- [변형 및 애니메이션](#변형-및-애니메이션)
- [기타](#기타)
  - [효과](#효과)
  - [기타 속성](#기타-속성)
  - [용어](#용어)

---

## 참고 사이트

- `http://gridstackjs.com/`: DnD 및 크기 조정 시 레이아웃 배치 라이브러리

변형 관련

- `https://codepen.io/vineethtr/full/XKKEgM`: Transform

Flex 관련

- https://codepen.io/enxaneta/pen/adLPwv
- https://css-tricks.com/snippets/css/a-guide-to-flexbox/

---

## 레이아웃

### Box

- `box-sizing: border-box;`: width 및 height 크기가 border크기를 포함

<br />

### Flex

- `flex-wrap: wrap;`: 부모 크기 오버시 아래에 정렬

<br />

#### Flex내의 `flex: 1;`인 자식 요소가 부모에 맞춰 크기 줄어들게 하기

부모가 `flex-direction: row;`이며, 자식이 `flex: 1;`인 상황에서 가로 크기를 부모에 맞춰 줄어들게 할 때,
자식요소에 `min-width: 0px;` 지정

<br />

### Grid

- 상위요소

  ```scss
  display: grid;
  gap: 10px;
  grid-template-columns: 1fr 2fr auto 100px; // 너비
  grid-template-rows: repeat(2, minmax(100px, auto)); // 높이

  grid-auto-flow: row; // 왼쪽에서 오른쪽으로, 위에서 아래로 배치
  grid-auto-flow: column; // 위에서 아래로, 왼쪽에서 오른쪽으로 배치

  grid-auto-flow: dense; // 순서에 상관없이 가능한 한 빈 공간을 채우도록 배치
  grid-auto-flow: row dense; // or column dense

  grid-auto-columns: max-content; // grid-template-columns를 사용하지 않고, 하위 요소의 가로길이 만큼 자동 조정 (== tw: auto-cols-max)
  ```

- 하위요소

  ```scss
  grid-column: 4; // 네 번째 열 뒤에 위치
  grid-column: 1 / 3; // 첫 번째 열 ~ 세 번째 열 차지(두 칸)
  grid-column: 2 / span 3; // 두 번째 열에서 3개의 열을 차지(세 칸)
  grid-row: 2 / -1; // 두 번째 행에서 끝에서 첫 번째 행(마지막 행)까지 차지
  ```

<br />

### Table

- `table-layout: fixed;`: 테이블의 내부 요소가 커져도 th 및 td 크기를 고정 시킴

---

## 이미지

- `background-clip: border-box;`: 배경(background-color, background-image)을 border 영역까지 표시

### SVG

- 요소 크기를 부모 크기에 맞추기(비율 유지 제거)
  -> 해당 파일 태그 내의 `preserveAspectRatio` 속성을 `none`으로 변경
- 색 변경 반영
  -> 해당 파일 태그 내의 `fill` 또는 `stroke` 속성에 `currentColor`로 변경

---

## 텍스트

- `text-indent: 10px;`: 들여쓰기
- `letter-spacing: 10px;`: 글자간격
- `line-height: 10px;`: 줄간격

### 생략

```scss
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

### 그라디언트

```scss
background-image: linear-gradient(to right, #7dd3fc, #4f46e5);
background-clip: text;
color: transparent;
```

---

## 스크롤

- `scroll-behavior: smooth;`: 화면 내 부드러운 이동

### 스냅 포커싱

```scss
// 부모 요소
overflow-y: auto;
scroll-snap-type: y mandatory;

// 자식 요소
scroll-snap-align: start;
```

<br />

### flex내 요소 스크롤 적용

```scss
// flex요소(+ 그 상위 요소)
overflow: hidden;

// 스크롤 대상 요소
overflow: auto;
// 또는
flex: auto;
height: 0;
overflow: auto;
```

- flex요소 내 `상위 - 중간 - 하위`구조에서 하위 요소가 스크롤인 경우

  ```scss
  // 상위
  display: flex;
  flex: auto;
  height: 0;

  // 중간
  display: flex;
  height: 100%; // 또는 flex: 1;
  overflow: hidden; // 방향은 상관 없음

  // 스크롤 대상 하위 요소
  flex: 1 1 0;
  overflow-y: auto;
  ```

  또는

  ```scss
  // 상위
  display: flex;
  flex: 1; // 상하 full
  overflow: hidden;

  // 중간
  display: flex;
  height: 100%;

  // 스크롤 대상 하위 요소
  overflow-y: auto;
  ```

<br />

### 스크롤 제한

#### 모달 아래 요소 스크롤 방지

`overscroll-behavior: contain`: 스크롤링 체인을 제한

#### 당겨서 새로고침 방지

```scss
body {
  overscroll-behavior-y: contain;
}
```

- 또는 html의 스타일에서 `overflow: hidden` 적용
- 또는 최상위 요소에 `overscroll-behavior: none;` 적용

#### 이전/다음 페이지 이동 방지(사파리)

`overscroll-behavior: none`: 스크롤 영역 경계 제한

---

## 변형 및 애니메이션

- `transform: translate(x,y) | scale(x,y) | rotateX(45deg) | skew(xdeg, ydeg)`
- `transform-origin: left top;`: 중심점 변경
- `transition: all 1s ease-in-out;`
- `animation: fadeIn 1s ease infinite;`
- `animation: fadeIn 1s ease forwards;`

---

## 기타

### 효과

- `filter: blur(5px);`
  - [참고](https://georapbox.github.io/css-filters-playground/)
  - 대상 요소에 대해 적용(background-image 제외)
- `backdrop-filter: blur(10px);`: 대상 요소 뒤의 영역에 대해 적용

<br />

### 기타 속성

- `user-select: none;`: 드래그 제한

<br />

### 용어

- 플랫 디자인: 입체효과를 제거하고 단순화시킴으로 직관적인 인식이 가능케하는 2차원 디자인
- 머티리얼 디자인: 가상 빛을 이용한 입체효과로 입체감부여
- 캐러셀: 슬라이드
- 타이포그래피: 글자를 활용한 모든 디자인
- 리퀴드 글라스: 글래스모피즘의 질감에 액체(Liquid)의 유기적인 움직임을 더한 인터페이스
- Masonry 레이아웃: 벽돌을 쌓아 올린 모양처럼 동일한 너비를 가진 이미지가 엇갈려 배열(ex. Pinterest)
- Justified 레이아웃: 한 행을 기준으로 이미지가 가득 차도록 배치

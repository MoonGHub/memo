# CSS - Attribute-Value

### 🦋 접두어

**-webkit-**: 크롬, 사파리\
**-moz-**: 모질라, 파이어폭스\
**-ms-**: 익스플로러\
**-o-**: 오페라

<br />

## Attribute-Value

### 배경

```css
background-image: linear-gradient(
    to bottom,
    rgba(255, 255, 0, 0.5),
    rgba(0, 0, 255, 0.5)
  ), url("catfront.png");
// 콤마로 여러개 지정 가능
background-position: center;
background-position: 25% 75%;
background-repeat: no-repeat;
background-attachment: fixed;
// 스크롤 고정
background-size: auto;
background-size: 가로px 세로px;
background-blend-mode: soft-light;
// 배경 요소가 겹칠 경우 나타내는 방식 지정(사진, 동영상 색상변경, 흑백, 반전 등)
mix-blend-mode: difference;
// 위와 동일
```

#### 필터

[참고](https://georapbox.github.io/css-filters-playground/)

```css
filter: blur(5px);
// 사진, 동영상 색상변경, 흑백, 반전 등
```

<br />

### 텍스트

#### 간격

```css
text-indent: 10px;
// 들여쓰기
letter-spacing: 10px;
// 글자간격
line-height: 10px;
// 줄간격
text-align: justify;
// 글자가 양쪽을 균등히 배분
```

#### 단 나누기

```css
columns: auto 3;
// 너비 자동, 단 3개
column-rule: 1px solid black;
// 단 사이의 border

column-count: 4;	// (최대) 단 수
        column-width: 200px; */  // 단 폭 길이
        column-gap:30px; 	// 단 간격
        column-rule-style: solid;
        column-rule-width: 5px;
        column-rule-color: red;

```

<br />

### 애니메이션

#### transform

[참고](https://codepen.io/vineethtr/full/XKKEgM)

```css
transform: translate(x,y) | scale(x,y) | rotateX(45deg) | skew(xdeg, ydeg)
transform-origin: left top;
// 중점 변경
```

#### transition

[참고](https://matthewlein.com/tools/ceaser)

```css
transition: all 1s ease-in-out;

// 위와 동일
transition-property: all;
transition-duration: 1s;
transition-timing-function: ease-in-out | linear | ease(천천 빨리 천천);

// 기타 옵션들
transition-delay: 0s;
```

#### keyframes - animation

```css
@keyframes ani {
  from {
    // ...;
  }
  50% {
    // ...;
  }
  to {
    // ...;
  }
}

animation-name: ani;
```

- `animation-duration: 1s;`: 한 싸이클 시간
- `animation-delay: 1s;`: 로드 후 지연 시간
- `animation-direction: normal;`: 애니메이션이 종료 후 순방향, 역방향 지정
  - normal: 순반향
  - alternate: 순, 역 반복
  - reverse: 역박향
  - alternate-reverse: 역, 순 반복
- `animation-iteration-count: 2;`: 반복 횟수
  - infinite: 무한
- `animation-play-state: running;`: 멈추거나, 다시 시작
  - running
  - paused
- `animation-timing-function: ease;`: @keyframes의 상태들의 시간간격
  - ease
  - ease-in-out
- `animation-fill-mode: forwards;`: 애니메이션이 전후의 적용 값
  - none
  - forwards: 마지막 키프레임 상태 유지
  - backwards: 스타일을 먼저 지정
  - both: forwards와 backwards 둘 다 적용

<br />

### grid

- 함수
  - [minmax()](./Function.md#minmax)
  - [fit-content()](./Function.md#fit-content)
  - [repeat()](./Function.md#repeat)

<br />

- 상위요소

  ```css
  display: grid;
  gap: 10px;
  grid-template-columns: 1fr 2fr auto 100px;
  // 너비 지정
  grid-template-rows: repeat(2, minmax(100px, auto));
  // 높이 지정

  grid-auto-flow: row;
  // 왼쪽에서 오른쪽으로, 위에서 아래로 배치
  // 그리드 아이템이 채워진 행이 다 차면 새로운 행이 생성
  grid-auto-flow: column;
  // 위에서 아래로, 왼쪽에서 오른쪽으로 배치
  // 그리드 아이템이 채워진 열이 다 차면 새로운 열이 생성
  grid-auto-flow: dense;
  grid-auto-flow: row dense; // or column dense
  // 그리드 아이템이 순서에 상관없이 가능한 한 빈 공간을 채우도록 배치
  ```

- 하위요소

  ```css
  grid-column: 4;
  // 네 번째 열뒤에 위치
  grid-column: 1 / 3;
  // 첫 번째 열 ~ 세 번째 열 차지(두 칸)
  grid-column: 2 / span 3;
  // 두 번째 열에서 3개의 열을 차지(세 칸)
  grid-row: 2 / -1;
  // 두 번째 행에서 끝에서 첫 번째 행(마지막 행)까지 차지
  ```

- subgrid

  > 그리드인 부모요소의 하위요소에서 사용\
  > 부모 그리드 컬럼과 동기화(상속)\
  > **_모든 브라우저에서 완전 지원되지 않음_**

  - [참고1](https://codepen.io/kumjungmin/pen/qBxRVey)
  - [참고2](https://codepen.io/rachelandrew/pen/axLzYv)

  ```css
  // 그리드인 부모요소의 하위요소
  display: grid;
  grid-row: 1 / 4;
  grid-template-rows: subgrid;
  ```

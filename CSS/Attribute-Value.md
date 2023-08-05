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

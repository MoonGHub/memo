# CSS - Attribute-Value

### ๐ฆ ์ ๋์ด

**-webkit-**: ํฌ๋กฌ, ์ฌํ๋ฆฌ\
**-moz-**: ๋ชจ์ง๋ผ, ํ์ด์ดํญ์ค\
**-ms-**: ์ต์คํ๋ก๋ฌ\
**-o-**: ์คํ๋ผ

<br />

## Attribute-Value

### ๋ฐฐ๊ฒฝ

```css
background-image: linear-gradient(
    to bottom,
    rgba(255, 255, 0, 0.5),
    rgba(0, 0, 255, 0.5)
  ), url("catfront.png");
// ์ฝค๋ง๋ก ์ฌ๋ฌ๊ฐ ์ง์  ๊ฐ๋ฅ
background-position: center;
background-position: 25% 75%;
background-repeat: no-repeat;
background-attachment: fixed;
// ์คํฌ๋กค ๊ณ ์ 
background-size: auto;
background-size: ๊ฐ๋กpx ์ธ๋กpx;
background-blend-mode: soft-light;
// ๋ฐฐ๊ฒฝ ์์๊ฐ ๊ฒน์น  ๊ฒฝ์ฐ ๋ํ๋ด๋ ๋ฐฉ์ ์ง์ (์ฌ์ง, ๋์์ ์์๋ณ๊ฒฝ, ํ๋ฐฑ, ๋ฐ์  ๋ฑ)
```

#### ํํฐ

[์ฐธ๊ณ ](https://georapbox.github.io/css-filters-playground/)

```css
filter: blur(5px);
// ์ฌ์ง, ๋์์ ์์๋ณ๊ฒฝ, ํ๋ฐฑ, ๋ฐ์  ๋ฑ
```

<br />

### ํ์คํธ

#### ๊ฐ๊ฒฉ

```css
text-indent: 10px;
// ๋ค์ฌ์ฐ๊ธฐ
letter-spacing: 10px;
// ๊ธ์๊ฐ๊ฒฉ
line-height: 10px;
// ์ค๊ฐ๊ฒฉ
text-align: justify;
// ๊ธ์๊ฐ ์์ชฝ์ ๊ท ๋ฑํ ๋ฐฐ๋ถ
```

#### ๋จ ๋๋๊ธฐ

```css
columns: auto 3;
// ๋๋น ์๋, ๋จ 3๊ฐ
column-rule: 1px solid black;
// ๋จ ์ฌ์ด์ border

column-count: 4;	// (์ต๋) ๋จ ์
        column-width: 200px; */  // ๋จ ํญ ๊ธธ์ด
        column-gap:30px; 	// ๋จ ๊ฐ๊ฒฉ
        column-rule-style: solid;
        column-rule-width: 5px;
        column-rule-color: red;

```

<br />

### ์ ๋๋ฉ์ด์

#### transform

[์ฐธ๊ณ ](https://codepen.io/vineethtr/full/XKKEgM)

```css
transform: translate(x,y) | scale(x,y) | rotateX(45deg) | skew(xdeg, ydeg)
transform-origin: left top;
// ์ค์  ๋ณ๊ฒฝ
```

#### transition

[์ฐธ๊ณ ](https://matthewlein.com/tools/ceaser)

```css
transition: all 1s ease-in-out;

// ์์ ๋์ผ
transition-property: all;
transition-duration: 1s;
transition-timing-function: ease-in-out | linear | ease(์ฒ์ฒ ๋นจ๋ฆฌ ์ฒ์ฒ);

// ๊ธฐํ ์ต์๋ค
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

- `animation-duration: 1s;`: ํ ์ธ์ดํด ์๊ฐ
- `animation-delay: 1s;`: ๋ก๋ ํ ์ง์ฐ ์๊ฐ
- `animation-direction: normal;`: ์ ๋๋ฉ์ด์์ด ์ข๋ฃ ํ ์๋ฐฉํฅ, ์ญ๋ฐฉํฅ ์ง์ 
  - normal: ์๋ฐํฅ
  - alternate: ์, ์ญ ๋ฐ๋ณต
  - reverse: ์ญ๋ฐํฅ
  - alternate-reverse: ์ญ, ์ ๋ฐ๋ณต
- `animation-iteration-count: 2;`: ๋ฐ๋ณต ํ์
  - infinite: ๋ฌดํ
- `animation-play-state: running;`: ๋ฉ์ถ๊ฑฐ๋, ๋ค์ ์์
  - running
  - paused
- `animation-timing-function: ease;`: @keyframes์ ์ํ๋ค์ ์๊ฐ๊ฐ๊ฒฉ
  - ease
  - ease-in-out
- `animation-fill-mode: forwards;`: ์ ๋๋ฉ์ด์์ด ์ ํ์ ์ ์ฉ ๊ฐ
  - none
  - forwards: ๋ง์ง๋ง ํคํ๋ ์ ์ํ ์ ์ง
  - backwards: ์คํ์ผ์ ๋จผ์  ์ง์ 
  - both: forwards์ backwards ๋ ๋ค ์ ์ฉ

<br />

### ๋ฏธ๋์ด ์ฟผ๋ฆฌ

[์ฐธ๊ณ ](https://developer.mozilla.org/ko/docs/Web/CSS/Media_Queries/Using_media_queries#%EB%AF%B8%EB%94%94%EC%96%B4_%ED%8A%B9%EC%84%B1)

#### HTML์์์ ์ฌ์ฉ

```html
<link
  href="css/~.css"
  rel="stylesheet"
  type="text/css"
  media="screen and (min-width:321px) and (max-width:768px)"
/>
```

#### CSS๋ด์ ์ฌ์ฉ

@import์ฌ์ฉ

```css
@import url("css/~.css") screen and (min-width: 321px) and (max-width: 768px);
```

ํ๊ทธ ์ฌ์ฉ

```css
@media ๋ฏธ๋์ด์ ํ | ๋ฏธ๋์ดํน์ฑ | ๋ฏธ๋์ด๊ธฐ๋ฅ [๋ผ๋ฆฌ ์ฐ์ฐ์ ๋ฏธ๋์ด์ ํ | ๋ฏธ๋์ดํน์ฑ | ๋ฏธ๋์ด๊ธฐ๋ฅ ...] {
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

- ๋ฏธ๋์ด์ ํ
  - all
  - print
  - screen
  - speech
- ๋ฏธ๋์ด ํน์ฑ ์์
  - (orientation: landscape)
- ๋ฏธ๋์ด๊ธฐ๋ฅ ์์
  - (hover: hover)
  - (max-width: 12450px)
- ๋ผ๋ฆฌ ์ฐ์ฐ์
  - and
  - not
  - only
  - ,(์ผํ)

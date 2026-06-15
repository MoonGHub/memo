# 미디어 쿼리

[참고](https://developer.mozilla.org/ko/docs/Web/CSS/Media_Queries/Using_media_queries#%EB%AF%B8%EB%94%94%EC%96%B4_%ED%8A%B9%EC%84%B1)

- [HTML요소에 사용](#html요소에-사용)
- [CSS내에 사용](#css내에-사용)
- [작성 방법](#작성-방법)

---

### HTML요소에 사용

```html
<link
  href="css/~.css"
  rel="stylesheet"
  type="text/css"
  media="screen and (min-width:321px) and (max-width:768px)"
/>
```

<br />

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

<br />

### 작성 방법

- 미디어유형
  - `all`
  - `print`
  - `screen`
  - `speech`
- 미디어 특성 예시
  - `(orientation: landscape)`
  - `(prefers-color-scheme: dark)`
- 미디어 기능 예시
  - `(hover: hover)`: 모바일에서의 hover 제한
  - `(prefers-reduced-motion: no-preference)`:동작 모드
  - `(prefers-reduced-motion: reduce)`: 동작 줄이기 모드
  - `(max-width: 12450px)`
- 논리 연산자
  - `and`
  - `not`
  - `only`
  - `,`(쉼표)

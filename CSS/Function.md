# CSS - Function

- url()
- [linear-gradient()](#linear-gradient)
- [attr()](#css내에서-html요소-속성-참조)

<br />

### linear-gradient

`linear-gradient(각도 또는 위치, color-stop(시작색), [color-stop,...])`

- 위치: `to left`, `to bottom`
- 각도: `0deg`(아래->위), `90deg`(왼->오), `270deg`(오->왼), `180deg`(위->아래), ... 등
- 두번 째 인자부터: `red`, `green 10%`, `40%`, `blue 50% 100%`, ... 등(% 범위를 나타냄 )
- ex)
  ```css
  background: linear-gradient(
    to right,
    red 20%,
    orange 20% 40%,
    yellow 40% 60%,
    green 60% 80%,
    blue 80%
  );
  ```

<br />

### CSS내에서 HTML요소 속성 참조

```html
<a href="home">홈</a>
```

```css
a::after {
  content: " (" attr(href) ") ";
}
```

==> 홈 (home)

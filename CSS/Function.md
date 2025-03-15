# CSS - Function

- url()
- [linear-gradient()](#linear-gradient)
- [attr()](#css내에서-html요소-속성-참조)
- [minmax()](#minmax)
- [fit-content()](#fit-content)
- [repeat()](#repeat)

<br />

### linear-gradient

`linear-gradient(각도 또는 위치, color-stop(시작색), [color-stop,...])`

- 위치: `to left`, `to bottom`
- 각도: `0deg`(아래->위), `90deg`(왼->오), `270deg`(오->왼), `180deg`(위->아래), ... 등
- 두 번째 인자부터: `red`, `green 10%`, `40%`, `blue 50% 100%`, ... 등(% 범위를 나타냄 )
- ex)
  ```scss
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

```scss
a::after {
  content: " (" attr(href) ") ";
}
```

결과: 홈 (home)

<br />

### minmax

`minmax( min , max )`

> grid요소에서 사용

- ex)

  ```scss
  display: grid;
  grid-template-rows: repeat(2, minmax(20px, auto));
  grid-template-columns: minmax(30px, auto) repeat(3, 1fr);
  ```

<br />

### fit-content

`fit-content( length )`

> grid요소에서 사용\
> 열의 너비를 해당 열의 내용에 맞게 조정하되, 최대 너비를 지정 크기까지만 제한

- ex)

  ```scss
  display: grid;
  grid-template-columns: fit-content(40%) fit-content(40%) 1fr;
  // 하위 요소 너비에 맞추되 최대 너비를 40%로 제한
  ```

<br />

### repeat

`repeat( count, tracks )`

> grid요소에서 사용\
> count만큼 tracks를 반복

- ex)

  ```scss
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  // 결과: 1fr 1fr 1fr 1fr

  grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
  // 공간이 남을 경우, 셀 생성
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  // 셀의 길이를 너비에 맞게 연장
  ```

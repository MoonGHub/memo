# JavaScript - ETC

### ๐ฆ ์ด๋ฒคํธ ์ ํ

์บก์ฒ -> ํ๊น -> ๋ฒ๋ธ๋ง
์บก์ฒ : window์์ ๋์ ์์๊น์ง
ํ์ผ : ๋์ ์์์ ๋์ฐฉํ ๋์ ๋จ๊ณ
๋ฒ๋ธ๋ง : ๋์์์์์ ์ด๋ฒคํธ ์บก์ฒ ํ ์์์์๋ก ์ด๋ฒคํธ ์ ํ

<br />

### ๐ฆ DOM ์์ ํ์์ ๋ฐํ ๊ฐ๋ค

#### HTMLCollection

getElementsByTagName
(์ธ๋ฑ์ค์ ๊ทผ์ด์ง๋ง ๋ฐฐ์ด์ด ์๋)

#### NodeList

getElementsByClassName
querySelector() ..?
querySelectorAll() ..?

<br />

### ๐ฆ this์ context scope

- function์ this๋ window๋ฅผ ๊ฐ๋ฅดํด

<br />

### ๐ฆ block scope

```js
var i;

for (i = 0; i < 10; i++) {
  (function (j) {
    setTimeout(function () {
      console.log(j);
    }, 100);
  })(i);
}
```

์ ์ฒ๋ผ ์ฌ์ฉํ๊ฑฐ๋, var ํค์๋ ๋์  let ํค์๋๋ก ๋ฐ๊ฟ์ค

<br />

### ๐ฆ **prototype** and **\_\_proto\_\_**

- prototype

  ```js
  function Shape() {
    this.x = 0;
    this.y = 0;
  }

  Shape.prototype.move = function (x, y) {
    this.x += x;
    this.y += y;

    console.info("Shape moved.");
  };

  function Rectangle() {
    Shape.call(this); // super ์์ฑ์ ํธ์ถ.
  }

  Rectangle.prototype = Object.create(Shape.prototype);
  Rectangle.prototype.constructor = Rectangle;

  var rect = new Rectangle();
  ```

- \_\_proto\_\_

  ```js

  ```

<br />

### ๐ฆ strict ๋ชจ๋

> 1. ๊ธฐ์กด์๋ ์กฐ์ฉํ ๋ฌด์๋๋ ์๋ฌ๋ค์ throwing
> 2. JavaScript ์์ง์ ์ต์ ํ ์์์ ์ด๋ ต๊ฒ ๋ง๋๋ ์ค์๋ค์ ์ก์
> 3. ์๊ฒฉ ๋ชจ๋์ ์ฝ๋๋ ๋น์๊ฒฉ ๋ชจ๋์ ๋์ผํ ์ฝ๋๋ณด๋ค ๋ ๋นจ๋ฆฌ ๊ธฐ๋ฅ ํ  ์ ์์
> 4. ์๊ฒฉ ๋ชจ๋๋ ECMAScript์ ์ฐจ๊ธฐ ๋ฒ์ ๋ค์์ ์ ์ ๋  ๋ฌธ๋ฒ์ ๊ธ์ง
> 5. ๋ชจ๋๋ฐฉ์์ ๊ธฐ๋ณธ์ ์ผ๋ก strict๋ชจ๋

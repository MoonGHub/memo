# JavaScript - ETC

### 🦋 이벤트 전파

캡처 -> 타깃 -> 버블링
캡처 : window에서 대상 요소까지
타켓 : 대상 요소에 도착한 대상 단계
버블링 : 대상요소에서 이벤트 캡처 후 상위요소로 이벤트 전파

<br />

### 🦋 DOM 요소 탐색의 반환 값들

#### HTMLCollection

getElementsByTagName
(인덱스접근이지만 배열이 아님)

#### NodeList

getElementsByClassName
querySelector() ..?
querySelectorAll() ..?

<br />

### 🦋 this의 context scope

- function의 this는 window를 가르킴

<br />

### 🦋 block scope

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

위 처럼 사용하거나, var 키워드 대신 let 키워드로 바꿔줌

<br />

### 🦋 **prototype** and **\_\_proto\_\_**

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
    Shape.call(this); // super 생성자 호출.
  }

  Rectangle.prototype = Object.create(Shape.prototype);
  Rectangle.prototype.constructor = Rectangle;

  var rect = new Rectangle();
  ```

- \_\_proto\_\_

  ```js

  ```

<br />

### 🦋 StrictMode

> 1. 기존에는 조용히 무시되던 에러들을 throwing
> 2. JavaScript 엔진의 최적화 작업을 어렵게 만드는 실수들을 잡음
> 3. 엄격 모드의 코드는 비엄격 모드의 동일한 코드보다 더 빨리 기능 할 수 있음
> 4. 엄격 모드는 ECMAScript의 차기 버전들에서 정의 될 문법을 금지
> 5. 모듈방식은 기본적으로 strict모드

<br />

### 🦋 **ESM** vs **CJS**

- ESM: ECMAScript Module

  - import/export
  - package.json의 **type**이 **module**이거나, 확장자가 **.mjs**
  - package.json의 **type**이 **module**인 경우

    - `.mjs`또는 `.js`사용
    - import 사용이 강제됨
    - import시, 해당 파일의 확장자 명시 필요\
      **아래와 같은 설정으로 무시 가능**

      - 웹팩 사용의 경우(Storybook 설정도 마찬가지)
        ```js
        // webpack.config.js
        {
        		test: /\.m?js/,
        		resolve: {
        			fullySpecified: false,
        		},
        },
        ```
      - Vite의 경우

        ```js

        ```

      - Vite의 SSR(Node 환경)의 경우
        ```js
        // vite.config.ts
        {
          ssr: {
            noExternal: [
              "@react-financial-charts/**/*",
              "react-financial-charts",
            ],
          },
        }
        ```

- CJS: CommonJS

  - require/module.exports
  - package.json의 **type**이 **commonjs**이거나, 확장자가 **.cjs**
  - package.json의 **type**이 **commonjs**인 경우
    - `.cjs`또는 `.js`사용
    - require 사용이 강제됨

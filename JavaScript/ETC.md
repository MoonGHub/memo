# JavaScript - ETC

### 이벤트 전파

캡처 -> 타깃 -> 버블링
캡처 : window에서 대상 요소까지
타켓 : 대상 요소에 도착한 대상 단계
버블링 : 대상요소에서 이벤트 캡처 후 상위요소로 이벤트 전파

<br />

### DOM 요소 탐색의 반환 값들

#### HTMLCollection

getElementsByTagName
(인덱스접근이지만 배열이 아님)

#### NodeList

getElementsByClassName
querySelector() ..?
querySelectorAll() ..?

<br />

### this의 context scope

- function의 this는 window를 가르킴

<br />

### block scope

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

### **prototype** and **\_\_proto\_\_**

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

### StrictMode

> 1. 기존에는 조용히 무시되던 에러들을 throwing
> 2. JavaScript 엔진의 최적화 작업을 어렵게 만드는 실수들을 잡음
> 3. 엄격 모드의 코드는 비엄격 모드의 동일한 코드보다 더 빨리 기능 할 수 있음
> 4. 엄격 모드는 ECMAScript의 차기 버전들에서 정의 될 문법을 금지
> 5. 모듈방식은 기본적으로 strict모드

<br />

### **ESM** vs **CJS**

> 결론: ESM가 CJS보다 안정적이며 정적인 특성으로 트러블슈팅이 편함

- ESM: ECMAScript Module

  - import/export 구문 사용
  - 최상위에서 작성하며, 정적인 값으로만 가능
    - Top-level Await 지원?
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
            optimizeDeps: {
              disabled: "build",
              // 의존성 최적화 비활성화로 true는 build와 dev 모두 포함
              include: ["react-financial-charts"],
              // 모노레포에서 알아서 탐색이 되지만 번들이 되지않음
              // 연결된 패키지를 미리 번들화
              // ??? - 해당 디펜던시가 ESM로 내보내져야 함, 그렇지 않다면 명시 필요(강제 최적화?)
            },
            noExternal: ["react-financial-charts"],
            // 기본적으로 SSR은 디펜던시를 번들링에 포함하지 않음(초기 로딩이 빨라짐)
            // 설정 시, 외부화에서 제외, 번들링에 포함됨
          },
        }
        ```

- CJS: CommonJS

  - require/module.exports 구문 사용
  - 동적인 값으로 처리 가능
    - 임의 시점(조건문 등)에서 require 사용 가능
    - 빌드 단계에서 전체 코드를 알 수 없어, 불 필요한 부분의 체킹이 불가(번들 사이즈를 못줄임)
  - package.json의 **type**이 **commonjs**이거나, 확장자가 **.cjs**
  - package.json의 **type**이 생략 또는 **commonjs**인 경우
    - `.cjs`또는 `.js`사용
    - require 사용이 강제됨

<br />

### Node에서의 CJS과 ESM

노드에서는 기본적으로 CJS의 require이 사용된다.\
ESM의 import/export 구문을 사용하기 위해서는 **package.json**에서 `type: "module"`로 지정이 필요하다

- `type: "module"`을 지정하면 모든 파일(?)이 ESM구문을 사용해야 한다.
- `type: "module"`인 프로젝트에서 외부 라이브러리가 CJS의 require을 사용 할 경우,\
  `require is not defined` 에러가 발생 할 수 있음
  > 해결법:
  >
  > 1. `type: "module"`을 제거 후, import구문을 require로 변경
  > 2. 위 내용을 [참고](#esm-vs-cjs)
  > 3. 해당 모듈을 lazy 로딩하여 사용 [참고](../React/Grammar.md#suspense)

<br />

### Generator Function (function\*, yield)

```js
function* generator(i) {
  yield i;
  yield i + 10;
}

const gen = generator(10);

console.log(gen.next().value);
// Expected output: 10

console.log(gen.next().value);
// Expected output: 20
```

```js
function* foo(index) {
  while (index < 2) {
    yield index;
    index++;
  }
}

const iterator = foo(0);

console.log(iterator.next().value);
// Expected output: 0

console.log(iterator.next().value);
// Expected output: 1
```

```js
function* func1() {
  yield 42;
}

function* func2() {
  yield* func1();
}

const iterator = func2();

console.log(iterator.next().value);
// Expected output: 42
```

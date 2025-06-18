# JavaScript - ETC

- [prototype and \_\_proto\_\_](#prototype-and-__proto__)
- ["use strict"](#use-strict)
- [ESM vs CJS](#esm-vs-cjs)
- [제네레이터 함수](#제네레이터-함수---generator-function-function-yield)

## **prototype** and **\_\_proto\_\_**

- `prototype`: 생성자 함수가 생성할 객체의 프로토타입 정의\
  new 키워드로 인스턴스 생성시, `prototype`에 연결된 객체를 `__proto__`로 연결

  ```javascript
  function Shape() {
    this.x = 0;
    this.y = 0;
  }

  // 상속할 함수 정의
  Shape.prototype.move = function (x, y) {
    this.x += x;
    this.y += y;

    console.info("Shape moved.");
  };

  // new 키워드로 실행됨
  function Rectangle() {
    Shape.call(this); // super 생성자 호출, x와 y 바인딩 및 초기화
  }

  // Shape의 프로퍼티 상속
  Rectangle.prototype = Object.create(Shape.prototype);
  // 생성자를 명시적으로 Rectangle 변경, 안하면 Shape.prototype의 constructor를 가르킴
  Rectangle.prototype.constructor = Rectangle;

  let rect = new Rectangle();

  rect.move(10, 20); // Shape moved.

  console.log(rect.x, rect.y); // 10 20
  console.log(rect.constructor); // [Function: Rectangle]
  ```

- `__proto__`: 프로토타입 체인 - 상속

  ```javascript
  const parent = {
    sayHello() {
      console.log("Hello from parent");
    },
  };

  const child = {
    name: "child",
  };

  // 프로토타입 체인 연결
  child.__proto__ = parent;

  // parent의 메서드를 child가 사용 가능
  child.sayHello(); // "Hello from parent"
  ```

---

## "use strict"

1. 기존에는 조용히 무시되던 에러들을 throwing
   - 정의되지 않은 변수에 값을 할당(window에 바인딩) 등
2. JavaScript 엔진의 최적화 작업을 어렵게 만드는 실수들을 잡음
   - 특정 패턴/함수 제약 등
3. 엄격 모드의 코드는 비엄격 모드의 동일한 코드보다 더 빨리 기능 할 수 있음
4. 엄격 모드는 ECMAScript의 차기 버전들에서 정의 될 문법을 금지
   - 미래의 예약어 방지
5. 모듈방식`(ES6의 "type": "module")`은 기본적으로 strict모드

---

## **ESM** vs **CJS**

> ESM가 CJS보다 안정적이며 정적인 특성으로 트러블슈팅이 편함

### ESM(ECMAScript Module)

- import/export 구문 사용
- 최상위에서 작성하며, 정적인 값으로만 가능
  - Top-level Await 지원
- package.json의 **type**이 **module**이거나, 파일의 확장자가 **.mjs**

### CJS(CommonJS)

- require/module.exports 구문 사용
- 동적인 값으로 처리 가능
  - 임의 시점(조건문 등)에서 require 사용 가능
  - 빌드 단계에서 전체 코드를 알 수 없어, 불 필요한 부분의 체킹이 불가(번들 사이즈를 못줄임)
- package.json의 **type**이 **commonjs**이거나, 파일의 확장자가 **.cjs**
- package.json의 **type**이 생략되는 경우, `CJS`로 인식

### Node에서의 CJS과 ESM

노드에서는 기본적으로 CJS의 require 문법을 사용
ESM의 import/export 구문을 사용하기 위해서는 **package.json**에서 `type: "module"`로 지정이 필요

- `type: "module"`인 프로젝트에서 외부 라이브러리가 CJS의 require을 사용 할 경우, `require is not defined` 에러가 발생 할 수 있음

  - 사용 번들러의 솔루션을 따름
  - 해당 모듈을 `React.lazy`와 같은 lazy로딩을 사용하여 해결

---

## 제네레이터 함수 - Generator Function (function\*, yield)

```javascript
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

```javascript
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

```javascript
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

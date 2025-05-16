# Rust - Grammar

## Basic

- `Trait`: Interface 와 비슷하지만 다름

  ```rs
  trait Greet {
      fn say_hello(&self);
  }

  struct Person;

  impl Greet for Person {
      fn say_hello(&self) {
          println!("Hello!");
      }
  }
  ```

- `Struct`: 상속 없는 클래스 느낌

  ```rs
  struct Point {
      x: i32,
      y: i32,
  }

  let p = Point { x: 1, y: 2 };
  println!("({}, {})", p.x, p.y);
  ```

- `Closure`: 익명 함수, 람다와 유사

  > let 변수명 = |매개변수| 표현식;

  ```rs
  let add = |a: i32, b: i32| a + b;

  println!("{}", add(2, 3)); // 5
  ```

- `Module`: 네임스페이스

  ```rs
  mod math {
      pub fn add(a: i32, b: i32) -> i32 {
          a + b
      }
  }

  let result = math::add(1, 2);
  println!("{}", result);
  ```

- `Option`: Maybe monad

  ```rs
  fn get_age(name: &str) -> Option<u8> {
      if name == "Alice" {
          Some(30)
      } else {
          None
      }
  }

  match get_age("Alice") {
      Some(age) => println!("Age is {}", age),
      None => println!("No age found"),
  }
  ```

- `Enum`: Algebraic data type - 서로 다른 타입들끼리의 묶음

  ```rs
  enum Direction {
      North,
      South,
      East,
      West,
  }

  let dir = Direction::North;

  match dir {
      Direction::North => println!("Going up"),
      _ => println!("Not going up"),
  }
  ```

- 기타 용어
  - 캡처: 클로저가 외부 변수에 접근할 때 그 값을 내부에서 사용하기 위해 가져오는 것

### Type(Trait)

- `Result<T, E>` - `Ok(T)`, `Err(E)`
  - `Result<u8, _>`: 성공 시 `u8`, 에러 시 `_`(알 수 없는 타입 -> 타입 추론)
  - `Result<Self, Self::Error>`
- `&'static str`: 고정된 메시지나 변경되지 않는 데이터 일 때 사용
- `String`: 동적 문자열 일 때 사용
- `Fn`, `FnMut`, `FnOnce`: 호출 가능한 객체(클로저, 함수 포인터 등)의 추상 타입

  ```rs
  fn make_adder(x: i32) -> impl Fn(i32) -> i32 {
      move |y| x + y
  }

  fn run_with_callback1(x: i32, callback: impl Fn(i32)) {
      callback(x);
  }
  // 또는
  fn run_with_callback2<F>(x: i32, callback: F)
  where
      F: Fn(i32),
  {
      callback(x);
  }
  // 또는
  fn run_with_callback3<F: Fn(i32)>(x: i32, callback: F) {
      callback(x);
  }
  ```

  - `Fn()`: 외부 변수(환경)를 불변 참조(&x)로 캡처
  - `FnMut()`: 외부 변수(환경)를 가변 참조(&mut x)로 캡처, FnMut 클로저를 호출하려면 클로저 변수 자체도 mut여야 함
  - `FnOnce()`: move로 소유권을 클로저 내부로 이동시켜 소비하기 때문에, 한 번만 호출 가능

#### [Primitive](https://doc.rust-lang.org/std/index.html#primitives)

- `i8`: -128 ~ 127
- `u8`: 0 ~ 255

<br />

### [Macros](https://doc.rust-lang.org/std/index.html#macros)

- `println!`
  - 자리표시자 출력 형식:\
    `{variable_name}`: 변수명에 매칭되는 변수 출력
    `{}`: 일반 출력 - Display 트레잇을 구현해야함 - [참고](https://doc.rust-lang.org/std/fmt/trait.Display.html#examples)
    `{:?}`: 디버깅용 출력 - `#[derive(Debug)]` 속성을 추가해주면 사용 가능
    `{:#?}`: `{:?}`의 포맷팅

<br />

### [Attribute](https://doc.rust-lang.org/rust-by-example/attribute.html)

> `#![...]`
> crate 전체$^1$에 특정 동작을 지정하거나 메타데이터를 추가
> 1 :: a module or a crate

> `#[...]`
> 특정 항목$^1$에 특정 동작을 지정하거나 메타데이터를 추가
> 1 :: a function, a module declaration, a constant, a structure, an enum

[Referrence - built in attributes](https://doc.rust-lang.org/reference/attributes.html#built-in-attributes-index)

- `derive($, ...)`: $ 트레잇을 상속\
  ex) `#[derive(Clone, Debug, PartialEq)]`
  - Debug: 디버깅용 출력 제공, {:?}, {:#?}
  - Default: 지정된 타입에 대해서 기본값이 설정, i32 -> 0, String -> "", bool -> false
- `no_mangle`: C와 같은 다른 언어와의 FFI(Foreign function interface - 외부 함수 인터페이스)에서, 컴파일러가 함수 이름을 변경하지 않도록 지시하는 속성
- `cfg($)`: $(조건)이 참일 때만 포함(컴파일)\
  ex) `#[cfg(target_os = "linux")]`, `#[cfg(target_os = "macos")]`
- `cfg_attr($1, $2)`: \$1(조건)이 참일 때만, \$2(속성) 부여, 단 컴파일은 됨

<br />

### [prelude](https://doc.rust-lang.org/std/prelude/index.html)

#### [std::option::Option](https://doc.rust-lang.org/std/option/enum.Option.html)

```rs
enum Option<T> {
    Some(T), // 값이 있는 경우
    None,    // 값이 없는 경우
}
```

<br />

## PBL

### 에러 핸들링

`unwrap`, `match`, `unwrap_or`, `unwrap_or_else`, `?`
=> `Option<T>`(Some, None) 또는 `Result<T, E>`(Ok, Err)와 함께 사용

- `unwrap`: 실패(Err 또는 None)일 경우 panic 발생. 즉, 프로그램이 종료
- `?`: 실패(Err 또는 None) 시, 조기 리턴하며 panic이 발생하지 않고 에러를 전파

<br />

- 공통
  - `map`: `Ok`에 대해 변환
  - `and_then`
  - `or_else`
- Result
  - `map_err`: `Err`인 경우, 새로운 `Result<T, E2>` 반환
- Option
  - `ok_or`: `None`인 경우, 지정한 에러로 `Result<T, E>` 반환

#### match

```rs
use std::thread;

let handle = thread::spawn(|| {
    println!("{}", "good");
});

// join: 메인 스레드가 서브 스레드 끝날 때까지 기다림
match handle.join() {
    Ok(_) => println!("성공적으로 종료"),
    Err(e) => println!("스레드에서 에러 발생: {:?}", e),
}
```

#### unwrap_or - 기본값 반환

```rs
fn get_number() -> Option<i32> {
    None
}

let num = get_number().unwrap_or(42); // 실패 시 기본값 42
println!("숫자: {}", num);
```

#### unwrap_or_else - 기본값 함수 호출

```rs
fn default_number() -> i32 {
    println!("기본값을 계산 중...");
    42
}

fn get_number() -> Option<i32> {
    None
}

let num = get_number().unwrap_or_else(default_number);
println!("숫자: {}", num);
```

#### ?

```rs
fn get_name() -> Result<String, &'static str> {
    Err("이름이 없음")
}

fn greet() -> Result<(), &'static str> {
    let name = get_name()?;  // 에러가 발생하면 여기서 바로 리턴됨
    println!("안녕하세요, {}", name);
    Ok(())
}

match greet() {
    Ok(_) => println!("완료"),
    Err(e) => println!("에러 발생: {}", e),
}
```

<br />

### 소유권 가져오기 move - Closure(익명 함수)에서만 사용 가능

- 외부 변수를 복사(borrow) 말고 소유(move)하고 싶을 때!

  ```rs
  let name = String::from("Rust");
  let say_hi = move || println!("Hi, {}", name); // name의 소유권을 가져감

  say_hi();
  // println!("{}", name); // ❌ name은 더 이상 사용 못함!
  ```

- 스레드에 클로저를 넘길 때!

  ```rs
  use std::thread;

  let msg = String::from("Hello");

  let handle = thread::spawn(move || {
      println!("{}", msg); // msg의 소유권을 가져가야 사용 가능
  });

  handle.join().unwrap();
  ```

- 비동기 코드에서 클로저가 오래 살아야 할 때!

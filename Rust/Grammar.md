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

  impl Point {
      fn p(&self) {
        println!("{}, {}", self.x, self.y)
      }
  }

  let p = Point { x: 1, y: 2 };
  println!("({}, {})", p.x, p.y);

  p.p();
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
- 기타..
  - Heap 영역은 모든 스레드가 공유

### Type(Trait)

- `String`: 소유권이 있는(owned) 동적 문자열(수정 가능) 일 때 사용
  - `"hello".to_string()`, `String::from("hello")`
- `str`: 크기 불명(길이에 대한 정보가 없음)의 문자열 슬라이스(borrowed) - 문자열 데이터 그 자체
  - `'hello'`, `'hi'`
  - 길이 정보가 없기 때문에 반드시 `&str`와 같이 사용
- `Result<T, E>`(Enum타입) - `Ok(T)`, `Err(E)`
  - `Result<u8, _>`: 성공 시 `u8`, 에러 시 `_`(알 수 없는 타입 -> 타입 추론)
  - `Result<Self, Self::Error>`
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

- `Any`: `Box<dyn Any>`처럼 어떤 타입도 허용
- `Future`: `impl Future<Output = T>`와 같이 async 클로저의 반환 타입으로 사용 - [참고](#async-클로저의-트레잇-전달)
- `Pin`: 고정 시킨 포인터, 비동기의 Future를 await하기위해 사용
- `Mutex`: Mutual Exclusion(상호 배제), 여러 스레드나 비동기 작업이 동시에 데이터를 건드리지 못하게 잠그는 도구 - [참고](#stdsyncarc---atomic-reference-counted)

#### 복수 트레잇 조합

ex) `T: Debug + PartialEq + Clone`: T는 디버그 출력 가능, 동등 비교 가능, 복사 가능함

자주 쓰이는?

- `Copy`: 값을 비트 단위로 복사 가능 (얕은 복사) - 정수, bool, 작은 크기의 복사 가능한 타입
- `Clone`: 명시적 복사 가능 (clone() 메서드 사용) - Vec, String 등
- `Debug`: 디버그용 출력 가능 ({:?} 포맷 사용 가능) - 대부분 타입
- `PartialEq`: 동등 비교 가능(값이 같은지) (==, != 연산자 사용 가능) - 대부분 타입
- `Eq`: 완전한 동등 비교 가능 (추가 제약이 있는 PartialEq 확장) - 정수, bool 등
  - `Eq`는 항상 `PartialEq`의 상위 트레잇
- `PartialOrd`: 부분 순서 비교 가능 (<, >, <=, >=) - 정수, 부동소수점, 문자열 등
- `Ord`: 완전한 순서 비교 가능 (PartialOrd 확장) - 정수, 문자열 등
  - `Ord`는 항상 `PartialOrd + Eq`를 포함
- `Default`: 기본값 생성 가능 (Default::default()) - Option, 기본 자료형 등
- `Send`: 다른 스레드로 안전하게 이동 가능 - 대부분 스레드 안전 타입
- `Sync`: 여러 스레드에서 동시에 접근 가능 - 대부분 불변 데이터
  - `&T`가 `Sync`이면 `T`는 `Send`임

#### Lifetime Specifier

> `'static`: 전역 변수와 같이 프로그램 전체 생애 동안 유효한 참조 또는 소유 값을 의미

- `&'static str`: 고정된 메시지나 변경되지 않는 데이터 일 때 사용 - 정적 메모리에 저장됨
- `&'static mut str`: `'static` 수명을 가진 가변 참조

구조체가 참조를 들고 있을 경우

```rs
pub struct LimitTracker<'a, T: 'a + Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}
```

#### [Primitive](https://doc.rust-lang.org/std/index.html#primitives)

- `i8`: -128 ~ 127
- `u8`: 0 ~ 255

타입 변환

```rs
fn main() {
    let big: i32 = 300;
    let small: Result<u8, _> = big.try_into();

    match small {
        Ok(val) => println!("변환 성공: {}", val),
        Err(e) => println!("변환 실패: {}", e),
    }
}
```

#### [Box](https://doc.rust-kr.org/ch15-00-smart-pointers.html)

> 힙 메모리를 사용하는 스마트 포인터

언제 사용하는가?

- [동적 디스패치](#동적-디스패치): 크기를 모르는 타입(dyn Trait)은 직접 사용불가하며, 이 때 Box로 감싸서 사용
- 재귀적 구조체: 자기 자신을 직접 포함할 때, Box로 감싸줌
- 큰 데이터 사용 시

사용법

- `Box<T>`: `T`를 힙에 저장할 수 있는 박스 타입
- `Box::new(value)`: value를 힙에 저장하고, 그 포인터를 스택에 저장

예시

- 동적 디스패치

  ```rs
  trait Animal {
      fn speak(&self);
  }

  struct Dog;

  impl Animal for Dog {
      fn speak(&self) {
          println!("멍멍!");
      }
  }

  let a: Box<dyn Animal> = Box::new(Dog);
  a.speak();
  ```

- 재귀적 구조체

  ```rs
  #[allow(dead_code)]
  enum List {
      Cons(i32, Box<List>),
      Nil,
  }

  use List::*;

  fn main() {
      let list = Cons(1, Box::new(Cons(2, Box::new(Nil))));

      // 열거형 패턴으로 단일 실행
      if let Cons(value, _) = list {
          println!("첫 번째 값: {}", value);
      }

      // 순회 실행
      fn print_list(list: &List) {
          match list {
              Cons(value, next) => {
                  println!("{}", value);
                  print_list(next);
              }
              Nil => {}
          }
      }
      print_list(&list);
  }
  ```

- 큰 데이터 사용 시

  ```rs
  #[derive(Debug)]
  struct BigData {
      arr: [u8; 1000], // 큰 데이터
  }

  let big = Box::new(BigData { arr: [0; 1000] });

  println!("{:?}", big.arr)

  ```

#### [Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html)

특징

- 가변 크기의 배열
- 힙(heap) 메모리에 데이터를 연속적으로 저장
- 오직 하나의 타입만 사용가능, 여러개 사용 시에는 enum사용

```rs
let mut vec = Vec::new();

vec.push(10);
vec.push(20);
vec.push(30);

println!("{:?}", vec); // [10, 20, 30]

println!("첫 번째 요소: {}", vec[0]);

for val in &vec {
    println!("값: {}", val);
}

vec.pop();

println!("{:?}", vec); // [10, 20]
```

Enum 사용 시

```rs
#[derive(Debug)]
#[allow(dead_code)]
enum MyType {
    Int(i32),
    Text(String),
    Bool(bool),
}

let mut vec: Vec<MyType> = Vec::new();

vec.push(MyType::Int(1));
vec.push(MyType::Text("hello".to_string()));
vec.push(MyType::Bool(true));

println!("{:?}", vec); // [Int(1), Text("hello"), Bool(true)]
```

#### [LinkedList](https://doc.rust-lang.org/std/collections/struct.LinkedList.html)

...

<br />

### [Macros](https://doc.rust-lang.org/std/index.html#macros)

- `println!`
  - 자리표시자 출력 형식:\
    `{variable_name}`: 변수명에 매칭되는 변수 출력
    `{}`: 일반 출력 - [Display 트레잇](https://doc.rust-lang.org/std/fmt/trait.Display.html#examples)을 구현해야함
    `{:?}`: 디버깅용 출력 - `#[derive(Debug)]` 속성을 추가해주면 사용 가능
    `{:#?}`: `{:?}`의 포맷팅 출력
- `format!`

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

여러 속성들

- `#[tokio::main]`

<br />

### [prelude](https://doc.rust-lang.org/std/prelude/index.html)

#### [std::option::Option](https://doc.rust-lang.org/std/option/enum.Option.html)

```rs
enum Option<T> {
    Some(T), // 값이 있는 경우
    None,    // 값이 없는 경우
}
```

#### [std::ptr](https://doc.rust-lang.org/std/ptr/index.html#functions)

> raw pointer를 다룰 때 사용

- `eq`: 메모리 주소 비교

<br />

## Advanced

### 비동기 처리 - async

> `cargo add tokio --features full`로 `tokio` 크레잇 설치

예제

```rs
use std::time::Duration;
use tokio::{runtime::Runtime, time::sleep};

async fn task() -> String {
    println!("start!");
    sleep(Duration::from_secs(1)).await;  // await()가 아님!
    println!("complete!");

    "작업 완료!".to_string()
}

fn main() {
    let rt = Runtime::new().unwrap();

    let result = rt.block_on(task());

    println!("main ended :: {}", result);
}
```

### 에러 핸들링

`unwrap`, `match`, `unwrap_or`, `unwrap_or_else`, `?`
=> `Option<T>`(Some, None) 또는 `Result<T, E>`(Ok, Err)와 함께 사용

- `unwrap`: 실패(Err 또는 None)일 경우 panic 발생. 즉, 프로그램이 종료
- `?`: 실패(Err 또는 None) 시, 조기 리턴하며 panic이 발생하지 않고 에러를 전파

<br />

- `Result`와 `Option` 공통
  - `map`: `Ok`에 대해 변환
  - `and_then`
  - `or_else`
- Result
  - `map_err`: `Err`인 경우, 새로운 `Result<T, E2>` 반환
- Option
  - `ok_or`: `None`인 경우, 지정한 에러로 `Result<T, E>` 반환

<br />

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

`None`이면 즉시 리턴

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

### 소유권

#### move - Closure(익명 함수)에서만 사용 가능

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

#### as_ref

소유권 유지를 위해 사용

```rs
fn main() {
    let opt: Option<String> = Some("hello".to_string());
    let opt_ref: Option<&String> = opt.as_ref();

    if let Some(val) = opt_ref {
        println!("if :: {}", val);
    } else {
        println!("if :: 없음");
    }

    match opt_ref {
        Some(val) => println!("match :: {}", val),
        None => println!("match :: 없음"),
    }

    println!(
        "{}",
        opt_ref.unwrap_or(&"unwrap_or :: 없음 :: 기본 값".to_string())
    );
}
```

구조체에서 값을 참조 시에 사용

```rs
struct Profile {
    nickname: Option<String>,
}

struct User {
    profile: Option<Profile>,
}

fn get_uppercase_nickname(user: &User) -> Option<String> {
    let nickname = user
        .profile.as_ref()?           // Option<&Profile>
        .nickname.as_ref()?          // Option<&String>
        .to_uppercase();             // String
    Some(nickname)
}

fn main() {
    let user = User {
        profile: Some(Profile {
            nickname: Some("rustacean".to_string()),
        }),
    };
    println!("{:?}", get_uppercase_nickname(&user));  // Some("RUSTACEAN")

    let user2 = User { profile: None };
    println!("{:?}", get_uppercase_nickname(&user2));
}
```

<br />

### 동적 디스패치

> 공통된 트레잇을 구현한 여러 타입을 처리하기 위함

- 정적 디스패치: 컴파일 타임에 결정, 인라인 최적화 => 빠름, 바이너리 커질 가능성 있음
- 동적 디스패치: 런타임에 결정, 단일 함수 코드로 여러 타입 처리, 가상 메서드 테이블로 호출 => 비교적 느림, 유연

키워드: `dyn`
사용법: `&dyn Trait` 또는 `Box<dyn Trait>`로 사용

```rs
trait Animal {
    fn speak(&self);
}

struct Dog;
struct Cat;

impl Animal for Dog {
    fn speak(&self) {
        println!("멍멍!");
    }
}

impl Animal for Cat {
    fn speak(&self) {
        println!("야옹~");
    }
}

let dog = Dog;
let cat = Cat;

let animals: Vec<&dyn Animal> = vec![&dog, &cat];

for animal in animals {
    animal.speak(); // 런타임에 어떤 speak()를 호출할지 결정됨
}

// 또는 (&Dog).speak(); 처럼도 사용 가능
```

<br />

### clone 지양

#### std::rc::Rc - Reference Counted

- 단일 스레드 환경
- 다중 소유권을 지원 - 동일한 데이터에 대한 소유권을 공유
- Deref Trait를 기본적으로 포함하여 자동 역참조

```rs
async fn main() {
    let s1 = Rc::new(String::from("hello"));

    let s2 = Rc::clone(&s1);  // Rc::clone가 s1의 rc참조 카운터를 늘림(rc참조 포인터를 복사)
    let s3 = Rc::clone(&s1);
}
```

#### std::sync::Arc - Atomic Reference Counted

- 멀티 스레드 환경
- 여러 스레드에서 동시에 참조 카운트를 수정해도 안전 - `Arc::strong_count`

값을 참조시

```rs
use std::{sync::Arc, thread};

#[tokio::main]
async fn main() {
    let s1 = Arc::new(String::from("hello"));

    for i in 0..2 {
        let s1_moved = Arc::clone(&s1);

        let handle = thread::Builder::new()
            .name(format!("thread-{}", i)) // 스레드에 이름 지정
            .spawn(move || {
                println!("thread-{} :: {:?}", i, s1_moved);
            })
            .unwrap();

        handle.join().unwrap();
    }
}
```

값을 수정시

```rs
use std::{sync::{Arc, Mutex}, thread};

fn main() {
    let s1 = Arc::new(Mutex::new(String::from("hello")));   // Mutex가 내부 가변성을 제공해 mut없이 변경 가능

    for i in 0..2 {
        let s1_moved = Arc::clone(&s1);

        let handle = thread::Builder::new()
            .name(format!("thread-{}", i))
            .spawn(move || {
                let mut data = s1_moved.lock().unwrap();
                data.push_str(&format!(" from thread-{}", i));
                println!("thread-{} :: {:?}", i, data);
            })
            .unwrap();

        handle.join().unwrap();
    }
}
```

```rs
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    let counter = Arc::new(Mutex::new(0));    // Mutex가 내부 가변성을 제공해 mut없이 변경 가능

    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);

        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();
            *num += 1;

            std::mem::drop(num);  // 잠금 해제 기능, 생략 가능, 스코프 벗어날 경우 자동 잠금 해제됨
        });

        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("최종 값: {}", *counter.lock().unwrap());
}
```

#### std::cell::RefCell

- 단일 소유권만 지원
- 단일 스레드 환경
- 내부 가변성 패턴: 불변 참조(외부에서는 불변 속성)를 사용하면서도 값을 수정할 수 있음(unsafe)
- 컴파일이 아님 런타임에서 체크 - 실행 오류시, 패닉이 발생하며 종료

```rs
use std::cell::RefCell;

pub trait Messenger {
    fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: 'a + Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(messenger: &T, max: usize) -> LimitTracker<T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

    pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max = self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger.send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
                .send("Urgent warning: You've used up over 90% of your quota!");
        } else if percentage_of_max >= 0.7 {
            self.messenger
                .send("Warning: You've used up over 75% of your quota!");
        }
    }
}

#[derive(Debug)]
struct MockMessenger {
    // sent_message: Vec<String>,
    sent_message: RefCell<Vec<String>>,
}

impl MockMessenger {
    fn new() -> MockMessenger {
        MockMessenger {
            // sent_message: vec![],
            sent_message: RefCell::new(vec![]),
        }
    }
}

impl Messenger for MockMessenger {
    fn send(&self, message: &str) {
        // self.sent_message.push(String::from(message));  -> 불변참조 self의 필드에 값을 추가 시 오류!
        self.sent_message.borrow_mut().push(String::from(message));
    }
}

fn main() {
    let mock_messenger = MockMessenger::new();
    let mut limit_tracker = LimitTracker::new(&mock_messenger, 100);

    limit_tracker.set_value(80);

    // assert_eq!(mock_messenger.sent_message.len(), 1);
    assert_eq!(mock_messenger.sent_message.borrow().len(), 1);

    println!("{:#?}", mock_messenger);
}
```

##### `Rc<T>`와 `RefCell<T>`의 조합

> 보편적인 방법

- 다중 소유권과 내부 가변성을 가짐

```rs
#[derive(Debug)]
enum List {
    Cons(Rc<RefCell<i32>>, Rc<List>),
    Nil,
}

use List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

fn main() {
    let value = Rc::new(RefCell::new(5));

    let a = Rc::new(Cons(Rc::clone(&value), Rc::new(Nil)));
    let b = Cons(Rc::new(RefCell::new(6)), Rc::clone(&a));
    let c = Cons(Rc::new(RefCell::new(10)), Rc::clone(&a));

    *value.borrow_mut() += 10;

    println!("a after = {:?}", a);
    println!("b after = {:?}", b);
    println!("c after = {:?}", c);
}
```

#### std::rc::Weak

- 소유는 하지않고, 참조만 가능

언제 사용하나?

- 순환 참조 방지: Rc 타입 간에 순환 참조가 발생할 경우, 참조 카운트가 0이 되지 않아서 메모리 누수 발생

```rs
use std::{
    cell::RefCell,
    rc::{Rc, Weak},
};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}

fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

    *leaf.parent.borrow_mut() = Rc::downgrade(&branch);   // Rc를 Weak으로 변환 (약한 참조 생성) - 참조카운트 유지

    println!("leaf parent :: {:#?}", leaf.parent.borrow().upgrade());   // Weak을 Rc(살아있을 경우만) 또는 None 반환  - 참조카운트 증가(살아있을 경우만)
}
```

#### std::borrow::Cow - Clone On Write

- 읽을 때는 참조하고, 쓸 때만 복사해서 소유(clone), 또는 원본 사용
- `Cow::from`: 참조값 전달시 `Cow::Borrowed`, 소유권을 넘길 시에는 `Cow::Owned`
- `Cow::to_mut`: `Cow::Borrowed`이면 복사하여 소유, `Cow::Owned`이면 원본 사용

```rs
use std::borrow::Cow;

fn abs_all(input: &mut Cow<[i32]>) {
    for i in 0..input.len() {
        let v = input[i];
        if v < 0 {
            input.to_mut()[i] = -v; // 이 시점에 clone 발생
        }
    }
}

fn main() {
    let slice: [i32; 3] = [-1, 2, -3];

    let mut input1: Cow<[i32]> = Cow::Borrowed(&slice);
    let mut input2 = Cow::from(vec![-1, 0, 1]);

    abs_all(&mut input1);
    abs_all(&mut input2);

    println!("원본: {:?}", slice); // ➤ [-1, 2, -3] (변경 안 됨)
    println!("복사본: {:?}", input1); // ➤ [1, 2, 3] (복사되어 복사본 바뀜)
    println!("소유권 전달: {:?}", input2); // ➤ [1, 0, 1] (소유권 이전하여 원본 바뀜)
}
```

<br />

## PBL

### 인스턴스 비교

`==`(PartialEq)를 사용 시, 내부 값을 비교

> `Eq`: 완전한 동치성 비교시 사용(표시),

```rs
#[derive(PartialEq)]
struct Dog;

let dog1 = Dog;
let dog2 = Dog;

println!("{}", dog1 == dog2); // true
```

메모리 주소 비교

```rs
use std::ptr;

let dog1 = Dog;
let dog2 = Dog;

let same = ptr::eq(&dog1, &dog2);
println!("같은 인스턴스인가? {}", same); // false
```

### 일반 함수/클로저의 트레잇 전달

기본적인 사용

```rs
struct MyStruct<F>
where
    F: Fn(i32) -> i32,
{
    func: F,
}

fn main() {
    let s = MyStruct { func: |x| x + 10 };

    println!("{}", (s.func)(5));
}
```

Box와 함께 사용시

```rs
struct MyStruct {
    func: Box<dyn Fn(i32) -> i32>,
}

fn main() {
    let s = MyStruct {
        func: Box::new(|x| x + 10),
    };

    println!("{}", (s.func)(5));
}
```

기타 예제

```rs
struct Adder<F>
where
    F: Fn(i32, i32) -> i32,
{
    op: F,
}

impl<F> Adder<F>
where
    F: Fn(i32, i32) -> i32,
{
    fn new(op: F) -> Self {
        Self { op }
    }

    fn calc(&self, a: i32, b: i32) -> i32 {
        (self.op)(a, b)
    }
}

fn main() {
    let add = Adder::new(|x, y| x + y);
    println!("{}", add.calc(3, 4)); // 7
}
```

### async 함수/클로저의 트레잇 전달

async 함수/클로저는 반환 타입이 `impl Future<Output = T>`임

기본적인 사용

```rs
use std::future::Future;
use std::time::Duration;
use tokio::runtime::Runtime;
use tokio::time::sleep;

async fn task() -> String {
    println!("start!");
    sleep(Duration::from_secs(1)).await;
    println!("completed!");

    "result".to_string()
}

async fn call<F, Fut>(f: F) -> String
where
    F: Fn() -> Fut,
    Fut: Future<Output = String>,
{
    f().await
}

fn main() {
    let rt = Runtime::new().unwrap();

    let result1 = rt.block_on(call(task));
    println!("{}", result1);

    let result2 = rt.block_on(call(|| async {
        println!("closure task start");
        sleep(Duration::from_secs(1)).await;
        println!("closure task completed");

        "result2".to_string()
    }));
    println!("{}", result2);
}
```

Pin과 Box와 함께 사용시

```rs
use std::future::Future;
use std::pin::Pin;
use std::time::Duration;
use tokio::runtime::Runtime;
use tokio::time::sleep;

async fn task() -> String {
    println!("start!");
    sleep(Duration::from_secs(1)).await;
    println!("completed!");

    "result".to_string()
}

async fn call(f: impl Fn() -> Pin<Box<dyn Future<Output = String>>>) -> String {
    f().await
}

fn main() {
    let rt = Runtime::new().unwrap();

    let result1 = rt.block_on(call(|| Box::pin(task())));
    println!("{}", result1);

    let result2 = rt.block_on(call(|| {
        Box::pin(async {
            println!("closure task start");
            sleep(Duration::from_secs(1)).await;
            println!("closure task completed");

            "result2".to_string()
        })
    }));
    println!("{}", result2);
}
```

트레잇의 async 함수 선언/사용시

> `cargo add async_trait`로 `async_trait` 크레잇 설치

```rs
use async_trait::async_trait;
use tokio::runtime::Runtime;

#[async_trait]
trait MyTrait {
    async fn call(&self) -> String;
}
struct MyStruct;

#[async_trait]
impl MyTrait for MyStruct {
    async fn call(&self) -> String {
        println!("async trait method");

        "result".to_string()
    }
}

fn main() {
    let rt = Runtime::new().unwrap();

    let result = rt.block_on(MyStruct.call());

    println!("main ended :: {}", result);
}
```

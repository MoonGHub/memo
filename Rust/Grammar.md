# Rust - Grammar

## Basic

### 기본 지식

- `Trait`: Interface 와 비슷하지만 다름

  ```rs
  trait Greet {
      fn say_hello1(&self);

      fn say_hello2(&self) {
          println!("Hello!2")
      }
  }

  struct Person;

  impl Greet for Person {
      fn say_hello1(&self) {
          println!("Hello!1");
      }
  }

  Person.say_hello1();
  Person.say_hello2();
  ```

- `Struct`: 상속 없는 클래스 느낌

  ```rs
  struct Point1 {
      x: i32,
      y: i32,
  } // 일반 구조체
  struct Point2(i32, i32, i32); // 튜플 구조체

  impl Point1 {
      fn p(&self) {
          println!("{}, {}", self.x, self.y)
      }
  }

  let p1 = Point1 { x: 1, y: 2 };
  println!("({}, {})", p1.x, p1.y);
  p1.p();

  let p2 = Point2(1, 2, 3);
  println!("{}, {}, {}", p2.0, p2.1, p2.2);
  ```

  ```rs
  #[derive(Default, Debug)]
  struct User {
      active: bool,
      nickname: String,
  }

  impl User {
      fn new() -> Self {
          Self {
              ..Default::default()
          }
      }
  }

  fn main() {
      let user1 = User {
          active: true,
          ..User::default() // 스프레드는 마지막에 위치해야 함
      };

      let user2 = User::new();

      println!("{:?}, {:?}", user1, user2);
  }
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

- `Enum`: Algebraic data type - 서로 다른 variant(타입)들의 묶음, 어떤 종류의 타입도 담을 수 있음

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
      _ => println!("Not going up"),  // 포괄적인 갈래는 마지막에 위치 할 것
  }
  ```

  ```rs
  #[derive(Debug)]
  enum IpAddr {
      V4(u8, u8, u8, u8),
      V6(String),
      Other { name: String },
  }

  impl IpAddr {
      fn p(&self) {
          println!("{:?}", self);
      }
  }

  fn main() {
      let home = IpAddr::V4(127, 0, 0, 1);
      let loopback = IpAddr::V6(String::from("::1"));
      let other = IpAddr::Other {
          name: String::from("good"),
      };

      home.p();
      loopback.p();
      other.p();
  }
  ```

- `Tuple`: 튜플

  ```rs
  fn main() {
      let rect1 = (30, 50);

      println!("{}", area(rect1));
  }

  fn area(dimensions: (u32, u32)) -> u32 {
      dimensions.0 * dimensions.1
  }
  ```

<br />

#### 문법

- if 조건식은 무조건 `bool`타입이어야 함

  ```rs
  let condition = true;
  let number = if condition { 5 } else { 6 };

  println!("The value of number is: {number}");
  ```

- 범위 표현식

  - `1..100	`: (범위표현식) 1이상 100미만 - 100 미포함
  - `1..=100`: (범위표현식) 1이상 1이하 - 100 포함

    ```rs
    fn main() {
        let a: Vec<u32> = (1..=100).collect();

        println!("{:?}", a);
    }
    ```

  - `&s[..2]`또는 `&s[..]`와 같이도 사용

- 반복문: `loop`, `while`, `for`

  ```rs
  let mut counter = 0;

  let result = loop {
      counter += 1;

      if counter == 10 {
          break counter * 2;  // 이 값을 반환하며 반복문을 빠져나감
      }
  };

  println!("The result is {result}");
  ```

  ```rs
  let mut count = 0;
  'counting_up: loop {
      println!("count = {count}");
      let mut remaining = 10;

      loop {
          println!("remaining = {remaining}");
          if remaining == 9 {
              break;
          }
          if count == 2 {
              break 'counting_up;
          }
          remaining -= 1;
      }

      count += 1;
  }
  println!("End count = {count}");
  ```

  ```rs
  let mut number = 3;

  while number != 0 {
      println!("{number}!");

      number -= 1;
  }

  println!("LIFTOFF!!!");
  ```

  ```rs
  for number in (1..4).rev() {
      println!("{number}!");
  }
  ```

  ```rs
  fn main() {
      let mut str = String::from("test goood");

      let word = first_word(&str); // 불변 참조

      str.clear(); // 가변 참조로 에러! - 하지만 word가 사용되지 않으면 word는 없는 것으로 취급하여 허용됨

      // println!("the first word is: {}", word); // word 사용시, 가변참조 str.clear(); 에서 에러 발생
  }

  fn first_word(s: &String) -> &str { // 라이프타임 생략 규칙 1~2에 해당되어 추론 가능
      let bytes = s.as_bytes();

      for (i, &item) in bytes.iter().enumerate() {
          if item == b' ' {
              return &s[0..i];
          }
      }

      &s[..]
  }
  ```

#### 알뜰잡식

- 메서드: 메서드는 impl 블록에서 정의되는 함수
- 캡처: 클로저가 외부 변수에 접근할 때 그 값을 내부에서 사용하기 위해 가져오는 것
- Heap 영역(런타임에 동적 메모리를 할당)은 모든 스레드가 공유
- 정수형 등 컴파일 타임에 크기가 고정되는 타입은 모두 스택에 저장
- `"hello"`과 같은 문자열 리터럴은 바이너리 내(읽기 전용 메모리 영역 - static 영역)에 저장되며 `&'static str`타입으로 사용
- 스택에 저장되는 값은 빠른 복사본 생성으로 계속 사용 가능
- 스코프 밖으로 벗어났을 때 특정 동작이 요구되는 타입(Drop 등)에 Copy 어노테이션 추가 불가
- 대여(borrow): `&`참조자로 스택에 저장된 값(힙을 가르키는 - 포인터 + 길이 + 용량 등)을 참조(가르키는)하겠다는 값을 생성, 소유하지 않으니 drop도 없음
- `*`는 역참조

  ```rs
  let mut x = 5;  // x는 포인터가 아님, 값 5를 저장한 스택 메모리 공간의 이름

  x += 2; // 따라서 바로 수정 가능
  println!("{}", x); // 7

  let y = &mut x; // y는 x의 주소를 저장하는 참조자
  *y += 1;  // 따라서 역참조로 수정

  println!("{}", x); // 8
  ```

- **동일 스코프에서 어떤 값에 대한 불변 참조자 또는 가변 참조자가 존재시, 추가적인 가변 참조자 `&mut`를 만들지 못함**
  - 여러 개의 불변 참조가 생성 가능, 가변 참조자는 하나만 생성 가능
- 사용되지 않는 변수에 대해서는 최적화를 통해 "사실상 없는 것처럼" 취급
- 슬라이스 == 연속된 데이터, 슬라이스는 참조형 타입(&)로만 사용
- 백트레이스 (backtrace): 어떤 지점에 도달하기까지 호출한 모든 함수의 목록
- mangle: minify + uglify
- `&self`: impl 구현체 함수의 첫 파라미터로 쓰며 사용(명시) 시 인스턴스의 함수로 호출, `&self`가 없으면 정적 메서드로 인스턴스 생성없이 바로 호출
- `Self`: 해당 impl 블록의 별칭
- 댕글링 참조 (dangling reference): 이미 메모리에서 사라진 값을 가리키는 참조

#### 프로젝트(패키지, 크레이트, 모듈) 관리

- 패키지: Cargo.toml이 포함된 하나 이상의 크레이트로 구성된 번들 - 크레이트를 빌드하고, 테스트하고, 공유하는 데 사용하는 카고 기능
  - 라이브러리 크레이트(lib.rs)는 하나만 작성 가능
  - `cargo new 경로 --lib`로 만든건 라이브러리 패키지이자 크레잇 - 여러개 가능(Cargo.toml를 포함하고있는 패키지임으로)
- 크레이트: 라이브러리나 실행 가능한 모듈로 구성된 트리 구조

  - 바이너리 크레이트: 실행 가능한 실행파일로 컴파일할 수 있는 프로그램
    - 기본적으로 src/main.rs가 크레이트 루트
    - src/bin안에 둘 시, 여러 바이너리 크레이트를 패키지에 포함할 수 있음
  - 라이브러리 크레이트: main 함수를 가지고 있지 않고 실행파일 형태로 컴파일되지 않음
    - 기본적으로 src/lib.rs가 크레이트 루트
  - 바이너리(src/main.rs)와 라이브러리(src/lib.rs)가 같이 있는 경우, 해당 패키지의 이름을 경로의 시작점으로 라이브러리 크레이트를 사용

    ```rs
    // 패키지 이름이 hello_app인 경우

    // src/lib.rs
    pub fn greet(name: &str) -> String {
        format!("Hello, {}!", name)
    }

    // src/main.rs
    fn main() {
        // 라이브러리 크레이트를 외부 크레이트처럼 패키지 이름을 사용하여 호출
        println!("{}", hello_app::greet("Rust"));
    }
    ```

- 모듈과 use: 구조, 스코프를 제어하고, 조직 세부 경로를 감추는 데 사용
- 경로: 구조체, 함수, 모듈 등의 이름을 지정
  - `crate::`: 절대경로로 루트 시작점
  - `super::`: 부모 모듈의 컨텍스트를 가르키는 상대 경로
- `use`는 이미 등록된 모듈이나 항목을 현재 스코프로 가져옴
  - 키워드와 경로를 함께 사용하여 해당 경로를 단축
  - `use std::io::{self, Write};`
  - `use std::collections::*;`
- `mod`는 모듈을 정의
  - 파일을 로드 - 모듈 파일사용 시, 선언된 위치의 경로를 사용하여 `mod`로 프로젝트의 일부란 것을 명시해줘야 함
  - 새로운 스코프를 만듬 -> `mod`내에서 새로 `use`를 사용해야 함

#### 접근 제어자

기본적으로 `private` 접근 제어자를 가짐

- `pub`: 어디서든 접근 가능 (현재 크레이트 외부도 가능)
- `pub(crate)`: 크레이트 내부에서만 접근 가능
- `pub(super)`: 바로 위 모듈에서만 접근 가능
- `pub(in path)`: `pub(in crate::a)` - a 모듈 내에서만 접근 가능

```rs
mod front_of_house {  // eat_at_restaurant와 front_of_house는 동일한 모듈 내에 정의(형제 관계)되어 있어 바로 사용 가능
    pub mod hosting { // 모듈의 상위에서 아래로 접근하기 위해 pub 명시 필요
        pub fn add_to_waitlist() {} // 모듈의 상위에서 아래로 접근하기 위해 pub 명시 필요, 반대로 아래에서 위로의 접근으로는 언제든 가능
    }
}

pub fn eat_at_restaurant() {
    // 절대 경로
    crate::front_of_house::hosting::add_to_waitlist();

    // 상대 경로
    front_of_house::hosting::add_to_waitlist();
}
```

- 구조체(struct) 내에 비공개 필드가 존재 할 경우, 인스턴스를 생성하고 공개(반환)하는 연관 함수가 필요 - 비공개 필드에 값을 지정할 방법이 없기 때문
- 열거형(enum)은 공개로 지정할 경우, 모든 배리언트가 공개

#### 제네릭(Generic)

```rs
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

```rs
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

<br />

### [Crates](https://crates.io/)

- `rand`
- `strum`
- `strum_macros`
- `tokio`

<br />

### Type, Trait

- Trait: 메서드 시그니처를 그룹화하여 특정 목적을 달성하는 데 필요한 일련의 동작을 정의
- Trait를 구현한 구조체를 사용할 때는, 트레이트도 사용하는 스코프내로 가져와야함
- 외부 타입에 외부 트레이트 구현은 못함, 하나 이상이 자신의 것이어야 함(내 타입 + 외부 트레잇 또는 외부타입 + 내 트레잇)

  ```rs
  use std::fmt;

  struct MyType;

  // 외부 트레잇 + 내 타입 => 가능
  impl fmt::Display for MyType {
      fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
          write!(f, "MyType입니다!")
      }
  }
  ```

- `스칼라 (scalar)`: 정수, 부동 소수점 숫자, 부울린, 문자

#### Lifetime Specifier

> 라이프타임은 제네릭의 일종으로, 어떤 참조자가 필요한 기간 동안 유효함을 보장하여 댕글링 참조를 방지

- `'`(어퍼스트로피)로 시작d
- `'static`: 정적 라이프타임 - 전역 변수와 같이 프로그램 전체 생애 동안 유효한 참조 또는 소유 값을 의미
- `&'static str`: 고정된 메시지나 변경되지 않는 데이터 일 때 사용 - 정적 메모리에 저장됨
- `&'static mut str`: `'static` 수명을 가진 가변 참조
- 참조자를 반환하는 함수를 작성할 때는 반환 타입의 라이프타임 매개변수가 함수 매개변수 중 하나와 일치해야 함

**라이프타임 생략 규칙** - 아래 절차(1~3)로 입력과 출력 라이프타임이 추론되지 않는 경우 에러

1. 참조자인 매개변수 각각에게 라이프타임 매개변수를 할당
2. 입력 라이프타임 매개변수가 딱 하나라면, 해당 라이프타임이 모든 출력 라이프타임에 대입
3. 입력 라이프타임 매개변수가 여러 개인데, 그중 하나가 &self나 &mut self라면,\
   즉 메서드라면 self의 라이프타임이 모든 출력 라이프타임 매개변수에 대입

<br />

구조체가 참조를 들고 있을 경우, 라이프타임 명시

```rs
#[derive(Debug)]
pub struct Test<'a> {
    str: &'a str,
}

fn main() {
    println!("{:?}", Test { str: "good" });
}
```

```rs
pub struct LimitTracker<'a, T: 'a + Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}
```

```rs
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

#### [Primitive](https://doc.rust-lang.org/std/index.html#primitives)

- 숫자 기본 설정 타입: i32, f64
  - 정수 오버플로우 시, 디버그는 패닉, 릴리즈는 2의 보수 감싸기
  - 오버플로우 대응: `wrapping_*`, `checked_*`, `overflowing_*`, `saturating_*`
- `isize`, `usize`: 컴퓨터 환경이 64-bit 아키텍처이면 64비트를, 32-bit 아키텍처이면 32비트
- `[]`배열은 갯수가 고정되어 있음, 갯수가 변할 시 벡터를 사용

##### 문자열

- `String`: 소유권이 있는(owned) 동적 문자열(수정 가능) 일 때 사용
  - `"hello".to_string()`, `String::from("hello")`
- `str`: 크기 불명(길이에 대한 정보가 없음)의 문자열 슬라이스 - 문자열 데이터의 연속된 데이터 그 자체를 의미
  - `'hello'`, `'hi'` 와 같은 값
  - 따라서, 길이 정보가 없기 때문에 반드시 `&str`와 같은 타입으로 사용됨 - 길이 정보 포함
- 문자열 리터럴은 큰 따옴표 사용되며 `&'static str`타입으로 `UTF-8`형식(u8<sub>1바이트</sub>의 배열)으로 인코딩되어 저장
- `String`도 `UTF-8`형식(`Vec<u8>`)으로 인코딩되어 저장
- `UTF-8`은 1바이트에서 4바이트의 가변 길이로, 저장되는 문자에 따라 여러 인덱스(1개~4개) 범위를 차지
- `char`타입(4byte)은 작은 따옴표를 사용

```rs
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2;  // 이후 s1은 소유권 이전으로 사용 불가

println!("{}", s3); // Hello, world!
```

가변 길이로 인해 인덱스로 문자열 슬라이스 접근 대신 `chars` 활용

```rs
// 실제 길이 값(u8의 갯수)은 24
for c in "Здравствуйте".chars() {
    println!("{c}");
}
```

##### 타입 변환

- `parse`: 문자열을 숫자 등으로 변환

  ```rs
  let n1 = "3.14".parse::<f64>().unwrap(); // turbofish 문법 사용

  let n2: f64 = "3.14".parse().unwrap();

  println!("{}, {}", n1, n2);

  let result = "abc".parse::<i32>();
  match result {
      Ok(n) => println!("숫자: {}", n),
      Err(e) => println!("에러 발생: {}", e),
  }
  ```

- `try_into`

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

- `try_from`

  ```rs
  use std::convert::TryFrom;

  #[derive(Debug)]
  struct Age(u8);

  impl TryFrom<i32> for Age {
      type Error = String;

      fn try_from(value: i32) -> Result<Self, Self::Error> {
          if value >= 0 && value <= 130 {
              Ok(Age(value as u8))
          } else {
              Err("나이 범위 초과".into())
          }
      }
  }

  fn main() {
      let age: Result<Age, _> = 150.try_into();

      println!("{:?}", age); // Err("나이 범위 초과")
  }
  ```

##### 기타 예제

```rs
// 튜플
let tup = (500, 6.4, 1);
let (x, y, z) = tup;

println!("{x}, {y}, {z}, {}", tup.0);

// 배열
let a = [1, 2, 3, 4, 5];
let first = a[0];
```

#### 여러 Trait

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
  - 정수형 타입은 `0`, `bool` 타입은 `false`, `&str`타입은 `""`의 기본값으로 초기값 생성
- `Send`: 다른 스레드로 안전하게 이동 가능 - 대부분 스레드 안전 타입
- `Sync`: 여러 스레드에서 동시에 접근 가능 - 대부분 불변 데이터
  - `&T`가 `Sync`이면 `T`는 `Send`임
- `T: Debug + PartialEq + Clone`: 복수 트레잇 조합 - T는 디버그 출력 가능, 동등 비교 가능, 복사 가능함
  - `pub fn notify(item: &(impl Summary + Display)) {`
  - `pub fn notify<T: Summary + Display>(item: &T) {`
- `std::cmp::Ordering`: cmp의 결과 타입으로 사용
- `std::collections::HashMap` - O(1)
- [std::ptr](https://doc.rust-lang.org/std/ptr/index.html#functions): raw pointer를 다룰 때 사용
  - `eq`: 메모리 주소 비교

##### Result

- `Result<T, E>`(Enum타입) - `Ok(T)`, `Err(E)`
- `Result<u8, _>`: 성공 시 `u8`, 에러 시 `_`(알 수 없는 타입 -> 타입 추론)
- `Result<Self, Self::Error>`

  ```rs
  use std::str::FromStr;

  #[derive(Debug)]
  struct MyNumber(i32);

  impl FromStr for MyNumber {
      type Err = String;

      fn from_str(s: &str) -> Result<Self, Self::Err> {
          match s.parse::<i32>() {
              Ok(n) => Ok(MyNumber(n)),
              Err(_) => Err("정수가 아닙니다".to_string()),
          }
      }
  }

  let mn = MyNumber::from_str("good");
  match mn {
      Ok(mn) => println!("{:?}", mn),
      Err(err) => println!("{err}"),
  }
  ```

##### std::collections::HashMap

- 순서 보장 못함

```rs
use std::collections::HashMap;

let mut scores = HashMap::new();

scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);

let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0); // copied를 통해 Option<&V>가 아닌 Option<V>를 얻음

for (key, value) in &scores {
    println!("{key}: {value}");
}
```

- 키가 없을 때만 키와 값 추가하기

  ```rs
  use std::collections::HashMap;

  let mut scores = HashMap::new();
  scores.insert(String::from("Blue"), 10);

  scores.entry(String::from("Yellow")).or_insert(50); // or_insert는 키에 대한 가변 참조자(&mut V)를 반환
  scores.entry(String::from("Blue")).or_insert(50);

  println!("{:?}", scores);
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
- 오직 하나의 타입만 사용가능, 여러개 사용 시에는 enum과 함께 사용

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

let mut v = vec![100, 32, 57];
for i in &mut v {
    *i += 50;
}
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

매크로 활용

```rs
let v = vec![1, 2, 3, 4, 5];

let third: &i32 = &v[2];
// let third: i32 = (&v)[2]; // 의 경우, 복사본이므로 원본 벡터와 연결이 되지 않음
println!("The third element is {third}");

let third: Option<&i32> = v.get(2); // get은 Option<T>를 반환 -> 범위 밖이어도 패닉이 발생하지 않음
match third {
    Some(third) => println!("The third element is {third}"),
    None => println!("There is no third element."),
}
```

<br />

#### [역참조 강제 변환 (deref coercions)](#역참조-강제-변환-deref-coercions-1)

### [Macros](https://doc.rust-lang.org/std/index.html#macros)

- `println!`
  - 소유권을 가져가지 않음
  - 자리표시자 출력 형식:\
    `{variable_name}`: 변수명에 매칭되는 변수 출력
    `{}`: 일반 출력 - [Display 트레잇](https://doc.rust-lang.org/std/fmt/trait.Display.html#examples)을 구현해야함
    `{:?}`: 디버깅용 출력 - `#[derive(Debug)]` 속성을 추가해주면 사용 가능
    `{:#?}`: `{:?}`의 포맷팅 출력
- `format!`
  - 소유권을 가져가지 않음
- `dbg!`: 디버그 출력을 하며 결과값을 그대로 반환함, 넘기는 값이 소유권을 가지는 타입이면, 그 소유권이 dbg!로 이동
- `panic!`: 복구 불가능한 에러 처리
- `assert_eq!`: 유닛 테스트 또는 디버깅에 사용, 설정한 두 값이 다르면 panic 발생

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

### [prelude](https://doc.rust-lang.org/std/prelude/index.html) - 프렐루드

#### [std::result::Result](https://doc.rust-lang.org/std/result/enum.Result.html)

#### [std::option::Option](https://doc.rust-lang.org/std/option/enum.Option.html)

```rs
enum Option<T> {
    Some(T), // 값이 있는 경우
    None,    // 값이 없는 경우
}
```

예제

```rs
fn main() {
    let some_number = Some(10).unwrap_or(1);
    let none_number = None.unwrap_or(1);

    println!("{}, {}", some_number * 100, none_number * 100);
}
```

---

## Advanced

### 역참조 강제 변환 (deref coercions)

내부적으로 Deref를 구현하는 Trait

- `String`: String은 str의 Wrapper이며(실제로는 `Vec<u8>`), &str으로 변환됨

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

#### 복구 불가능한 에러

사용자를 위험에 빠뜨릴 수 있는 연산을 수행할 때 의도적인 `panic!`을 사용

> 기본적으로 `panic!` 발생 시, unwinding 실행 - 데이터/메모리 정리

`unwinding`를 하지않고, 바로 그만두기 방식

```toml
[profile.release]
panic = 'abort'
```

예제

```rs
use std::fs::File;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file: {:?}", error),
    };
}
```

#### 복구 가능한 에러

```rs
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error);
            }
        },
    };
}
```

위와 동일 기능

```rs
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            File::create("hello.txt").unwrap_or_else(|error| {
                panic!("Problem creating the file: {:?}", error);
            })
        } else {
            panic!("Problem opening the file: {:?}", error);
        }
    });
}
```

##### 체이닝 함수로 제어

`unwrap`, `match`, `unwrap_or`, `unwrap_or_else`, `?`
=> `Option<T>`(Some, None) 또는 `Result<T, E>`(Ok, Err)와 함께 사용

- `unwrap`: 실패(Err 또는 None)일 경우 panic 발생. 즉, 프로그램이 종료
- `unwrap_or`: 디폴트 값 설정
- `?`: 실패(Err 또는 None) 시, 해당 실패값으로 즉시 조기 리턴하며 panic이 발생하지 않음 - 에러 전파

<br />

- `Result`와 `Option` 공통
  - `expect`: 에러 발생 시 panic!의 기본메세지 대신 설정한 메세지를 표시하며 패닉을 발생, 또는 정상값 반환
  - `map`: `Ok`또는 `Some`에 대해 변환 후, 새로운 `Result`또는 `Option` 반환
  - `and_then`
  - `or_else`
- Result
  - `ok`: `Option<T>`로 반환되며 `Err`인 경우는 `None`
  - `map_err`: `Err`에 대해 변환 후, 새로운 `Result` 반환
- Option
  - `ok_or`: 지정한 에러로 `Result<T, E>` 반환

<br />

`Err` 배리언트가 나오지 않는 상황에서는 아래 처럼 작성하여도 무방

```rs
use std::net::IpAddr;

let home: IpAddr = "127.0.0.1"
    .parse()
    .expect("Never :: Hardcoded IP address should be valid");
```

###### match

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

###### unwrap_or - 기본값 반환

```rs
fn get_number() -> Option<i32> {
    None
}

let num = get_number().unwrap_or(42); // 실패 시 기본값 42
println!("숫자: {}", num);
```

###### unwrap_or_else - 기본값 함수 호출

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

###### ?

- `None` 또는 `Err`이면 즉시 리턴하며 에러를 전파
- Result, Option 혹은 FromResidual을 구현한 타입을 반환하는 함수에서만 사용 가능

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

```rs
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username = String::new();

    File::open("hello.txt")?.read_to_string(&mut username)?;

    Ok(username)

    // 위는 아래와 동일
    // fs::read_to_string("hello.txt")
}

println!("{:?}", read_username_from_file());
```

<br />

### 소유권

- 한 값의 소유자는 동시에 여럿 존재할 수 없음
- 스코프 밖으로 벗어날 때, 값은 버려짐 - drop 실행

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

- 정적 디스패치: 컴파일 타임에 결정, 인라인 최적화 => 빠름, 바이너리 커질 가능성 있음\
  일반 타입 또는 `&impl`를 사용한 구현타입\
  _\* `&impl`는 매개변수나 반환값 타입으로만 지정가능, `Vec`와 같은 자료형 안에서는 사용 불가하며, 구현체 타입으로 조건분기 불가_

  ```rs
  pub fn notify(item: &impl Summary) -> impl Summary {
    // ...
  }
  ```

  ```rs
  pub fn notify<T: Summary>(item1: &T, item2: &T) {
    // ...
  }
  ```

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

- 읽을 때는 참조하고, 쓸 때만 복사해서 소유(clone) 또는 원본 사용
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
    println!("복사본: {:?}", input1); // ➤ [1, 2, 3] (복사되어 복사본이 바뀜)
    println!("소유권 전달: {:?}", input2); // ➤ [1, 0, 1] (소유권이 이전되어 원본이 바뀜)
}
```

<br />

### Derive 매크로 작성(proc_macro_derive) - 커스텀 트레잇 derive 주입

작성 방법

1. `cargo new ./lib/my_macro_hello --lib`\
   프로시저 매크로는 별도의 라이브러리 패키지(크레이트)로 작성해야 함
2. 생성된 크레잇 경로에서 `cargo add syn quote`으로 필요 의존성 설치
3. 생성된 `Cargo.toml`에 아래 내용이 포함되어야 함

   ```toml
   [lib]
   proc-macro = true
   ```

   전체 내용

   ```toml
   [package]
   name = "my_macro_hello"
   version = "0.1.0"
   edition = "2024"

   [dependencies]
   quote = "1.0.40"
   syn = "2.0.101"

   [lib]
   proc-macro = true
   ```

4. 구현체 작성

   ```rs
    use proc_macro::TokenStream;
    use quote::quote;
    use syn::{DeriveInput, parse_macro_input};

    #[proc_macro_derive(MyMacroHello)]
    pub fn my_macro_hello(input: TokenStream) -> TokenStream {
        // 매크로가 적용된 타입의 정보
        let ast = parse_macro_input!(input as DeriveInput);

        // 타입의 이름
        let name = &ast.ident;

        // 함수 주입
        let expanded = quote! {
            impl #name {
                pub fn hello(&self) {
                    println!("Hello from {}!", stringify!(#name));
                }
            }
        };

        // 생성된 코드를 토큰 스트림으로 변환
        expanded.into()
        // 또는 TokenStream::from(expanded)
    }
   ```

5. 라이브러리 의존성 추가 `cargo add my_macro_hello --path ./lib/my_macro_hello`
6. 사용

   ```rs
    use my_macro_hello::MyMacroHello;

    #[derive(MyMacroHello)]
    struct StructGood;

    fn main() {
        StructGood.hello();
    }
   ```

<br />

### 속성 매크로 작성(proc_macro_attribute)

작성 방법

1. [Derive 매크로 작성과 동일(1~3)](#derive-매크로-작성proc_macro_derive---커스텀-트레잇-derive-주입)
2. 구현제 작성

   ```rs
    use proc_macro::TokenStream;
    use quote::quote;
    use syn::{ItemFn, parse_macro_input};

    #[proc_macro_attribute]
    pub fn auth_required(_attr: TokenStream, item: TokenStream) -> TokenStream {
        //  파싱
        let input = parse_macro_input!(item as ItemFn);

        // 파싱된 함수에서 정보 추출
        let fn_name = &input.sig.ident; // 함수 이름
        let fn_block = &input.block; // 함수 본문
        let fn_vis = &input.vis; // 함수 가시성(pub, private)
        let fn_sig = &input.sig; // 함수 정의 타입

        let expanded = quote! {
            #fn_vis #fn_sig {
                println!("[auth_required] 인증 체크 중...");

                // 인증 여부 체크 로직
                let authorized = true;

                if !authorized {
                    println!("🚫 인증 실패: {}", stringify!(#fn_name));

                    return;
                }

                println!("[auth_required] ✅ 인증 체크 성공!");

                // 인증 성공 시, 원본 함수 본문 실행
                #fn_block
            }
        };

        // 생성된 코드를 토큰 스트림으로 변환
        expanded.into()
        // 또는 TokenStream::from(expanded)
    }
   ```

3. 라이브러리 의존성 추가 `cargo add my_macro_auth --path ./lib/my_macro_auth`
4. 사용

   ```rs
    use my_macro_auth::auth_required;

    #[auth_required]
    fn something_func() {
        println!("인증된 사용자만 실행됨!");
    }

    fn main() {
        something_func();
    }
   ```

---

## PBL

### 인스턴스 비교

`==`(PartialEq)를 사용 시, 내부 값을 비교

> `Eq`: 완전한 동치성 비교라는 명시적 표시

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

### 일반 함수/클로저의 구조체 필드값

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

    println!("{}", (s.func)(5));  // impl로 구현한 메소드가 아닌, 필드값이어서 괄호 필요
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
        (self.op)(a, b) // impl로 구현한 메소드가 아닌, 필드값이어서 괄호 필요
    }
}

fn main() {
    let add = Adder::new(|x, y| x + y);
    println!("{}", add.calc(3, 4)); // 7
}
```

### async 함수/클로저의 전달

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

# Rust - PBL

- [인스턴스 비교](#인스턴스-비교)
- [콜백 함수](#콜백-함수)
  - [Fn, FnMut, FnOnce](#fn-fnmut-fnonce)
  - [fn 함수 포인터](#fn-함수-포인터)
- [구조체 필드값에 일반 함수/클로저 설정](#구조체-필드값에-일반-함수클로저-설정)
- [async 함수/클로저의 전달](#async-함수클로저의-전달)
- [오버라이딩](#오버라이딩)
  - [메서드에 self가 존재](#메서드에-self가-존재)
  - [메서드에 self가 미존재](#메서드에-self가-미존재)

## 인스턴스 비교

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

#[derive(PartialEq)]
struct Dog;

let dog1 = Dog;
let dog2 = Dog;

let same = ptr::eq(&dog1, &dog2);
println!("같은 인스턴스인가? {}", same); // false

println!("{:p} :: {:p}", &dog1, &dog2); // 메모리 주소 출력
```

---

## 콜백 함수

### Fn, FnMut, FnOnce

- `Fn()`: 외부 변수(환경)를 불변 참조(&x)로 캡처하거나 캡처하지 않는 클로저
- `FnMut()`: 외부 변수(환경)를 가변 참조(&mut x)로 캡처, FnMut 클로저를 호출하려면 클로저 변수 자체도 mut여야 함
- `FnOnce()`: move로 소유권을 클로저 내부로 이동시켜 소비하기 때문에, 한 번만 호출 가능

> `impl Fn(...)` 또는 `Box<dyn Fn(...)>` 와 같은 형식을 사용하며 일반 함수도 허용

```rs
fn make_adder(x: i32) -> impl Fn(i32) -> i32 {
    move |y| x + y
}

fn adder(x: i32) -> i32 {
    x + 1
}

fn run_with_callback1(x: i32, callback: impl Fn(i32) -> i32) -> i32 {
    callback(x)
}

fn run_with_callback2<F>(x: i32, callback: F) -> i32
where
    F: Fn(i32) -> i32,
{
    callback(x)
}

fn run_with_callback3<F: Fn(i32) -> i32>(x: i32, callback: F) -> i32 {
    callback(x)
}

let result1 = run_with_callback1(10, make_adder(1));
let result2 = run_with_callback2(20, make_adder(2));
let result3 = run_with_callback3(30, make_adder(3));
let result4 = run_with_callback3(30, adder);

println!("{result1}, {result2}, {result3}, {result4}");
```

### fn 함수 포인터

- 함수 포인터는 세 가지 클로저 트레이트 (Fn, FnMut, FnOnce) 을 모두 구현
- 고정 크기이고 비용 적음

```rs
fn add_one(x: i32) -> i32 {
    x + 1
}

fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}

fn main() {
    let answer1 = do_twice(add_one, 5);
    let answer2 = do_twice(|x| x + 1, 5);

    println!("{answer1}, {answer2}");
}
```

---

## 구조체 필드값에 일반 함수/클로저 설정

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

---

## async 함수/클로저의 전달

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

---

## 오버라이딩

기본적으로 직접 정의된 연관 함수를 호출

### 메서드에 self가 존재

```rs
trait Pilot {
    fn fly(&self);
}

trait Wizard {
    fn fly(&self);
}

struct Human;

impl Pilot for Human {
    fn fly(&self) {
        println!("This is your captain speaking.");
    }
}

impl Wizard for Human {
    fn fly(&self) {
        println!("Up!");
    }
}

impl Human {
    fn fly(&self) {
        println!("*waving arms furiously*");
    }
}

fn main() {
    let person = Human;

    Pilot::fly(&person);
    Wizard::fly(&person);
    person.fly();
}
```

### 메서드에 self가 미존재

```rs
trait Animal {
    fn baby_name() -> String;
}

struct Dog;

impl Dog {
    fn baby_name() -> String {
        String::from("Spot")
    }
}

impl Animal for Dog {
    fn baby_name() -> String {
        String::from("puppy")
    }
}

fn main() {
    println!("{}", Dog::baby_name());
    println!("{}", <Dog as Animal>::baby_name());
}
```

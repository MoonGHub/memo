# Rust - Cargo

- rustup.rs으로 설치한 경우 바이너리 파일 저장 경로: `$HOME/.cargo/bin`
- [crates.io에 배포](https://doc.rust-kr.org/ch14-02-publishing-to-crates-io.html#cartesio-%EA%B3%84%EC%A0%95-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)

---

- [CLI](#cli)
  - [생성](#생성)
  - [의존성 관리](#의존성-관리)
  - [기타](#기타)
- [프로필](#프로필)
  - [dev 프로필](#dev-프로필)
  - [release 프로필](#release-프로필)
- [workspace - 모노레포](#workspace---모노레포)
  - [생성](#생성-1)

---

## CLI

### 생성

일반 프로젝트 생성

- `cargo new new_project`

라이브러리 생성

- `cargo new ./lib/my_macro_hello --lib`

### 의존성 관리

- `cargo add {crate_name} --features {feature}`: 현재 프로젝트(Cargo.toml)에 라이브러리 크레이트를 설치
- `cargo remove {crate_name}`: 현재 프로젝트의 라이브러리 크레이트를 제거
- `cargo update`: 명시한 버전 범위 내에서 최신 버전으로 업데이트

전역 설치

- `cargo install {crate_name}`: 전역적으로 CLI를 위한 바이너리 크레이트를 설치 - 바이너리 타겟(실행 가능한 프로그램) 한정
  - `cargo install --list`: 설치 목록
- `cargo uninstall {crate_name}`: 전역적으로 설치한 바이너리 크레이트를 제거

### 기타

- `cargo doc --open`: 의존하는 크레이트의 문서를 로컬에서 모두 빌드하여 브라우저로 오픈
  - `target/doc` 경로에 생성됨
  - `///`: 문서화 주석
  - `//!`: 이 주석을 포함하는 아이템에 대한 주석 - 루트 파일에 작성 - 크레이트 또는 모듈 전체에 대한 주석 작성
  - 일반적인 # 사용 절 - Panics, Errors, Safety
- `cargo test`: 모든 크레이트에 대해 `#[test]` 속성이 붙은 함수 또는 문서화 주석(///)내 ```블록 안의 함수들을 실행 (빌드함)
  - `--`: cargo 명령어 인자와 해당 실행 바이너리의 인자 구분자
  - `--nocapture`: stdout과 stderr를 출력
  - `-p {crate_name}`
- `cargo --list`: cargo로 실행 가능 목록
- `cargo check`: 소스 내 오류 검출(빌드 안함)

---

## 프로필

`Cargo.toml`의 `[profile.*]` 섹션으로 설정하며 기본 설정을 덮어씌움

- `opt-level`: 0~3, 최적화 수치
- [설정 옵션 참고](https://doc.rust-lang.org/cargo/reference/profiles.html)

### dev 프로필

`cargo build`에 적용

```toml
[profile.dev]
opt-level = 0 # 기본값
```

### release 프로필

`cargo build --release`에 적용

```toml
[profile.release]
opt-level = 3 # 기본값
```

---

## workspace - 모노레포

- `Cargo.lock`은 루트에 하나만 생김 - 모든 의존성에 대해 같은 버전을 사용

### 생성

1. 루트 경로에서 아래 내용으로 `Cargo.toml`생성

   ```toml
   [workspace]
   members = [
       "adder",
       "add_one",
   ]
   ```

2. 멤버로 등록한 크레이트를 루트에서 각각 생성
   - `cargo new adder`
   - `cargo new add_one --lib`
3. `add_one`를 사용하는 `adder`에서 의존성 추가
   ```toml
   [dependencies]
   add_one = { path = "../add_one" }
   ```
4. 루트에서 `cargo build`로 빌드
5. 루트에서 `cargo run -p adder`

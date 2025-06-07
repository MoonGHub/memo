# Rust - Cargo

## CLI

### 생성

일반 프로젝트 생성

- `cargo new new_project`

라이브러리 생성

- `cargo new ./lib/my_macro_hello --lib`

### 의존성

- `cargo add {crate} --features {feature}`: 현재 프로젝트(Cargo.toml)에 라이브러리 크레이트를 설치
- `cargo remove {crate}`: 현재 프로젝트의 라이브러리 크레이트를 제거
- `cargo update`: 명시한 버전 범위 내에서 최신 버전으로 업데이트
- `cargo install {crate}`: 전역적으로 CLI를 위한 바이너리 크레이트를 설치
- `cargo uninstall {crate}`: 전역적으로 설치한 바이너리 크레이트를 제거

### 기타

- `cargo doc --open`: 의존하는 크레이트의 문서를 로컬에서 모두 빌드하여 브라우저로 오픈

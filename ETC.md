# ETC

### 🦋 메타마스크 및 이더리움 결제 참고

- https://metamask.github.io/api-playground/api-documentation/
- https://ethereum.org/en/developers/docs/apis/json-rpc/

<br />

### 🦋 포트

> `0 ~ 1023`: Well Know Port Numbers - 국제인터넷주소관리기구(CANN)가 특정 앱용으로 예약한 포트\
> `1024 ~ 49151`: Registered Port Numbers - 회사에서 등록, 사용가능\
> `49152 ~ 65535`: Dynamic Or Private Port Numbers - 운영체제가 부여하는 동적포트, 또는 개인적 사용가능

- `21`: FTP
- `22`: SFTP
- `443`: HTTPS
- `3306`: MySql

<br />

### 🦋 데이터 단위

- bit: 0 or 1
- Byte: 8bit
- KB: 1024Byte
- MB: 1024KB
- GB: 1024MB
- TB: 1024GB

<br />

### 🦋 진수와 비트

- 2진수 - 0, 1 (1bit)
- 4진수 - 0 ~ 3 (2bit)
- 8진수(0): 0 ~ 7 (3bit)
- 16진수(0x): 0 ~ F (4bit)

<br />

### 🦋 문자

- ASCII

  - 1Byte
  - $2^8$(256)개의 문자를 표현(0~255 or -128~127)

- 유니코드

  - 문자 코드들의 집합
  - 16진수(4bit) 네자리로 2바이트 문자 표현
  - 0x0041(면 번호 2개(00는 아스키) + 인덱스 번호 2개) = A
  - UTF - 유니코드의 인코딩 규칙
    - UTF-8
      - 1바이트씩 표시
      - 가변바이트(1byte ~ 4byte)
      - 4byte는 이모지 영역
      - 1바이트로 표현 가능한 경우 1바이트로 표현
      - A: 0x0041 -> 0x41
      - π: 0x03C0 -> 0xCF 0x80
      - 한: 0xD55C -> 0xED 0x95 0x9C

<br />

### 🦋 실수를 저장하는 방법

- 지수와 가수
  - 비트
    - Float: `1(MSB) + 8(지수) + 23(가수)` = `32`자릿수의 비트를 가짐
    - Double: `1(MSB) + 11(지수) + 52(가수)` = `64`자릿수의 비트를 가짐
  - 상용로그
    - 정수 부분: 지수(Characteristic)
    - 소수 부분: 가수(Mantissa)
    - $\log16 = 1.234$\
      지수: 1\
      가수: 0.234
  - 부동 소수점 기수법
    - Mantissa(M: 가수)$\pm$ n(n은 지수:exponent)
    - $123.4 = 0.1234$+3
      - 가수: 0.1234
      - 지수: 3
    - $0.001234 = 0.1234$-2
      - 가수: 0.1234
      - 지수: -2
  - 부동 소수점 형식(`E or e`)
    - Mantissa(M: 가수)E $\pm$ n = M $\times 10^n$(n은 지수:exponent)
    - 3e+6 $= 3 \times 10^6$
      - 가수: 3
      - 지수: 6
    - $123.456 =$ 1.23456e+2 $= 1.23456 \times 10^2$
      - 가수: 1.23456
      - 지수: 2

...[참고](https://bigpel66.oopy.io/library/c/chewing-c/4)

<br />

### 🦋 로컬 스토리지 vs 세션 스토리지

- 로컬 스토리지
  - 영구적 보존
  - 5MB ~ 10MB
  - 해당 도메인에서만 접근이 가능
  - 사용자의 개인설정, 프로필, 오프라인 데이터 등을 저장
- 세션 스토리지
  - 브라우저를 닫거나 세션을 종료할 때까지 보존
  - 5MB ~ 10MB, 브라우저마다 다름
  - 같은 브라우저 세션, 같은 도메인의 여러탭 또는 창 내에서만 공유
  - 로그인 정보, 장바구니 정보 등을 저장

---

- `Enter`: \r(캐리지 리턴 - 13) + \n(라인피드 - 10)
- Data from forms is normally encoded using the "media type" application/x-www-form-urlencoded.
  - But when the form includes files, it is encoded as multipart/form-data. (HTTP 프로토콜)

---

<br />

## WORD

- `i.e.`: 라틴어 id est,의 약어이며, '즉', '다시 말하면'이라는 뜻
- `Fyi`: For Your Information, 참고로
- `코딩 컨벤션`: 관리하기 쉬운 코드를 작성하기 위한 일종의 코딩 스타일 규약
- `UTC`: Coordinated Universal Time - 협정 세계시(영국 런던기준),
- `KST`: 한국 표준시(UTC +9)
- `MS949`: 한글 확장 완성형 문자집합(일본어, 중국어 등에도 사용)
- `XML`: eXtensible Markup Language, 확장성 마크업 언어
- `RSS`: Really Simple Syndication, 초간편 배포, XML기반의 콘텐츠 배급 포맷
- `ECMA`: European Computer Manufacturers Association\
  - ECMAScript(ES)는 자바스크립트를 이루는 코어(Core) 스크립트 언어
  - ES5는 2009년에 ES6은 2015에 제작
- `SVG`: Scalable Vector Graphic, 웹을 위한 벡터 기반 그래픽
  - Canvas는 비트맵 그래픽
- `TCP`: Transmission Control Protocol
- `UDP`: User Datagram Protocol
- `URL`(Uniform Resource Locator): 서버가 제공하는 파일들의 위치
- `URI`(Uniform Resource Identifier): URL로부터 자원을 식별, HTTP프로토콜, 호스트명, port번호 등 제외함
- `UUID`: Universally Unique Identifier
- `TL;DR`: Too Long; Didn't Read, 요약이나 간추린 설명
- `DX`: Developer Experience, 개발자 경험

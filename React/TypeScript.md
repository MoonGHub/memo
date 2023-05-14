# React - TypeScript

## Keywords

- Partial
- Omit
- Pick
- Record
- Awaited
- ReturnType
- Parameters

target: 컴파일된 코드가 어떤 환경에서 실행될 지 정의 ex) es5 or es6
module: 컴파일된 코드가 어던 모듈 시스템을 사용할지 정의 ex) common or es2015
strict: 모든 타입 체킹 옵션을 활성화한다는 것을 의미
esModuleInterop: commonjs 모듈 형태로 이루어진 파일을 es2015 모듈 형태로 호출
outDir: 컴파일된 파일들이 저장되는 경로를 지정
sourceMap : 소스맵 사용 여부, 원본 소스와 최종소스를 매핑해서 추적할 수 있는 방법
noImplicityAny : any 로 선언된 식과 정의에 대해 에러를 발생시킴.

source-map-loader : 원본 소스와 최종소스를 매핑해서 추적할 수 있는 방법, enforce:pre로 js에 설정

children: React.ReactNode;
onClick?(): void;
onClick?: () => void;
getArea(): number; // getArea라는 함수 필수, 리턴값은 숫자
// getArea(): () => String; -> 리턴값은 String을 리턴하는 함수!

React.MouseEvent<HTMLButtonElement>

typings.d.ts
기존 js모듈을 ts에서 사용하기 위해, js모듈의 타입 정보를 기술 하는 곳

1. 단순히 npm으로 타입전용 모듈을 받는다(없는 경우도 있음) // @types/모듈이름
2. typings.d.ts에 declare module '모듈이름'; 을 기술

### 재 내보내기

```ts
export { default as man } from "./man.svg";
export { default as girl } from "./girl.svg";
```

```ts
import * as icons from "./svg";

type IconType = keyof typeof icons;
// 'man' | 'girl'
```

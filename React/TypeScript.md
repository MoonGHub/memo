# React - TypeScript

## Keywords

> VSCode 내장 타입스크립트 참고
> **/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/node_modules/typescript/lib/lib.es5.d.ts** > https://www.typescriptlang.org/ko/docs/handbook/utility-types.html

- Utility Type
  - Partial
  - Omit
  - Pick
  - Record
  - Awaited
  - ReturnType
  - Parameters
  - Capitalize
  - InstanceType
- etc
  - infer

<br />

## tsconfig.json

- `target`: 컴파일된 코드가 어떤 환경에서 실행될 지 정의 ex) es5 or es6
- `module`: 컴파일된 코드가 어던 모듈 시스템을 사용할지 정의 ex) common or es2015
- `strict`: 모든 타입 체킹 옵션을 활성화한다는 것을 의미
- `esModuleInterop`: commonjs 모듈 형태로 이루어진 파일을 es2015 모듈 형태로 호출
- `outDir`: 컴파일된 파일들이 저장되는 경로를 지정
- `sourceMap` : 소스맵 사용 여부, 원본 소스와 최종소스를 매핑해서 추적할 수 있는 방법
- `noImplicityAny` : any 로 선언된 식과 정의에 대해 에러를 발생시킴.

<br />

## PBL

### class

클래스에 대해 typeof 사용하여 변수에 지정할 경우, 해당 클래스의 타입이 아닌 생성자 타입을 나타냄\
따라서 typeof를 사용하지 않고, 직접 클래스를 타입으로 지정해줘야 함 또는 Utility Type의 InstanceType를 사용

### ts-2742

- 스토리북 에러

> '\_LexicalEditor'의 유추된 형식 이름을 지정하려면 '.pnpm/@storybook+types@7.6.17/node_modules/@storybook/types'에 대한 참조가 있어야 합니다.
> 이식하지 못할 수 있습니다. 형식 주석이 필요합니다.ts(2742)

> [!NOTE]
>
> tsconfig.json
>
> ```js
> {
>   // ...
>   "declaration": false // *.d.ts 생성 여부,
> }
> ```

- StoryFn 타입 지정해주면 됨

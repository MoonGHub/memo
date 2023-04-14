# Node - Grammer

## ESM

파일 확장자를 .mjs로 하여 실행 가능하지만,\
`--experimental-modules`플래그와 함께 실행하거나 **package.json**에서 `type: "module"`을 지정해줘야 함 (검증 전)

<br />

## 실행 옵션

### `--experimental-specifier-resolution=node`

CommonJS 모듈과의 상호 운용성을 개선하기 위해 도입된 옵션.\
이 옵션을 사용하면 ECMAScript 모듈의 import 구문에서 파일 확장자를 생략하거나, 상대 경로로 모듈을 찾을 때 더 유연하게 해석

<br />

### `--es-module-specifier-resolution=node`

ECMAScript 모듈의 해석을 지정하는 옵션

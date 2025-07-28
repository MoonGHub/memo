# JavaScript - package.json

- files: 패키지가 의존성으로 설치될 때 같이 포함될 파일들의 배열. 생략 시, 자동 제외로 설정된 파일을 제외한 모든 파일이 포함
- main: 프로그램의 기본 진입 점(entry point)를 지정
- dependencies: 패키지의 배포 시 포함될 의존성 모듈을 지정
- devDependencies: 패키지의 개발 시 사용될 의존성 모듈을 지정.(배포 시 미포함)
  - ~version: 버전과 대략 동일, 버그 수정 릴리즈
  - ^version: 버전과 호환, 이전 버전과 호환, 버그 수정 릴리즈
- bundledDependencies:

  - 패키지를 게시할 때 번들로 묶을 패키지 이름을 배열로 지정
  - npm 패키지를 로컬에서 보존해야 하거나 단일 파일 다운로드를 통해 사용할 수 있는 경우,\
    npm pack을 실행하여 패키지를 <name>-<version>.tgz 형태의 tarball 파일로 묶을 수 있음

- private: 개인 저장소의 우연한 발행을 방지하기 위해 npm에서 패키지의 공개 여부를 지정
- dependenciesMeta: dependencies 및 optionalDependencies에 포함된 의존성들에 대한 추가 정보를 설정하는 데 사용
  - optional: 특정 의존성을 선택적 의존성으로 표시
  - injected: pnpm 전용이며, 특정 의존성이 직접 설치되지 않고 외부에서 주입 [- 참고](./PackageManager.md#dependenciesmetainjected)
- sideEffects: 사용되지 않는 파일도 안전하게 제거하지 않고 번들에 포함시킬지의 여부
- exports: 해당 패키지를 import시, 외부에 노출될 경로 지정

  - ex)
    ```javascript
    // @moon-libs/web 패키지
    {
      // ...
      "exports": {
        ".": {
          "types": "./dist/index.d.ts",
          "import": "./dist/index.js",
          "require": "./dist/index.js"
        },
        // import { color, defaultTheme } from '@moon-libs/web/dist/ui/theme/constant';
        "./dist/ui/theme/constant": {
          "import": "./dist/ui/theme/constant/index.js",
          "require": "./dist/ui/theme/constant/index.js"
        },
        "./*": {
          "import": "./dist/*",
          "require": "./dist/*",
          "types": "./dist/*"
        }
      }
    }
    ```

---

- `packageManager`: 해당 프로젝트의 패키지 매니저 명시
  - `npm view pnpm@9.13.2 dist.integrity`: 해당 패키지 매니저 해쉬값 확인
    - 버전은 같아도 실행파일이 다를 수 있으므로 명시
  - ex) `"packageManager": "pnpm@9.13.2+sha512-iMnDhkR...`
- `proxy`: CRA 프로젝트에서만 사용(간단하게 적용)
- `engines`: 패키지가 작동하는 Node 버전을 명시
  - `.npmrc`에서 `engine-strict=true` 설정 시, 버전이 맞지 않으면 설치 거부
- `browserslist`: 트랜스파일, 폴리필, 최적화 등에 대상 브라우저 타겟 지정
  ```json
  {
    // ...
    "browserslist": {
      "production": [
        ">0.2%", // 시장 점유율 0.2% 이상인 브라우저
        "not dead", // 24개월 이내에 업데이트된 브라우저만 포함
        "not op_mini all", // Opera Mini 제외 (저사양 모바일)
        "ie 11", // IE 11 포함 (ES5 지원)
        "last 2 versions", // 각 브라우저 최신 2개 버전 지원
        "Firefox ESR" // Firefox 장기 지원 버전 포함
      ],
      "development": [
        "last 1 chrome version",
        "last 1 firefox version",
        "last 1 safari version"
      ]
    }
  }
  ```

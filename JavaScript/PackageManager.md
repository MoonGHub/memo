# Package Manager

## NPM

### 패키지 관리

- `npm update`\
  해당 프로젝트에 설치된 패키지들을 업데이트
- `npm update <패키지명>`\
  특정 패키지 업데이트
- `npm version [버전]`\
  npm으로된 프로젝트 버전을 업데이트
- `npm dedupe`\
  npm의 중복된 패키지들을 정리
- `npm cache`
  - ls
  - clean
    - --force
- `npm rebuild`\
  현재 프로젝트에 이미 설치된 패키지들의 바이너리 파일을 다시 빌드하며 아래와 같은 경우에 사용
  - node버전을 변경 할 경우
  - 운영체제 등 실행 시스템 환경을 변경 할 경우
  - 패키지 자체 문제 또는 의존성 문제 발생 시

<br />

### 조회

- `npm root`\
  node_modules의 위치를 알려줍니다.
- `npm outdated`\
  package.json의 명시 버전에 **일치 - 빨강**, **불일치 - 노랑**
- `npm ls`\
  현재 설치된 패키지의 버전과 dependencies를 트리 구조로 표현
- `npm list -g --depth=0`\
  전역으로 설치된 패키지들을 보여줌

<br />

### 로그인 및 배포

- `npm adduser`
- `npm login`
- `npm logout`
- `npm whoami`
- `npm publish`
  - 직접 출시하거나 버전 업그레이드
  - .gitignore또는 .npmignore에 명시되지 않은 파일들이 npm 저장소에 업로드
- `npm unpublish`\
  사용 비추천
- `npm deprecate`\
  출시 된 패키지를 deprecate 적용

<br />

## [Yarn](https://yarnpkg.com/cli/install)

### 패키지 관리

- `yarn add`
- `yarn remove`
- `yarn upgrade`

<br />

### 워크스페이스

- `yarn workspace {app_name} {command | script_command}`\
  ex)

  ```shell
  yarn workspace dayfly dev
  # dayfly프로젝트의 dev script를 실행

  yarn workspace dayfly add react-day-picker
  # dayfly프로젝트에 react-day-picker 추가
  ```

<br />

## Yarn Berry

```text
1. 라이브러리 호이스팅이 안됨
2. 루트 패키지와 각 프로젝트 패키지간 충돌이 발생
```

`yarn set version berry`

적용 후, 생성 된 **.yarnrc.yml**에 `nodeLinker: pnp` 추가

```shell
# pnp(plug-n-play)를 사용 시, cannot find module Error 해결을 위함
yarn add @yarnpkg/sdks -D
yarn dlx @yarnpkg/sdks vscode
```

### 패키지 관리

- `yarn up`\
  업그레이드

<br />

## pnpm

[참고](https://pnpm.io/)

```text
1. 호이스팅 잘 됨
2. 기본적으로 가상 스토어(루트의 node_modules/.pnpm)에서 모든 패키지를 관리 - 빠름
```

<br />

### 설치

1. `npm install -g pnpm`
2. `pnpm --version`
3. 루트의 package.json에 추가

   ```js
   {
     // ...
     "packageManager": "pnpm@7.29.2",
     "workspaces": ["apps/**/*", "libs/**/*", "tools/**/*"]
     // ...
   }
   ```

4. `pnpm-workspace.yaml` 생성 후, 아래 내용 추가
   ```yml
   packages:
     - "apps/**/*"
     - "libs/**/*"
     - "tools/**/*"
   ```

<br />

### 프로젝트 추가

1. `pnpm init`(경로지정 안됨) 또는 `pnpm create vite@latest 경로` 또는 `pnpm dlx create-next-app@latest 경로`
2. package.json 설정
3. 루트 디렉토리에서 필요한 의존성들을 설치
   `pnpm --filter {project_name} add react react-dom @babel/cli`

<br />

### 명령어

- 프로젝트 리스트 보기

  - `pnpm recursive list`
  - `pnpm recursive list | grep @moon`

- 명령어 개별 실행

  - `pnpm --filter {project_name} exec {command}`

- 스크립트 전체 실행

  - `pnpm -r build`\
    build 스크립트가 포함된 모든 패키지의 build를 수행
  - `pnpm -r --parallel tscw`\
    비동기로 실행됨

- 부트스트랩 실행

  - `pnpm dlx create-next-app@latest`
  - `pnpm --filter {project_name} exec pnpm dlx storybook@latest init`

- ETC
  - `pnpm dedupe`\
    Perform an install removing older dependencies in the lockfile if a newer version can be used.
    - --check: Check if running dedupe would result in changes without installing packages or editing the lockfile. Exits with a non-zero status code if changes are possible.
  - `pnpm store prune`\
    Removed all cached metadata files
  - `pnpm install --shamefully-hoist`
    - 각 프로젝트의 의존성들이 최상위의 **node_modules**에 설치됨
    - 서로 다른 버전의 의존성으로 호환 문제 시
  - `pnpm update --workspace`\
    루트 의존성 버전 업데이트

<br />

### 의존성 관리

#### dependenciesMeta.\*.injected

> 현재 프로젝트에서 사용중인 의존성<sup>1</sup> 버전을, 다른 패키지의 의존성<sup>1</sup> 버전으로 내려줌
>
> - 1는 동일 의존성

`true`인 경우

- `패키지`가 해당 프로젝트의 node_modules에 설치되지 않고 가상 스토어에서 하드링크 됨
- 프로젝트의 의존성(e.g. react@100)이 있고, `패키지`에 동일 의존성(e.g. react@10)이 있는 경우, `패키지`는 프로젝트의 의존성(e.g. react@100)이 주입됨
- [참고](https://pnpm.io/8.x/package_json#dependenciesmeta)

```js
// ex) package.json
{
  "name": "card",
  "dependencies": {
    "button": "workspace:1.0.0",
    "react": "16"
  },
  "dependenciesMeta": {
    "button": {
      "injected": true
    }
  }
}
```

`미설정` 또는 `false`인 경우

- `패키지`가 해당 프로젝트의 node_modules에 설치 됨(설치된 패키지는 가상 스토어에서 심볼릭 링크 됨 - hoist가 true이며, hoist-pattern에 포함 될 경우)

- `패키지`마다의 각각의 의존성을 사용?

<br />

## 버전 범위

### **~**

`~0.0.1` : >=0.0.1 <0.1.0\
`~0.1.1` : >=0.1.1 <0.2.0\
`~0.1` : >=0.1.0 <0.2.0\
`~0` : >=0.0 <1.0\

<br />

### **^**

`^1.0.2` : >=1.0.2 <2.0\
`^1.0` : >=1.0.0 <2.0\
`^1` : >=1.0.0 <2.0

예외) 주 버전이 0인 경우

`^0.1.2` : >=0.1.2 <0.2.0\
`^0.1` : >=0.1.0 <0.2.0\
`^0` : >=0.0.0 <1.0.0\
`^0.0.1` : ==0.0.1

# JavaScript - NPM

## Command

### NPM 관리

- `npm version [버전]`\
  npm 버전 업데이트
- `npm cache`
- `npm cache clean`
  - --force
- `npm rebuild`\
  npm 재설치

### 패키지 관리

- `npm update`\
  설치한 패키지를 업데이트
- `npm dedupe`\
  npm의 중복된 패키지들을 정리

<br />

### 조회

- `npm root`\
  node_modules의 위치를 알려줍니다.
- `npm outdated`\
  package.json의 명시 버전에 **일치 - 빨강**, **불일치 - 노랑**
- `npm ls`\
  현재 설치된 패키지의 버전과 dependencies를 트리 구조로 표현

<br />

### 로그인 및 출시

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

--

<br />

## Yarn

[참고](https://yarnpkg.com/cli/install)

### Yarn Berry

`yarn set version berry`

적용 후, 생성 된 **.yarnrc.yml**에 `nodeLinker: pnp` 추가

```shell
# pnp(plug-n-play)를 사용 시, cannot find module Error 해결을 위함
yarn add @yarnpkg/sdks -D
yarn dlx @yarnpkg/sdks vscode
```

<br />

### 패키지 관리

- `yarn add`
- `yarn remove`
- `yarn upgrade`
  > `yarn berry`의 경우에는 `yarn up`

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

예외)

`^0.1.2` : >=0.1.2 <0.2.0\
`^0.1` : >=0.1.0 <0.2.0\
`^0` : >=0.0.0 <1.0.0\
`^0.0.1` : ==0.0.1

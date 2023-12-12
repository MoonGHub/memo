# React - Library

## react-router-dom

**react-router**는 코어를 포함하는 master브랜치의 라이브러리\
**react-router-dom**은 DOM이 인식 할 수 있는 컴포넌트들의 모음

<br />

## Monorepo

### Lerna

- `yarn lerna run {script} --scope={project_name} --steam`

### NX

> React와 React Native 그리고 그 외 React관련 프로젝트를 위한 세팅 명령어

```text
1. nx exec 명령어가 기능하지 않음
2. 초기화를 위해 nx exec 명령어가 안먹힘에 따라 package.json을 직접 생성 하면 링크, 호이스팅이 안됨(해당 프로젝트에서 별도 컨트롤이 필요)
3. project.json에 스크립트를 추가하는데 있어 별도 executor설정이 필요하며 번거로움
```

- 설치

  - `npx create-nx-workspace@latest {app_nmame} --preset=empty --packageManager=yarn`

- NX관련 패키지 설치

  - `yarn add -D @nrwl/react @nrwl/react-native @nrwl/storybook -W`

- 프로젝트 추가

  - 웹
    - `yarn nx g @nrwl/react:app {project_name} --directory=web`

- UI 라이브러리 및 스토리북 추가

  `yarn add -D -W @storybook/addon-actions @storybook/addon-docs @storybook/addon-interactions @storybook/addon-links`

  - 웹

    - `yarn nx g @nrwl/react:lib web --directory=ui`
    - `yarn nx g @nrwl/storybook:configuration ui-web --tsConfiguration=true`

- 실행 명령어

  - `yarn nx run {project_name}:{script_name}`
  - `yarn nx {script_name} {project_name}`

- 기타 명령어
  - `yarn nx graph`

### Yarn Berry

[참고](../JavaScript/NPM.md#yarn)

```text
1. 라이브러리 호이스팅이 안됨
2. 루트 패키지와 각 프로젝트 패키지간 충돌이 발생
```

### pnpm

[참고](https://pnpm.io/)

```text
1. 호이스팅 잘 됨
2. 빠름?
3. 현시점 모노레포의 종착점
```

- 설치

  1. `npm install -g pnpm`
  2. `pnpm --version`
  3. 루트의 package.json에 추가

     ```json
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

- 프로젝트 추가

  1. 새 디렉토리 추가 및 해당 디렉토리에서 `npm init`
  2. package.json에 프로젝트 이름 설정
  3. npx를 사용하는 경우, script로 추가 후 루트 디렉토리에서 pnpm으로 실행
     `pnpm --filter {project_name} sb-init`
  4. 루트 디렉토리에서 필요한 종속성들을 설치
     `pnpm --filter {project_name} add react react-dom @babel/cli`

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

- ETC
  - `pnpm store prune`\
    Removed all cached metadata files
  - `pnpm install --shamefully-hoist`
    - 각 프로젝트의 종속성들이 최상위의 **node_modules**에 설치됨
    - 서로 다른 버전의 종속성으로 호환 문제 시

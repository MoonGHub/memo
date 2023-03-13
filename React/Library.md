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

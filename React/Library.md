# React - Library

## 자주쓰는

### react-router-dom

**react-router**는 코어를 포함하는 master브랜치의 라이브러리\
**react-router-dom**은 DOM이 인식 할 수 있는 컴포넌트들의 모음

<br />

## Monorepo

### Lerna

- `yarn lerna run {script} --scope={project_name} --steam`

<br />

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

<br />

## 상태관리

- Redux
  - **VIEW** --> **Action** --> **Dispatch** --> **Store** --> **VIEW**
- MobX
- Recoil
  - **VIEW** --> **Action** --> **Atom** --> **VIEW**

<br />

## next.js PBL(14v)

### [모노레포 공통 모듈을 페이지 라우터에서 사용 시](https://nextjs.org/docs/pages/api-reference/next-config-js/transpilePackages)

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  transpilePackages: ["@acme/ui", "lodash-es"],
  // 공통 UI모듈을 사용 시, @emotion/styled도 추가해줘야 함
};

module.exports = nextConfig;
```

### 스타일링 - emotion, tailwindcss, twin.macro

- [importsource](https://nextjs.org/docs/architecture/nextjs-compiler#importsource): Next.js will automatically detect jsxImportSource in jsconfig.json or tsconfig.json
  - tsconfig.json에 추가 `"jsxImportSource": "@emotion/react"`
    - app router에서 `'use client'`추가 필수
      - metadata 사용 불가
  - 또는 next.config.mjs의 compiler.emotion에 `true`지정
    - app router는 `'use client'`불필요
      - app router에서 twin.macro 및 tw props 사용 불가
      - `'use client'`추가 시 tw props적용
    - app router에서 className으로 tailwindcss 사용 가능
- tailwindcss, twin.macro 적용에 있어 tailwind.config의 content에서 className은 `js`, tw는 `tsx`로 확장자 인식
- emotion 및 tw 사용 또는 `"jsxImportSource": "@emotion/react"` 지정 시, app router에는 `'use client'`필요

<br />

## UI 관련

- [floating-ui](https://floating-ui.com/)

<br />

## 기타 유틸

- [Moment](https://momentjs.com/)
- [Numeral](http://numeraljs.com/)

# React - Storybook

## 초기화

[참고](https://storybook.js.org/docs/react/get-started/install/)

1. `pnpm --filter {project_name} add react react-dom @babel/cli`
2. `pnpm --filter {project_name} sb-init`\
   스크립트 내용: `sb-init: npx storybook init --type webpack_react`

- [초기화 시의 타입들 참고](https://github.com/storybookjs/storybook/blob/cf5749a099fc7671659624521dbd5473c830d05b/code/lib/cli/src/project_types.ts#L75)

<br />

## CSF(Component Story Format)

> Storybook v5.2 이후부터 권장\
> export default { } 형식의 방식 사용

<br />

## @storybook/addon-knobs

> 컴포넌트의 props를 스토리북 화면에서 변경해 바로 반영을 시켜줌

`yarn add -D @storybook/addon-knobs`

<br />

## @storybook/addon-actions (기본설치)

> 스토리북 상의 컴포넌트에 이벤트를 추가

```jsx
import { action, withActions } from "@storybook/addon-actions";
```

1. 스토리 컴포넌트의 적용할 이벤트에 action('로그')로 전달하면 됨
2. withActions('click \*','mouseover button')를 export default{}의 decorators의 배열로 전달
   // withActions('이벤트 셀럭터', ...)

<br />

## @storybook/addon-docs

>

`yarn add -D @storybook/addon-docs`

> npm install react-docgen-typescript-loader -D
> // 컴포넌트의 props 에서 사용된 TypeScript 타입들을 추출하여 문서로 만들어주는 도구
> // 웹팩에 추가!

Docs에서 타입설명들을 보여주기 위해서는, 스토리의 export default {} 에서 component에 대상 컴포넌트를 넣어줘야 함
그리고 컴포넌트 파일에서 각 타입위에 주석!

Docs에서 컴포넌트 subtitle은, export default{}에서 parameters옵션의 componentSubtitle에 전달
컴포넌트의 설명은 컴포넌트 파일에서 컴포넌트 코드 바로 윗 부분에 주석!

<br />

## ~~Upgrade MDX1 to MDX2~~

- 참고
  - https://github.com/storybookjs/storybook/blob/next/MIGRATION.md#opt-in-mdx2-support
  - https://chromatic-ui.notion.site/Storybook-7-migration-guide-dbf41fa347304eb2a5e9c69b34503937

1. `yarn add -D @storybook/mdx2-csf @mdx-js/react`
2. ```js
   module.exports = {
     features: {
       previewMdx2: true,
     },
   };
   ```

# React - Storybook

Storybook

✔Storybook v5.2 부터는 Component Story Format (CSF) 형식을 사용하여 문서를 작성
->export default { } 형식 사용

Knobs 애드온 적용 : 컴포넌트의 props를 스토리북 화면에서 변경해 바로 반영시켜줌
@storybook/addon-knobs

@storybook/addon-actions (기본설치됨)
import { action, withActions } from '@storybook/addon-actions';

1. 스토리 컴포넌트의 적용할 이벤트에 action('로그')로 전달하면 됨
2. withActions('click \*','mouseover button')를 export default{}의 decorators의 배열로 전달
   // withActions('이벤트 셀럭터', ...)

Docs 애드온,

> npm install @storybook/addon-docs -D
> addons에 추가 '@storybook/addon-docs'

> npm install react-docgen-typescript-loader -D
> // 컴포넌트의 props 에서 사용된 TypeScript 타입들을 추출하여 문서로 만들어주는 도구
> // 웹팩에 추가!

Docs에서 타입설명들을 보여주기 위해서는, 스토리의 export default {} 에서 component에 대상 컴포넌트를 넣어줘야 함
그리고 컴포넌트 파일에서 각 타입위에 주석!

Docs에서 컴포넌트 subtitle은, export default{}에서 parameters옵션의 componentSubtitle에 전달
컴포넌트의 설명은 컴포넌트 파일에서 컴포넌트 코드 바로 윗 부분에 주석!

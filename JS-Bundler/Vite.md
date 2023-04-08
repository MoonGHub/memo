# Bundler - Vite

> 작성 시점 버전 4.2.1

진입점이 기본적으로 html이며, 라이브러리 모드의 경우 별도 설정(build.lib)이 필요함

<br />

## 설치

> `pnpm create vite` (pnpm v7.29.2)

- React App

  - Select a framework: React
  - Select a variant: TypeScript + SWC

- React SSR의 경우
  - Select a framework: Others
  - Select a variant: create-vite-extra
  - Select a template: ssr-react
  - Select a variant: TypeScript + SWC

<br />

## 실행

- `vite`\
  development모드로 개발서버 실행
- `vite --mode=production`
- `vite build`
  - --watch
- `vite preview`

<br />

## 환경변수

mode에 따라서 `.env.production`또는 `.env.development`와 자동으로 매칭되어 사용가능\
환경변수 명은 `VITE_` 접두사를 붙여야 노출이 되며, 이외는 내부적으로 사용

- dotenv를 따로 설치하지 않아도 됨

```env
# .env.development

VITE_KEY1 = key1
KEY2 = key2
```

```js
console.log(import.meta.env.VITE_KEY1); // key1
console.log(import.meta.env.KEY2); // undefined
```

<br />

## SSR

동작 방식

0. 클라이언트와 서버 각각 빌드
1. Node에서 요청을 받으면 entry-server에 작성된 코드로 html을 렌더링
2. 클라이언트의 index.html에 1.에서의 렌더값을 대치
3. 응답

### Import 관련 에러

- ESM의 Lib에서의 type 또는 모듈 관련 문제\
  - 방법1. [참고](../JavaScript/ETC.md#🦋-esm-vs-cjs)
  - 방법2. `lazy(() => import("./Tooltip"))`의 동적 Import를 사용
    - Vite에서 동적 Import 사용 시, lazy와 같이 사용해야 함 [참고](../React/Grammar.md#suspense)

<br />

## Plugin

- @originjs/vite-plugin-commonjs
  - viteCommonjs
  - esbuildCommonjs
- vite-plugin-node-polyfills
  - nodePolyfills

<br />

## PBL

### vite.config.ts에 package.json import

tsconfig.node.json에 추가

```json
{
  "compilerOptions": {
    "resolveJsonModule": true
  },
  "include": ["package.json"]
}
```

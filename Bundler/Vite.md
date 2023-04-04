# Bundler - Vite

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

## SSR

### Import 관련 에러

- ESM의 Lib에서의 type 또는 모듈 관련 문제\
  - 방법1. [참고](../JavaScript/ETC.md#🦋-esm-vs-cjs)
  - 방법2. `lazy(() => import("./Tooltip"))`의 동적 Import를 사용
    - Vite에서 동적 Import 사용 시, lazy와 같이 사용해야 함

<br />

## Plugin

- @originjs/vite-plugin-commonjs
  - viteCommonjs
  - esbuildCommonjs
- vite-plugin-node-polyfills
  - nodePolyfills

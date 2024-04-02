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

- ESM의 Lib에서의 type 또는 모듈 관련 문제
  - 방법1. [참고](../JavaScript/ETC.md#🦋-esm-vs-cjs)
  - 방법2. `lazy(() => import("./Tooltip"))`의 동적 Import를 사용
    - Vite에서 동적 Import 사용 시, lazy와 같이 사용해야 함 [참고](../React/Grammar.md#suspense)
  - `require is not defined`에러 발생 시, 플러그인 사용(**vite-plugin-commonjs**)\
    - 단일레포인 경우, `vite-plugin-commonjs`플러그인을 사용하여 require 구문들을 ESM형식으로 변환
    - 멀티레포로 구현하여 모듈을 가져올 경우, 외부 모듈을
      1. vite로 만들어 빌드 시키거나
      2. babel을 사용해서 빌드 시키거나
      3. node를 다르게 실행하거나 [참고](https://github.com/philals/reading-exports-issue/commit/501151290df7d8f04d28c7cc092674c7f53e1201)
      4. webpack과 같은 번들러를 사용해서, ESM구문을 CJS로 바꿈

> pnpm의 모노레포로 구성하여, 외부 모듈내 의존성을 찾지 못하는 경우 `require is not defined`와 같은 에러가 발생
>
> 루트에 **.npmrc** 생성 후, `shamefully-hoist=true` 추가하여 `pnpm install`을 재실행

<br />

## [SSG](https://github.com/Daydreamer-riri/vite-react-ssg)

<br />

## Plugin

- vite-plugin-commonjs\
  require을 import로 변환
- @originjs/vite-plugin-commonjs
  - viteCommonjs
  - esbuildCommonjs
- vite-plugin-node-polyfills
  - nodePolyfills

<br />

### [vite-plugin-svgr](https://github.com/pd4d10/vite-plugin-svgr)

> 3 -> 4 버전 상승에 따른 변경점

```jsx
// v3
export {
  default as Icon_Alarm_Default,
  ReactComponent as Icon_Alarm,
} from "./alarm.svg";

<img src={Icon_Alarm_Default} />
<Icon_Alarm />
```

```jsx
// v4
export { default as Icon_Alarm } from "./alarm.svg?react";
<Icon_Alarm />;

// 또는
export { default as Icon_Alarm_Default } from "./alarm.svg";
<img src={Icon_Alarm} />;
```

<br />

### [vite-plugin-pwa](https://vite-pwa-org.netlify.app/)

[빌드 방식](https://vite-pwa-org.netlify.app/guide/cookbook.html)

- [types](https://github.com/vite-pwa/vite-plugin-pwa/blob/4abcd5462f7ce030c7418303ba5bc6d5dd5b2634/src/types.ts#L236)
- VitePWA

  - [manifest](https://vite-pwa-org.netlify.app/guide/pwa-minimal-requirements.html)
    - `false`: manifest.webmanifest 자동 생성 안할 경우
  - srcDir: injectManifest strategy인 경우
  - filename: injectManifest strategy인 경우
  - [strategies](https://vite-pwa-org.netlify.app/guide/service-worker-strategies-and-behaviors.html#service-worker-strategies)
    - [injectManifest](https://developer.chrome.com/docs/workbox/modules/workbox-build?hl=ko#injectmanifest): sw 직접 만드는 경우
    - [generateSW](https://developer.chrome.com/docs/workbox/modules/workbox-build?hl=ko#generatesw): default, sw 자동 생성
  - [injectRegister](https://vite-pwa-org.netlify.app/guide/register-service-worker.html#register-service-worker)
    - `inline`
    - `script`
    - `auto`: default
  - registerType

    - `autoUpdate`\
      injectManifest 인경우 [SW 업데이트 코드](https://vite-pwa-org.netlify.app/guide/inject-manifest.html#auto-update-behavior) 필요

      ```js
      import { clientsClaim } from "workbox-core";

      self.skipWaiting();
      clientsClaim();
      ```

    - `prompt`: default\
      injectManifest 인경우 [SW 업데이트 코드](https://vite-pwa-org.netlify.app/guide/inject-manifest.html#prompt-for-update-behavior) 필요

      ```js
      self.addEventListener("message", (event) => {
        if (event.data && event.data.type === "SKIP_WAITING")
          self.skipWaiting();
      });
      ```

  - workbox
  - [manifest](https://vite-pwa-org.netlify.app/guide/pwa-minimal-requirements.html#web-app-manifest)
  - injectManifest
    - injectionPoint
      - `undefined`: [precaching](https://vite-pwa-org.netlify.app/guide/inject-manifest.html#service-worker-code)을 사용하지 않는 경우
  - [devOptions](https://vite-pwa-org.netlify.app/guide/development.html#development)\
    enable sw on development
    - enabled
    - type
      - `classic`: [generateSW strategy](https://vite-pwa-org.netlify.app/guide/development.html#generatesw-strategy) 인 경우
      - `module`: [injectManifest strategy](https://vite-pwa-org.netlify.app/guide/development.html#injectmanifest-strategy) 인 경우

<br />

#### [virtual:pwa-register/react](https://vite-pwa-org.netlify.app/frameworks/react.html)

> PWA 업데이트 관련 동작 지정

- useRegisterSW

  - [immediate](https://vite-pwa-org.netlify.app/guide/auto-update.html#automatic-reload)

    - `true`: registerType가 autoUpdate인 경우

  - onNeedRefresh
  - onRegisteredSW
  - onOfflineReady
  - onRegisterError

<br />

#### Service Worker

<br />

#### Workbox

- workbox-precaching
  - [precacheAndRoute](https://vite-pwa-org.netlify.app/guide/inject-manifest.html#service-worker-code)

<br />

## [Vitest](https://vitest.dev/)

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

<br />

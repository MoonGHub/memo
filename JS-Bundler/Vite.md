# Bundler - Vite

- 플러그인
  - https://vite.dev/plugins/
  - https://github.com/vitejs/awesome-vite#plugins

## 환경변수

mode에 따라서 `.env.production`또는 `.env.development`와 자동으로 매칭되어 사용가능\
환경변수 명은 `VITE_` 접두사를 붙여야 노출이 되며, 이외는 내부적으로 사용

- dotenv를 따로 설치하지 않아도 됨

```
# .env.development

VITE_KEY1 = key1
KEY2 = key2
```

```javascript
console.log(import.meta.env.VITE_KEY1); // key1
console.log(import.meta.env.KEY2); // undefined
```

---

## 빌드

### mjs, cjs 각각 빌드

- vite.config.ts

```javascript
{
  build: {
		lib: {
			entry: 'src/index.ts',
			name: '@moon-libs/util',
			formats: ['es', 'cjs'],
			fileName: (format, entryName) => {
				const extension = format === 'es' ? 'mjs' : 'cjs';

				return `${entryName}.${extension}`;
			},
		},
		cssCodeSplit: true,
		rollupOptions: {
			external: [...Object.keys(devDependencies), /react.*/],
			output: {
				preserveModules: true,
				preserveModulesRoot: 'src',
			},
		},
	},
}
```

- package.json

```javascripton
{
  "main": "./dist/index.cjs",
  "module": "./dist/index.mjs",
  "types": "./dist/index.d.ts",
  "exports": {
    ".": {
      "require": "./dist/index.cjs",
      "import": "./dist/index.mjs",
      "types": "./dist/index.d.ts"
    }
  }
}
```

### cjs만 빌드

- vite.config.ts

```javascript
{
  build: {
		lib: {
			entry: 'src/index.ts',
			name: '@moon-libs/util',
			formats: ['cjs'],
		},
		cssCodeSplit: true,
		rollupOptions: {
			external: [...Object.keys(devDependencies), /react.*/],
			output: {
				preserveModules: true,
				preserveModulesRoot: 'src',
				entryFileNames: '[name].js',
			},
		},
	}
}
```

- package.json

```javascripton
{
  "main": "./dist/index.js",
  "types": "./dist/index.d.ts"
}
```

---

## Advanced

### Https 로컬 환경 설정

SSL 직접 생성

- 인증 파일 생성: `openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365`
- CSR의 경우 `vite.config.ts`에 설정 추가

  ```ts
  // ...
  import path from "path";
  import fs from "fs";

  export default defineConfig({
    // ...
    server: {
      https: {
        key: fs.readFileSync(path.resolve(__dirname, "key.pem")),
        cert: fs.readFileSync(path.resolve(__dirname, "cert.pem")),
      },
      host: true,
    },
  });
  ```

- SSR의 경우 `server.js`에 app.listen 대신 사용

  ```ts
  // ...
  import https from "https";

  // ...
  https
    .createServer(
      {
        key: await fs.readFile(path.resolve("./", "key.pem")),
        cert: await fs.readFile(path.resolve("./", "cert.pem")),
      },
      app
    )
    .listen(port, () => {
      console.log(
        `Server running at https://${
          isProduction ? hostname : "localhost"
        }:${port}`
      );
    });
  ```

자동 생성 플러그인 사용

- CSR에서 사용 - [vite-plugin-mkcert](https://github.com/liuweiGL/vite-plugin-mkcert)
- SSR에서 사용 - [@small-tech/https](https://codeberg.org/small-tech/https.git)

  ```ts
  //...
  import https from "@small-tech/https";

  //...
  https.createServer(app).listen(port, () => {
    console.log(
      `Server running at https://${
        isProduction ? hostname : "localhost"
      }:${port}`
    );
  });
  ```

---

## PBL

### vite.config.ts에서 package.json import하는 경우

tsconfig.node.json에 추가

```javascripton
{
  "compilerOptions": {
    "resolveJsonModule": true
  },
  "include": ["package.json"]
}
```

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

### SSR Import 관련 에러

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

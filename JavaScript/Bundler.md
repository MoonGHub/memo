# JavaScript - Bundler

- [Webpack](#webpack)
  - [Plugins](#plugins)
  - [Loaders](#loaders)
  - [devtool](#devtool)
  - [PBL](#pbl)
- [Vite](#vite)
  - [SSR 옵션](#ssr-옵션)

## [Webpack](https://webpack.js.org/guides/)

### [Plugins](https://webpack.js.org/plugins/)

- html-webpack-plugin
- uglifyjs-webpack-plugin
- clean-webpack-plugin
- tsconfig-paths-webpack-plugin
- fork-ts-checker-webpack-plugin
- webpack
  - ProvidePlugin

### [Loaders](https://webpack.js.org/loaders/)

- file-loader
- url-loader
- mini-css-extract-plugin

### devtool

![webpack_devtool](../assets/webpack_devtool.png)

### PBL

#### import시, 파일 확장자 생략

_Storybook설정 동일_

```javascript
// webpack.config.js
{
    test: /\.m?js/,
    resolve: {
      fullySpecified: false,
    },
},
```

---

## Vite

### SSR 옵션

```javascript
// vite.config.ts
{
  ssr: {
    optimizeDeps: {
      disabled: "build",  // 의존성 최적화 비활성화로 true는 build와 dev 모두 포함
      include: ["react-financial-charts"],
      // 모노레포에서 알아서 탐색이 되지만 번들이 되지않음
      // 연결된 패키지를 미리 번들화
      // ??? - 해당 디펜던시가 ESM로 내보내져야 함, 그렇지 않다면 명시 필요(강제 최적화?)
    },
    noExternal: ["react-financial-charts"],
    // 기본적으로 SSR은 디펜던시를 번들링에 포함하지 않음(초기 로딩이 빨라짐)
    // 설정 시, 외부화에서 제외, 번들링에 포함됨
  },
}
```

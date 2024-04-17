# React - Grammar

## 속성

- class -> **className**
- for -> **htmlFor**

<br />

## 렌더링

- 모든 값을 렌더링 하기전에 이스케이프시킴\
  -> XXS(cross-site-scripting) 공격 방지

### >18

<br />

### Suspense

> React.lazy 또는 비동기 렌더링이 있는 경우 사용

#### React.lazy

```jsx
// export default 인 경우
const Home = lazy(() => import("./routes/Home"));
const About = lazy(() => import("./routes/About"));

// export 인 경우
const Home = lazy(() =>
  import("./routes/Home").then((res) => ({ default: res.Home }))
);
const About = lazy(() =>
  import("./routes/About").then((res) => ({ default: res.About }))
);

<Suspense fallback={<div>Loading...</div>}>
  <Switch>
    <Route exact path="/" component={Home} />
    <Route path="/about" component={About} />
  </Switch>
</Suspense>;
```

<br />

### 코드 스플릿팅 및 청크

- Webpack의 경우

  - [참고1](https://webpack.js.org/guides/code-splitting/)
  - [참고2](https://www.zerocho.com/category/Webpack/post/58ad4c9d1136440018ba44e7)

- Vite의 경우
  - Lazy 사용 시, 해당 변수명으로 자동으로 chunk가 이루어짐

<br />

## PBL

- input에 value가 있고, onChange가 없을 때, read-only로 됨

# React - Grammar

## 특징

### 속성

> class -> className\
> for -> htmlFor

#### input

- onChange 없이 value만 지정 시 read-only로 됨

#### style

카멜형식의 스타일 객체를 전달

```jsx
<span style={{ fontSize: "10px" }}> ... </span>
```

<br />

### 렌더링

> 모든 값을 렌더링 하기전에 이스케이프시킴\
> -> XXS(cross-site-scripting) 공격 방지

#### Suspense

- fallback에 로딩 중 대신할 컴포넌트를 추가
- React.lazy를 사용하기 위해서 필요

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

#### 청크 및 스플릿팅

- Webpack의 경우

  - [참고1](https://webpack.js.org/guides/code-splitting/)
  - [참고2](https://www.zerocho.com/category/Webpack/post/58ad4c9d1136440018ba44e7)

- Vite의 경우
  - 같은 패키지에서 다른 모듈을 Lazy로 가져와도 chunk가 되지 않음
  - Lazy 사용 시, 해당 변수명으로 자동으로 chunk가 이루어짐

<br />

## ETC

### Words

- SyntheticEvent: 합성 이벤트

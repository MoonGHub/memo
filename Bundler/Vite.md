# Bundler - Vite

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

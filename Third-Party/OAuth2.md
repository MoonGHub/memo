# Third Party - OAuth2

## OAuth2

대부분 OAuth2만을 사용해도 기본적인 사용자 정보를 제공하는 API가 존재함

```mermaid
---
title: OAuth2 Flow Chart
---

flowchart TD
    A[사용자: 로그인 버튼 클릭] -->
    B[클라이언트: Authorization Request 전송<br/>→ 인증 서버 로그인 페이지로 리다이렉트] -->
    C[사용자: 로그인 정보 입력 후 인증 완료] -->
    D[인증 서버: Authorization Code 포함하여 설정된 URI로 리다이렉트] -->
    E[클라이언트: 리다이렉트된 페이지에서 Authorization Code를 파싱] -->
    F[클라이언트: 파싱된 Authorization Code로 백엔드 API 호출] -->
    G[백엔드: Authorization Code로 인증 서버에 Access Token 요청] -->
    H[인증 서버: Access Token을 발급하여 백엔드로 응답] -->
    I[백엔드: 발급된 토큰을 HttpOnly 쿠키로 설정하여 클라이언트로 응답] -->
    J[클라이언트: 정상응답에 대해 홈화면 또는 원래 화면으로 이동 → 로그인 완료] -->
    K[사용자: 이후 모든 요청에서 HttpOnly 쿠키가 자동 포함됨]
```

## OIDC(OpenID Connect)

기본적인 OAuth2(인가)에 더해,
추가적으로 사용자 정보(ID, 이메일 등)를 발급하는 절차(인증)

다양한 인증 시나리오(SSO, MFA 등)를 위해 사용

- SSO: Single Sign-On
- MFA: Multi-Factor Authentication, 다중 인증

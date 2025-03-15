# LightHouse

### HTTP/2를 통해 게재되지 않는 요청

- NGINX를 사용하는 경우

  ```
  server {
  listen 443 ssl http2;
  ...
  }
  ```

- OPNSense를 통해 SSL 설정을 하는 경우

  > Public Services의 443을 Listen하는 서비스에서\
  > HTTP(S) settings > Enable HTTP/2 > 체크

<br />

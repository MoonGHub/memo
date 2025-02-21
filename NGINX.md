# NGINX

- 설치 위치 경로 및 설정 파일
  - /etc/nginx/
  - /etc/nginx/nginx.conf
  - /etc/nginx/conf.d/default.conf
  - /usr/share/nginx/html

## Command

- `nginx -s reload`
- `nginx -t`
  syntax 체크

<br />

## default.conf

```conf
server {
  listen 80;

  location / {
    proxy_pass http://client;
  }

  location ~* ^/images {
    # 정규 표현식 사용 시, ~ 또는 ~* 와 함께 사용
    # ~: 대소문자 구분
    # ~*: 대소문자를 구분하지 않음(/Images, /IMAGES)
    proxy_pass http://client/images;
  }

  location /api {
    rewrite /api/(.*) /$1;
    # 브라우저 상의 URL은 변경없고, 내부적으로 /$1를 가르키게 됨
    rewrite /+(.*) /$1 break;
    #last: 다른 구문 실행하지 않고, 다른 location을 찾음
    #break: 경로 그만찾고, 다른 구문 실행
    proxy_pass http://api;
  }
}
```

### 정규표현식

- server_name

  - An asterisk can match several name parts. The name “\*.example.org” matches not only www.example.org but www.sub.example.org as well.
  - A special wildcard name in the form “.example.org” can be used to match both the exact name “example.org” and the wildcard name “\*.example.org”.
  - 정규식을 사용 시, `~^`로 시작하여 `$`을 끝으로 사용
    - ex)\
      `~^www\d+\.example\.net$;`
      `"~^(?<name>\w\d{1,3}+)\.example\.net$";` // location에서 $name 변수로 사용 가능 
      `~^(www\.)?(?<domain>.+)$;` // location에서 $domain 변수로 사용 가능

- location

<br />

## nginx.conf

<br />

## PBL

### 프록시 사용 시의 host 및 hostname 재정의

- [참고](https://sculove.github.io/post/nginx-reverse-proxy/)

프록시 된 노드 서버에서 `req.hostname` 및 `req.headers.host`가 프록시의 정보로 재정의 됨
따라서, 아래와 같은 설정이 필요

```conf
proxy_set_header    Host    $host
proxy_set_header    Hostname    $hostname;
```

### SEO

- `server_tokens off;`: `curl -I 도메인` 호출 시, 버전 노출이 되지 않음

# NGINX

## Command

- `nginx -s reload`

## default.conf

```conf
server {
  listen 80;

  location / {
    proxy_pass http://client;
  }

  location /api {
    rewrite /api(.*) /$1;
    rewrite /+(.*) /$1 break;
    #last: 다른 구문 실행하지 않고, 다른 location을 찾음
    #break: 경로 그만찾고, 다른 구문 실행
    proxy_pass http://api;
  }
}
```

## nginx.conf

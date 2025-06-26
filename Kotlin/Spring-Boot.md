# Kotlin - Spring Boot

- [build.gradle.kts 의존성](#buildgradlekts-의존성)
- [CLI](#cli)
  - [gradlew](#gradlew)
- [PBL](#pbl)
  - [VSCode spring-boot-devtools Live Reload 설정](#vscode-spring-boot-devtools-live-reload-설정)
    - [실행 및 디버그에서 버튼 실행](#실행-및-디버그에서-버튼-실행)
    - [CLI로 실행](#cli로-실행)

## build.gradle.kts 의존성

- `org.springframework.boot:spring-boot-starter-thymeleaf`: Thymeleaf 템플릿 파서 및 렌더링 엔진, ViewResolver 자동 설정
  - @Controller → `return "templateName"` 하면 `resources/templates/templateName.html`를 렌더링
- `org.thymeleaf.extras:thymeleaf-extras-springsecurity6`: 권한/인증 여부에 따른 분기처리 가능
  - `sec:authorize="isAuthenticated()"` 또는 `sec:authorize="!isAuthenticated()"`와 같이 사용
- `org.springframework.boot:spring-boot-devtools`: LiveReload

---

## CLI

### gradlew

- `./gradlew :{project}:bootRun`: 지정 프로젝트 실행
  - `--args='--spring.profiles.active={env}'`: 지정 env 프로파일로 실행 - application-{env}.yml
- `./gradlew build --warning-mode=all -t --parallel --build-cache --configuration-cache`: 실시간으로 변경사항을 빌드

---

## PBL

### VSCode spring-boot-devtools Live Reload 설정

**`spring.profiles.active`은 `local`으로 가정**

1. `build.gradle.kts`에 `developmentOnly("org.springframework.boot:spring-boot-devtools")` 종속성 추가
2. `application-local.yml`에 `spring.devtools.livereload.enabled: true` 추가
3. `SecurityConfig`에서 프로파일이 local인 경우 http 응답 헤더 설정
   ```java
   response.setHeader("Content-Security-Policy",
    "script-src 'self' 'unsafe-inline' http://localhost:35729; " +
    "connect-src 'self' ws://localhost:35729 ws://127.0.0.1:35729; "
    );
   ```
4. Thymeleaf의 head에 LiveReload server의 스크립트 삽입
   ```html
   <script
     th:if="${@environment != null and @environment.acceptsProfiles('local')}"
     src="http://localhost:35729/livereload.js"
   ></script>
   ```

#### 실행 및 디버그에서 버튼 실행

1. `.vscode/launch.json`(디버그 설정 파일) 구성

   ```javascript
   {
     "configurations": [
       {
         "type": "java",
         "name": "Spring Boot-Project",
         "request": "launch",
         "cwd": "${workspaceFolder}",
         "mainClass": "com.project.path",
         "projectName": "project_name",
         "args": ["--spring.profiles.active=local"],
         "envFile": "${workspaceFolder}/.env"
       },
       {
         "name": "Run gradle continuous",
         "type": "node-terminal",
         "command": "./gradlew build --warning-mode=all -t --parallel --build-cache --configuration-cache",
         "request": "launch",
         "cwd": "${workspaceFolder}"
       }
     ],
     "compounds": [
       {
         "name": "Auto build",
         "configurations": [
           "Run gradle continuous",
           "Spring Boot-Project"
         ],
         "stopAll": true
       }
     ]
   }
   ```

2. 실행 및 디버그에서 `Auto build`를 선택하여 실행

#### CLI로 실행

아래 두 명령어를 각각의 터미널로 실행

- `./gradlew :{project_name}:bootRun --args='--spring.profiles.active=local'`
- `./gradlew build --warning-mode=all -t --parallel --build-cache --configuration-cache`

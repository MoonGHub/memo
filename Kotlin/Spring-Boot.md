# Kotlin - Spring Boot

- [빌드 & 실행](#빌드--실행)
  - [빌드](#빌드)
  - [실행](#실행)
- [기본 어노테이션](#기본-어노테이션)
- [build.gradle.kts 의존성](#buildgradlekts-의존성)
  - [lombok](#lombok)
  - [thymeleaf](#thymeleaf)
- [CLI](#cli)
  - [gradlew](#gradlew)
- [PBL](#pbl)
  - [VSCode spring-boot-devtools Live Reload 설정](#vscode-spring-boot-devtools-live-reload-설정)
    - [실행 및 디버그에서 버튼 실행](#실행-및-디버그에서-버튼-실행)
    - [CLI로 실행](#cli로-실행)

---

## 빌드 & 실행

### 빌드

`./gradlew clean build`

- `clean`: 이전 빌드 결과 삭제

### 실행

jar 파일 실행

- `java -jar build/libs/my-app-0.0.1-SNAPSHOT.jar`
- `/usr/bin/java -jar {/path/to/jar}`

---

## 기본 어노테이션

- `@Component`: 해당 클래스를 자동으로 Bean으로 등록

---

## build.gradle.kts 의존성

키워드

- `implementation`: 일반 라이브러리 의존성, 빌드 결과물에 포함되며 런타임 사용 가능
- `annotationProcessor`: 애노테이션 기반 코드 생성을 위함, 컴파일 시점에만 사용되며 런타임에는 포함되지 않음
- `compileOnly`: 런타임에는 필요 없지만 코드에서 참조는 필요한 경우

### lombok

> org.projectlombok:lombok

반복적인 코드를 자동으로 생성해주며, 어노테이션 기반으로 작동

- `@Builder`: 빌더 패턴을 자동 생성/적용
- `@Getter`
- `@Setter`
- `@Slf4j`: 로그 객체(Logger)를 자동으로 추가, `log.info(...)` 사용 가능
- 생성자
  - `@NoArgsConstructor`
  - `@AllArgsConstructor`
  - `@RequiredArgsConstructor`: final 필드 또는 @NonNull 필드를 매개변수로 갖는 생성자를 자동 생성, DI의 생성자 자동 생성

### thymeleaf

- `org.springframework.boot:spring-boot-starter-thymeleaf`: Thymeleaf 템플릿 파서 및 렌더링 엔진, ViewResolver 자동 설정
  - `@Controller` → `return "templateName"` → `resources/templates/templateName.html`를 렌더링
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
         "type": "node-terminal",
         "name": "Run gradle continuous",
         "command": "./gradlew :{project_name}:build --warning-mode=all -t --parallel --build-cache --configuration-cache -x test",
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
- `./gradlew :{project_name}:build --warning-mode=all -t --parallel --build-cache --configuration-cache -x test`

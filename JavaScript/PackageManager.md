# Package Manager

## Yarn Berry

[참고](../JavaScript/NPM.md#yarn)

```text
1. 라이브러리 호이스팅이 안됨
2. 루트 패키지와 각 프로젝트 패키지간 충돌이 발생
```

<br />

## pnpm

[참고](https://pnpm.io/)

```text
1. 호이스팅 잘 됨
2. 빠름?
```

### 설치

1. `npm install -g pnpm`
2. `pnpm --version`
3. 루트의 package.json에 추가

   ```json
   {
     // ...
     "packageManager": "pnpm@7.29.2",
     "workspaces": ["apps/**/*", "libs/**/*", "tools/**/*"]
     // ...
   }
   ```

4. `pnpm-workspace.yaml` 생성 후, 아래 내용 추가
   ```yml
   packages:
     - "apps/**/*"
     - "libs/**/*"
     - "tools/**/*"
   ```

<br />

### 프로젝트 추가

1. 새 디렉토리 추가 및 해당 디렉토리에서 `npm init`
2. package.json에 프로젝트 이름 설정
3. npx를 사용하는 경우, script로 추가 후 루트 디렉토리에서 pnpm으로 실행
   `pnpm --filter {project_name} sb-init`
4. 루트 디렉토리에서 필요한 종속성들을 설치
   `pnpm --filter {project_name} add react react-dom @babel/cli`

<br />

### 명령어

- 프로젝트 리스트 보기

  - `pnpm recursive list`
  - `pnpm recursive list | grep @moon`

- 명령어 개별 실행

  - `pnpm --filter {project_name} exec {command}`

- 스크립트 전체 실행

  - `pnpm -r build`\
    build 스크립트가 포함된 모든 패키지의 build를 수행
  - `pnpm -r --parallel tscw`\
    비동기로 실행됨

- ETC
  - `pnpm dedupe`\
    Perform an install removing older dependencies in the lockfile if a newer version can be used.
    - --check: Check if running dedupe would result in changes without installing packages or editing the lockfile. Exits with a non-zero status code if changes are possible.
  - `pnpm store prune`\
    Removed all cached metadata files
  - `pnpm install --shamefully-hoist`
    - 각 프로젝트의 종속성들이 최상위의 **node_modules**에 설치됨
    - 서로 다른 버전의 종속성으로 호환 문제 시

<br />

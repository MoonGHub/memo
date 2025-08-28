# Javascript - Node

- [Built-in module](#built-in-module)
- [CLI Options](#cli-options)
  - [import시 파일 확장자 생략 및 디렉토리 import](#import시-파일-확장자-생략-및-디렉토리-import)
  - [import시, ts 및 tsx확장자 사용](#import시-ts-및-tsx확장자-사용)
- [nvm](#nvm)

## Built-in module

- path
  - join
  - resolve
- fs
  - readdirSync
  - stat
- process
  - exit
- util
  - promisify

---

## CLI Options

### import시 파일 확장자 생략 및 디렉토리 import

[참고](https://stackoverflow.com/questions/64449464/error-err-unsupported-dir-import-directory-import-when-attempting-to-start-no)

- `--experimental-specifier-resolution=node`
  - 지원 버전: `16.15.1`, `18.19.0`
  - 미지원 버전:
  - 미기능 버전: `22.14.0`, `23.10.0`
- `--es-module-specifier-resolution=node`
  - 지원 버전: `16.15.1`, `18.19.0`
  - 미지원 버전: `22.14.0`, `23.10.0`
  - 미기능 버전:

<br />

기능(지원)하지 않는 버전 해결

**Vite**

- `tsconfig.json`에서 `tsc-alias`이용

  ```json
  {
    "tsc-alias": {
      "resolveFullPaths": true
    }
  }
  ```

- `vite.config.ts`에서 직접 설정
  ```json
  {
    "resolve": {
      "alias": {
        "@": path.resolve(__dirname, './src'),
      }
    }
  }
  ```

### import시, ts 및 tsx확장자 사용

1. `pnpm add -D ts-node`
2. node cli 실행 시, `--loader ts-node/esm`

---

## nvm

> 여러 버전의 노드 버전 사용

1. brew install nvm
2. ~/.bash_profile 에 아래내용 추가
   ```shell
   export NVM_DIR="$HOME/.nvm"
     [ -s "/usr/local/opt/nvm/nvm.sh" ] && . "/usr/local/opt/nvm/nvm.sh"  # This loads nvmWrapperBox
     [ -s "/usr/local/opt/nvm/etc/bash_completion.d/nvm" ] && . "/usr/local/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion
   ```

- `nvm ls`
- `nvm install {version}`
- `nvm uninstall {version}`
- `nvm use {version}`
- `nvm alias default 16.15.1`: 디폴트 버전 변경

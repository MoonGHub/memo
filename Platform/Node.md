# Platform - Node

## built in modules

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

<br />

## cli options

### ESM의 파일 확장자 생략 및 디렉토리 import

[참고](https://stackoverflow.com/questions/64449464/error-err-unsupported-dir-import-directory-import-when-attempting-to-start-no)

- `--experimental-specifier-resolution=node`
  - 기능하는 버전: `16.15.1`, `18.19.0`
  - 기능하지 않는 버전: `22.14.0`
- `--es-module-specifier-resolution=node`
  - 기능하는 버전: `16.15.1`, `18.19.0`

> 기능하지 않는 버전 해결: `tsc-alias`의 resolveFullPaths 옵션 이용

<br />

### `--loader ts-node/esm`

> pnpm add -D ts-node

import시, ts 및 tsx확장자를 사용 할 수 있음

<br />

## 여러 버전 사용 - nvm

1. brew install nvm
2. ~/.bash_profile 에 아래내용 추가
   ```shell
   export NVM_DIR="$HOME/.nvm"
     [ -s "/usr/local/opt/nvm/nvm.sh" ] && . "/usr/local/opt/nvm/nvm.sh"  # This loads nvmWrapperBox
     [ -s "/usr/local/opt/nvm/etc/bash_completion.d/nvm" ] && . "/usr/local/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion
   ```

- nvm ls
- nvm install {version}
- nvm uninstall {version}
- nvm use {version}
- nvm alias default 16.15.1\
  디폴트 버전 변경

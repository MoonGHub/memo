# Node - Grammer

## Node Module

### path

> import path from 'path';

- join
- resolve

<br />

### fs

> import fs from 'fs';

- readdirSync
- stat

<br />

### process

> import process from 'process';

- exit

<br />

### util

> import util from 'util';

- promisify

<br />

## ESM

import/export 구문을 사용하는 법

- **.mjs**로 실행
- **package.json**에서 `type: "module"`을 설정

<br />

## 실행 옵션

### `--experimental-specifier-resolution=node`

CommonJS 모듈과의 상호 운용성을 개선하기 위해 도입된 옵션.\
이 옵션을 사용하면 ECMAScript 모듈의 import 구문에서 파일 확장자를 생략하거나, 상대 경로로 모듈을 찾을 때 더 유연하게 해석

<br />

### `--es-module-specifier-resolution=node`

ECMAScript 모듈의 해석을 지정하는 옵션, import시 파일 확장자 생략 가능

<br />

### `--loader ts-node/esm`

> pnpm add -D ts-node

import시, ts 및 tsx확장자를 사용 할 수 있음

<br />

### nvm

1. brew install nvm
2. ~/.bash_profile 에 아래내용 추가
   ```sh
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

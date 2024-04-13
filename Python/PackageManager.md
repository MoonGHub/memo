# Python - PackageManager

## pip

<br>

## [Poetry](https://python-poetry.org/docs/)

> Poetry requires Python 3.8+

<br />

### 특징

- 의존성 체킹으로 설치 가능 여부 확인
- pyproject.toml을 통해 관리
- 여러 Python버전에 대해 대응 가능
- 1.2.0> 부터 플러그인 사용 가능
- 의존성 설치 시, 자동으로 가상환경 생성

<br />

### [설치](https://python-poetry.org/docs/#installing-with-the-official-installer)

- `poetry --version`
- `poetry self update`

<br />

#### 오류

- No such file or directory: 'python'
  - `virtualenvs.in-project true`인 경우,\
    `poetry install`후 VSCODE의 새 환경의 작업영역 폴더로 선택하고 `.venv`를 삭제 시 발생
    - `VSCODE 팔레트 > Python: Select Interpreter > 재설정` 또는 `VSCODE 팔레트 > Python: Clear Workspace Interpreter Setting`
    - 터미널 재오픈
  - 또는 [python3를 python으로 지정](./Grammar.md#오류)
- This build of python cannot create venvs without using symlinks
  - `curl -sSL https://install.python-poetry.org | sed 's/symlinks=False/symlinks=True/' | python3 -`
- command not found: poetry
  - `echo -e '\nexport PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc`
  - `source ~/.zshrc`
- command not found: wc
  - `export PATH=%PATH:/bin:/usr/local/bin:/usr/bin`
  - ~/.zshrc 잘못 입력 수정
  - `source ~/.zshrc`
- NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+\
  poetry 자체에서 사용하는 버전 수정이 안됨..
  - `poetry self show | grep urllib3`

<br />

### [프로젝트 세팅](https://python-poetry.org/docs/basic-usage/#project-setup)

> `poetry new poetry-demo` or `poetry init`

<br />

#### [Config](https://python-poetry.org/docs/configuration/)

- `poetry config --list`
- `poetry config [options] [setting-key] [setting-value]`
- `poetry config virtualenvs.in-project true`\
  To store virtual environments in the project root

> poetry config로 지정 시 전역으로 설정됨, 각 프로젝트 별 poetry.toml으로 설정 가능
>
> ```toml
> # poetry.toml
>
> virtualenvs.in-project = true
> # or
> # [virtualenvs]
> # in-project = true
>
> ```

<br />

### 의존성 설치

> [기본적으로 가상환경 생성해줌](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment)

- `poetry install`\
  pyproject.toml을 통해 설치
- `poetry add <package_name>`
  - `--group`: 개발 의존성인 경우 `--group dev`또는 `-G dev`사용
- `poetry lock`\
  pyproject.toml을 통해 lock파일 수정

<br />

- `poetry show`\
  설치된 모든 패키지 표시
  - `--tree`
- `poetry update [package_name]`

<br />

#### [모노레포 의존성](https://python-poetry.org/docs/dependency-specification/#path-dependencies)

- VSCode Suggestion, 자동 완성

  - ~~로컬 의존성: settings.json에 `"python.analysis.extraPaths": ["common/test", "util/test", ...]` 추가~~
    - ~~루트 의존성이 아닌 모듈 내에서만 사용하는 추가 의존성 해결 불가~~
  - ~~**탐색기의 작업 영역에 해당 모듈 폴더 추가**~~
  - [Poetry Monorepo](https://marketplace.visualstudio.com/items?itemName=ameenahsanma.poetry-monorepo) Extension 설치

    - `python.analysis.extraPaths`를 실시간으로 변경해줌
    - 저장 시 포맷팅(isort, black) 오류로 아래 설정 필요

      ```json
      // vscode settings.json

      {
        "[python]": {
          "editor.formatOnSave": true,
          "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
            // explicit로 설정
          },
          "editor.defaultFormatter": "ms-python.black-formatter"
        },
        "isort.args": ["--profile", "black"]
      }
      ```

      ```toml
      # pyproject.toml

      [tool.isort]
      # profile = 'black'
      # 여기서는 profile 설정 제거
      ```

<br />

#### 가상 환경

- [`poetry shell`](https://python-poetry.org/docs/cli/#shell)\
  가상환경을 activation
- `poetry env info`
- `poetry env list`
- `poetry config virtualenvs.in-project true`\
  [가상환경이 프로젝트 내에 위치하도록 설정](https://python-poetry.org/docs/configuration/#virtualenvsin-project)\
  [기본 캐시 디렉토리](https://python-poetry.org/docs/configuration/#cache-dir)

  ```text
  If a virtual environment has already been created for the project under {cache-dir}/virtualenvs, setting this variable to true will not cause poetry to create or use a local virtual environment.

  In order for this setting to take effect for a project already in that state, you must delete the virtual environment folder located in {cache-dir}/virtualenvs.

  You can find out where the current project’s virtual environment (if there is one) is stored with the command poetry env info --path.
  ```

<br />

### [Command](https://python-poetry.org/docs/cli/)

- [run](https://python-poetry.org/docs/cli/#run)

  - `poetry run python -V`
  - `poetry run my-script`

    ```toml
    # pyproject.toml

    [tool.poetry.scripts]
    my-script = "my_module:main"
    ```

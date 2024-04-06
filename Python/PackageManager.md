# Python - PackageManager

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

#### [Config](https://python-poetry.org/docs/configuration/)

- `poetry config --list`
- `poetry config [options] [setting-key] [setting-value]`

<br />

- `virtualenvs.in-project`\
  To store virtual environments in the project root

<br />

#### Error

- This build of python cannot create venvs without using symlinks
  - `curl -sSL https://install.python-poetry.org | sed 's/symlinks=False/symlinks=True/' | python3 -`
- command not found: poetry
  - `echo -e '\nexport PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc`
  - `source ~/.zshrc`
- command not found: wc
  - `export PATH=%PATH:/bin:/usr/local/bin:/usr/bin`
  - ~/.zshrc 잘못 입력 수정
  - `source ~/.zshrc`
- NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+

<br />

### [프로젝트 세팅](https://python-poetry.org/docs/basic-usage/#project-setup)

> `poetry new poetry-demo` or `poetry init`

<br />

### 의존성 설치

> [기본적으로 가상환경 생성](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment)

- `poetry install`\
  pyproject.toml을 통해 설치
- `poetry add <package_name>`
  - `--group`
- `poetry lock`\
  pyproject.toml을 통해 lock파일 수정

<br />

- `poetry show`\
  설치된 모든 패키지 표시
  - `--tree`
- `poetry update [package_name]`

<br />

#### 가상 환경

- [`poetry shell`](https://python-poetry.org/docs/cli/#shellhttps://python-poetry.org/docs/cli/#shell)\
  가상환경을 activation
- `poetry env info`
- `poetry env list`
- `poetry config virtualenvs.in-project true`\
  가상환경이 프로젝트 내에 위치하도록 설정, [참고](https://python-poetry.org/docs/configuration/#virtualenvsin-projecthttps://python-poetry.org/docs/configuration/#virtualenvsin-project)

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

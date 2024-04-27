# Python - Grammar

- [문법](https://docs.python.org/3/reference/index.html)

<br />

## [type](https://docs.python.org/3.13/library/stdtypes.html#)

- `int`
- `float`
- `str`
- `bool`
- `list`
- `tuple`: 불변(immutable)
- `dict`
- `set`
- `None`
- [from typing](https://docs.python.org/3/library/typing.html#)
  - `Any`

<br />

## 설치

- `python3 -m pip install --upgrade pip`\
  pip 업그레이드
- `python3 -m venv <가상환경명>`\
  가상환경 생성
- `. ./env/bin/activate`\
  가상 환경 활성화\
  가상환경이 활성화 된 상태에서 패키지를 설치하면 .venv 내부에 패키지가 설치

<br />

### 오류

- command not found: python
  - `echo -e '\nalias python="python3"' >> ~/.zshrc`
  - `. ~/.zshrc`

<br />

### [Anaconda](https://www.anaconda.com/download#downloads)

![image](/assets/python_conda.png)

- `conda info --envs`

<br />

### pip

- `pip show <모듈명>`
- `pip list | grep -i 패키지`
- `pip install 패키지[==버전]`
  - ex)\
    `pip install MySQL_python==1.2.2`
- `pip install 패키지[Optional Libraries]`
  - ex)\
     `pip install passlib[bcrypt]`
- `pip install -r requirements.txt`
- `pip freeze > requirements.txt`\
  패키지 백업

<br />

## Linting

- [pylint](https://pylint.readthedocs.io/en/stable/)
  - [옵션 참고](https://pylint.pycqa.org/en/latest/user_guide/configuration/all-options.html)
  - [파일 설정](https://pylint.pycqa.org/en/latest/user_guide/usage/run.html#command-line-options)
  - [설정 참고](https://www.codeac.io/documentation/pylint-configuration.html)
- [flake8](https://flake8.pycqa.org/en/latest/#)
  - [옵션 참고](https://flake8.pycqa.org/en/latest/genindex.html)
  - [파일 설정](https://flake8.pycqa.org/en/latest/user/configuration.html#configuration-locations)
  - pycodestyle: PEP8 준수 여부 검사 (오류코드 : E* / W* / N8\*\*)
  - PyFlakes: 오류, 일반적인 관행 위반 등 (오류코드 : F\*\*\*)
  - McCabe complexity checker(복잡도 검사): (오류코드 : C9\*\*\*)
  - 체킹만 하고 변환은 black를 통하여 함
  - plugin
    - [flake8-annotations](https://pypi.org/project/flake8-annotations/)\
      타입 체크\
      설치만 하면 됨
- [black](https://black.readthedocs.io/en/stable/#)
  - [파일 설정 - pyproject.toml](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file)
  - [설정 참고](https://github.com/psf/black/blob/main/pyproject.toml)
  - [다른 툴과 함께 사용](https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html#)
- [isort](https://pycqa.github.io/isort/)
  - [옵션 참고](https://pycqa.github.io/isort/docs/configuration/options.html)

> 코드 위 `# fmt: off` 주석 추가 시 포맷팅 생략

<br />

## Generic

```py
from typing import (
    Generic,
    TypeVar,
)

T = TypeVar("T")


@dataclass
class A(Generic[T]):
    data: T


@dataclass
class B:
    num: int


data: A[B] = A(B(10))
```

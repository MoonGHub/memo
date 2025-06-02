# Platform - Mac

## Shortcut

- `Ctrl Cmd Space`: 이모티콘
- `Ctrl Cmd f`: 전체화면 토글\
- `Cmd Shift .`: 숨김 파일 토글
- `Cmd shift 3`: 화면 전체 캡쳐
- `Cmd shift 4`: 화면 부분 캡쳐
- `shift 드래그`: 좌우 스크롤
- `Cmd ,`: 환경설정
- `Cmd down`: 폴더 진입
- `Cmd i`: 파일/폴더 정보
- `Space`: 파일 미리보기
- `Ctrl Space`: 키보드 국가 변환
- `Ctrl Shift r`: 일본어 한자 재변환

<br />

## Terminal

### Commands

- `open library`\
   해당 위치의 library폴더를 finder로 오픈

### 꾸미기

#### 터미널 - ohmyzsh, 테마

**실리콘 맥의 경우, brew사용 시 Prefix로 `arch -arm64` 추가**

1. `brew install wget`
2. `sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"`
   - https://ohmyz.sh/#install
3. **~/.zshrc.pre-oh-my-zsh** 기존 내용 **~/.zshrc**에 복사
4. theme 을 agnoster로 변경 후 `cmd ,`로 색상 변경
5. `vim ~/.oh-my-zsh/themes/agnoster.zsh-theme` 에서 **_prompt_context() {_** 검색\
   **_prompt_segment black default "%(!.%{%F{yellow}%}.)%n@%m"_** 를 아래로 치환\
   **_prompt_segment black default "%(!.%{%F{yellow}%}.)%n"_**
6. `brew install zsh-syntax-highlighting`
7. **~/.zshrc** 내 아래 추가\
   `source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh`

#### 터미널 - git 자동 완성

VSCODE 1.98.0 - Terminal IntelliSense

- [참고](https://fig.io/docs/getting-started)
- [참고](https://github.com/withfig/autocomplete)

### PBL

#### agnoster.zsh-theme:91: parse error near `<<<

- [참고](https://shuiky.tistory.com/entry/agnosterzsh-theme91-parse-error-near)

**_해결_**

```shell
cd $ZSH
git config core.autocrlf input
git rm --cached -r .
git reset --hard
```

<br />

## chrome

### Shortcut

- `Cmd Shift f`: 전체화면에서 툴바 토글
- `Cmd Option up`: 주소창 토글

---

## ETC

### 🦋 D2Coding 폰트 설치

https://github.com/naver/d2codingfont\
터미널 및 vscode 적용(vscode의 세팅에서 Font Family 검색 후 D2coding 설정)

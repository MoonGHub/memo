# OS - Mac

## Shortcut

- `Ctrl Cmd Space`: 이모티콘
- `Shift Cmd .`: 숨김 파일 토글

---

### 🦋 Terminal 꾸미기

실리콘 맥의 경우 `arch -arm64`를 brew실행 시, Prefix로 추가

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

### 🦋 D2Coding 폰트 설치

https://github.com/naver/d2codingfont\
터미널 및 vscode 적용(vscode의 세팅에서 Font Family 검색 후 D2coding 설정)

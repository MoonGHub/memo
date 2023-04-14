# IDE - VSCode

### 🦋 Command Palette

- `Configure Display Language`: 언어 변경
- `Color Theme`: 테마 변경

---

`F1`: Command Palette

- `>`: Run Commands
- `:`: 행 이동
- `?`: 명령 목록 확인

<br />

## Windows Shortcut

- Origin

  - `Ctrl PgUp`: Move Previous Tab
  - `Ctrl PgDown`: Move Next Tab
  - `Alt Up`: Move Left Terminal
  - `Alt Down`: Move Right Terminal
  - `Ctrl Home/End`: Cursor Top/Bottom
  - `Home/End`: Cursor Home/End
  - `Alt Shift Down/Up`: 행 복사
  - `Alt Down/Up`: 행 이동
  - `Ctrl /`: 행 주석
  - `Alt Shift a`: 블록 주석
  - `Ctrl d`: 커서 단어 반복 선택
  - `Ctrl Shift Alt Up/Down`: 커서 여러개 생성
  - `Alt Shift Drag`: 마우스 드래그 선택
  - `Alt Click`: 멀티 커서
  - `Ctrl h`: Find and Replace
  - `Ctrl g`: Go to Line
  - `Ctrl i`: Suggest
  - `Ctrl .`: Quick Fix
  - `Ctrl u`: 해당 파일에서의 이전 커서로 이동
  - `Ctrl -`: 이전 작업하던 곳으로 커서 이동
  - `Ctrl [ 또는 ]`: 들여쓰기
  - `Ctrl Shift c`: Open New External Terminal
  - `Ctrl Shift [ / ]`: 코드 접기/펼치기
  - `Ctrl Shift \`: 블럭 앞 뒤 이동
  - `Ctrl Shift t`: 방금 닫은 파일 오픈
  - `Ctrl F2`: 해당 커서의 단어 모두 선택
  - `F2`: 참조되는 변수명 모두 변경
  - `F8`: 해당 페이지의 에러부로 이동
  - `F12`: 해당 변수/함수 선언부 확인
  - Layout Toggle
    - `Ctrl Shift u`: OUTPUT
    - `Ctrl Shift m`: PROBLEMS

- Custom
  - `Windows Shift \`: Split Editor ?
  - `Windows \`: Split Terminal ?
  - `Ctrl Enter`: Git - Open File
  - `Ctrl n`: New file
  - `Ctrl Alt s`: Save Without Formatting

<br />

## Mac Shortcut

- Origin

  - `Cmd \`: Split Editor/Terminal
  - `Option Shift Down/Up`: 행 복사
  - `Option Down/Up`: 행 이동
  - `Cmd Shift u`: OUTPUT 콘솔 토글
  - `Cmd /`: 행 주석
  - `Option Shift a`: 블록 주석
  - `Cmd 방향키`: 커서 끝
  - `Option Shift Drag`: 마우스 드래그 선택
  - `Option Click`: 멀티 커서
  - `Ctrl g`: Go to Line
  - `Cmd Shift c`: Open New External Terminal
  - `Option Cmd Right/Left`: Move Right/Left Terminal
  - `Cmd i`: Suggest
  - `Cmd .`: Quick Fix
  - `Cmd u`: 해당 파일에서의 이전 커서로 이동
  - `Ctrl -`: 이전 작업하던 곳으로 커서 이동
  - `Cmd [ 또는 ]`: 들여쓰기
  - `Cmd Shift t`: 방금 닫은 파일 오픈
  - `Cmd F2`: 해당 커서의 단어 모두 선택
  - `F2`: 참조되는 변수명 모두 변경
  - `F8`: 해당 페이지의 에러부로 이동
  - `F12`: 해당 변수/함수 선언부 확인
  - Layout Toggle
    - `Cmd Shift u`: OUTPUT
    - `Cmd Shift m`: PROBLEMS

- Custom
  - `Ctrl d`: 커서 단어 반복 선택
  - `Ctrl n`: New file
  - `Ctrl Cmd s`: Save Without Formatting
  - `Ctrl Enter`: Git - Open File
  - `Ctrl Shift Cmd Up/Down`: 커서 여러개 생성
  - `Ctrl h`: Find and Replace
  - `Ctrl Shift [ / ]`: 코드 접기/펼치기
  - `Ctrl Shift \`: 블럭 앞 뒤 이동

<br />

## Extension Shortcut

- Code runnder
  - `Ctrl Alt(Cmd) n`: Run Code

<br />

## 설정(settings.json)

### 타입스크립트를 사용 할 경우, 작성한 alias paths를 자동완성으로 사용

shortest: 상대경로와 alias로 지정한 paths 중 비교하여 짧은 경로를 Sugesstions에 표시

방법 1. sttings.json에 아래 구문 추가\
 `"typescript.preferences.importModuleSpecifier": "shortest"`

방법 2. settings에서 **typescript importModuleSpecifier** 검색 후,\
 TypeScript > Preferences: Import Module Specifier 값을 `shortest`로 변경

# JavaScript - package.json

- files: 패키지가 의존성으로 설치될 때 같이 포함될 파일들의 배열. 생략 시, 자동 제외로 설정된 파일을 제외한 모든 파일이 포함
- main: 프로그램의 기본 진입 점(entry point)를 지정
- dependencies: 패키지의 배포 시 포함될 의존성 모듈을 지정
- devDependencies: 패키지의 개발 시 사용될 의존성 모듈을 지정.(배포 시 미포함)
  - ~version: 버전과 대략 동일, 버그 수정 릴리즈
  - ^version: 버전과 호환, 이전 버전과 호환, 버그 수정 릴리즈
- bundledDependencies:
  - 패키지를 게시할 때 번들로 묶을 패키지 이름을 배열로 지정
  - npm 패키지를 로컬에서 보존해야 하거나 단일 파일 다운로드를 통해 사용할 수 있는 경우,\
    npm pack을 실행하여 패키지를 <name>-<version>.tgz 형태의 tarball 파일로 묶을 수 있음
- engines: 패키지가 작동하는 Node 버전을 지정
- private: 개인 저장소의 우연한 발행을 방지하기 위해 npm에서 패키지의 공개 여부를 지정

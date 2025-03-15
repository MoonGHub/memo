# BLOG - Jekyll

<br />

# Mac

## 설치 및 실행

1. `xcode-select --install`
2. [Ruby 및 Jekyll 설치](https://jekyllrb-ko.github.io/docs/installation/macos/)
3. `sudo bundle`\
   실행하는 디렉토리의 Gemfile을 타겟으로 의존성이 있는 모듈들을 설치
4. `jekyll serve`

## PBL

**실리콘 맥의 경우, brew사용 시 Prefix로 `arch -arm64` 추가**

- 에러: rbenv로 특정 버전의 ruby 설치 시, BUILD FAILED (macOS 12.3 using ruby-build 20221004)\
  `brew install readline openssl`
- `chmod -R 0644 *`: 권한 부여
- 설치된 번들 모두 제거

  ```shell
  bundle list | ruby -e 'ARGF.readlines[1..-1].each {|l| g = l.split(" "); puts "Removing #{g[1]}"; `gem uninstall --force #{g[1]} -v #{g[2].gsub(/\(|\)/, "")}`; }'
  ```

- 에러: require': cannot load such file -- google/protobuf_c\
  ruby ver2.6.8(m1)에서 발생 - [참고](https://github.com/protocolbuffers/protobuf/issues/8199)
  1. `sudo gem uninstall google-protobuf`\
     All versions를 제거
  2. `sudo gem install google-protobuf -v 3.15.8 --platform=ruby`
  3. `bundle config set force_ruby_platform true`

<br />

# Windows

PBL# Mobile - React Native

- [Android](#android)
  - [키스토어 해쉬](#키스토어-해쉬)
  - [디버깅](#디버깅)
  - [APK 생성(aab -> apk) - bundletool을 이용](#apk-생성aab---apk---bundletool을-이용)
- [IOS](#ios)
  - [디버깅](#디버깅-1)
- [빌드](#빌드)
  - [Android](#android-1)
  - [IOS](#ios-1)
- [배포](#배포)
  - [IOS](#ios-2)
  - [스토어 배포 이슈](#스토어-배포-이슈)
    - [AOS - App must support 16 KB memory page sizes](#aos---app-must-support-16-kb-memory-page-sizes)
- [PBL](#pbl)
  - [캐시 제거 및 패키지 인식 오류](#캐시-제거-및-패키지-인식-오류)
    - [Android](#android-2)
    - [IOS](#ios-3)
    - [새 프로젝트 생성 시](#새-프로젝트-생성-시)
  - [App Center](#app-center)
  - [com.kakao.sdk.common.model.AuthError: Android keyHash validation failed. (AOS 배포앱에서만)](#comkakaosdkcommonmodelautherror-android-keyhash-validation-failed-aos-배포앱에서만)

---

## Android

- Android SDK 경로: **~/Library/Android/sdk/emulator**
- 에뮬레이터 실행
  1. `emulator -list-avds`
  2. `emulator -avd {기기명} -gpu {type}`
     - type : auto, host, mode, mesa

### 키스토어 해쉬

React Native 0.60.x 부터는 템플릿(project/android/app)에 기본적으로 디버그 키스토어(debug.keystore)가 포함

- `keytool -exportcert -alias androiddebugkey -keystore ~/.android/debug.keystore -storepass android -keypass android | openssl sha1 -binary | openssl base64`

### 디버깅

PC와 연결 후 아래 명령어 실행

```shell
adb devices
# react-native run-android --appIdSuffix 'dev' --deviceId LGMV300Sf73feca1
adb shell 또는 adb -s [device_name] shell
adb logcat | grep io.cyclub.app.dev
```

### APK 생성(aab -> apk) - [bundletool](https://developer.android.com/tools/bundletool?hl=ko)을 이용

설치

- [다운로드](#https://github.com/google/bundletool/releases)
- `~/.zshrc`에 추가 `alias bundletool='java -jar /Users/moong/Documents/cli-tools/bundletool-all-1.18.1.jar'`

**debug**

```shell
cd {prj_root}/android/app/build/outputs/bundle/debug

# apk 생성
# React Native 0.60.x 부터는 템플릿(project/android/app)에 기본적으로 디버그 키스토어(debug.keystore)가 포함
bundletool build-apks --ks-pass 'pass:android' --bundle app-debug.aab --output app.apks --ks debug.keystore --ks-key-alias androiddebugkey --overwrite

# 에뮬레이터 설치
bundletool install-apks --apks app.apks
```

**release**

```shell
cd {prj_root}/android/app/build/outputs/bundle/release
# 또는 cd {prj_root}/android/app/build/outputs/bundle/googlePlayRelease

# apk 생성
# app-release.aab 또는 googlePlay-release.aab
bundletool build-apks --ks-pass 'pass:{키스토어 패스워드}' --bundle app-release.aab --output app.apks --ks {키스토어 파일 명}.keystore --ks-key-alias {키스토어 Alias} --overwrite

# 에뮬레이터 또는 실 기기에 설치
bundletool install-apks --apks app.apks

# 실 기기에 설치
adb install -r app-release.apk
```

**임시 apk 파일 삭제 참고**

The APKs have been extracted in the directory: /var/folders/yg/3y40k7_53tj_2k69j0hmvqrc0000gn/T/4701178596781160357
해당 경로는 `echo $TMPDIR`

---

## IOS

- 시뮬레이터 실행: `open -a Simulator`
- Xcode 업데이트
  - `brew install mas`
  - `mas search Xcode`
  - `mas install xxxxxxx`

### 디버깅

---

## 빌드

### Android

- `react-native build-android --mode=release`

**아래와 같이 직접 빌드 시, 여러 이슈 발생.. 따라서 RN CLI를 사용 할 것**

- `./gradlew assembleRelease` or `./gradlew assembleDebug`

  - apk빌드
  - assembleRelease의 경우, signingConfigs 및 buildTypes에 keystore가 필요

- `./gradlew bundleRelease`
  - .aab 빌드

### IOS

---

## 배포

- 빌드 버전
  - AOS: `versionCode`
  - IOS: `CFBundleVersion`, `CURRENT_PROJECT_VERSION`
- 사용자 표시 버전
  - AOS: `versionName`
  - IOS: `CFBundleShortVersionString`, `MARKETING_VERSION`

### IOS

**버전 설정**

- `1.06`은 `1.6`과 같음
- 세자리 가능
- 버전이 다르면, 빌드 넘버는 중복 가능
- 배포 버전은 기업로드 버전 이상이어야 함

### 스토어 배포 이슈

#### AOS - App must support 16 KB memory page sizes

> From Nov 1, 2025, if your app updates do not support 16 KB memory page sizes, you won't be able to release these updates.

해결: [RN 버전 업데이트 >= 0.77](https://reactnative.dev/blog/2025/01/21/version-0.77#android-version-15-support--16kb-page-support)

---

## PBL

### 캐시 제거 및 패키지 인식 오류

```shell
watchman watch-del-all
npm cache clean --force
rm -rf ./node_modules/
rm -rf $TMPDIR/haste-map-*
rm -rf $TMPDIR/metro-cache # 또는 rm -rf /tmp/metro-*
yarn install
```

#### Android

```shell
cd ./android
./gradlew --stop
./gradlew clean

# 삭제됨
# ./gradlew cleanBuildCache

```

#### IOS

IOS pod 삭제, 클린 후 설치\
(실리콘 맥의 경우 arch -arm64)

```shell
pod deintegrate
pod cache clean --all
pod install
```

#### 새 프로젝트 생성 시

```shell
rm -rf ~/Library/Developer/Xcode/DerivedData 1938
rm -rf ~/.gradle/caches
```

<br />

### App Center

- codepush
  - `appcenter codepush release-react -a {userName}/{AppName} -d {deployType}`
    - userName: moong_push
    - AppName: App Name
    - deployType: Production/Staging[/...CustomName]

<br />

### com.kakao.sdk.common.model.AuthError: Android keyHash validation failed. (AOS 배포앱에서만)

원인

- 로컬(개발, 운영)에서는 로컬 키스토어 파일의 해쉬값이 전송되는게 맞음
- 배포시에는 `Signing by Google Play`로 플랫폼에서 적용되는 해쉬값이 전송되므로, 해당 배포용 키해시도 추가해줘야함

해결

1. Google play store > App integrity > App signing > App signing key certificate
2. `SHA-1 certificate fingerprint`의 값을 [Hex to Base64](https://base64.guru/converter/encode/hex)로 변환하여 결과 값을 추가

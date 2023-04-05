# React Native - PBL

## 캐시 제거 및 패키지 인식 오류

```shell
watchman watch-del-all
npm cache clean --force
rm -rf ./node_modules/
rm -rf $TMPDIR/haste-map-*
rm -rf $TMPDIR/metro-cache # 또는 rm -rf /tmp/metro-*
yarn install
```

### ANDROID

```shell
cd ./android
./gradlew clean

# In MacOs
./gradlew --stop
./gradlew cleanBuildCache
```

<br />

### IOS

IOS pod 삭제, 클린 후 설치\
(실리콘 맥의 경우 arch -arm64)

```shell
pod deintegrate
pod cache clean --all
pod install
```

<br />

## 새 프로젝트 생성 시

```shell
rm -rf ~/Library/Developer/Xcode/DerivedData 1938
rm -rf ~/.gradle/caches
```

---

## Mac

- Android SDK 경로: **~/Library/Android/sdk/emulator**
- Emulator를 CLI로 실행
  1. `emulator -list-avds`
  2. `emulator -avd {기기명} -gpu {type}`
     - type : auto, host, mode, mesa

---

## Android

### 디버깅

PC와 연결 후 아래 명령어 실행

```shell
adb devices
# react-native run-android --appIdSuffix 'dev' --deviceId LGMV300Sf73feca1
adb shell 또는 adb -s [device_name] shell
logcat | grep io.cyclub.app.dev
```

<br />

### APK 생성(aab -> apk)

aab파일을 bundletool을 이용해 apk를 생성 및 에뮬레이터에 설치

debug

```shell
cd {prj_root}/android/app/build/outputs/bundle/debug

# apk 생성
bundletool build-apks --ks-pass 'pass:{키스토어 패스워드}' --bundle app-debug.aab --output app.apks --ks debug.keystore --ks-key-alias debugkeystore --overwrite

# 에뮬레이터 설치
bundletool install-apks --apks app.apks
```

<br />

release

```shell
cd {prj_root}/android/app/build/outputs/bundle/release
# 또는 cd {prj_root}/android/app/build/outputs/bundle/googlePlayRelease

# apk 생성
# app-release.aab 또는 googlePlay-release.aab
bundletool build-apks --ks-pass 'pass:{키스토어 패스워드}' --bundle app-release.aab --output app.apks --ks debug_key.keystore --ks-key-alias debugkeystore --overwrite

# 에뮬레이터 설치
bundletool install-apks --apks app.apks
```

---

react-native-image-picker : 카메라 및 이미지 라이브러리
react-native-device-info : 디바이스 관련 정보
react-native

> Animated : 애니메이션 처리

    area = new Animated.ValueXY(0, 0) 	// 초기값,
    				.Value(opacity)
    Animated.spring(area, { toValue: {x :, y : }).start();
    	// spring대신 timing … 옵션 문서 참고( duration, delay 등 ..)
    render에서는 <Animated.View style={area.getLayout()} > 안에 선언
    	// area.interpolate : 동시 애니메이션 효과, inputRange : 기본 효과, outputRange: 추가 효과 (배열 end-start 순, 각 인덱스는 매칭)
    	// transform: [{ translateY: area.interpolate({ inputRage: [ ,…], outputRange: [ ,…] }) }]
    Animated.sequence([ Animated.timing(…), Animated.spring(…), … ])	// 순차 실행
    Animated.parallel([ Animated.spring(…) , …]) // 동시 실행

> Platform

    …Platform.select({ ios: {스타일}, android: {스타일} })	// 플랫폼별 스타일 지정

> Dimensions

    .get(‘screen’)		// 화면전체
    .get(‘window’)	// 소프트 버튼바 미포함 등..

- react-native-debugger
  - Release > 응용프로그램 > 실행
  - 시뮬레이터(cmd d: ios, cmd m: and) > Debug
  -

window.addEventListener('scroll', function(e) {
var timer = false;
if (timer !== false) {
clearTimeout(timer);
}
timer = setTimeout(function() {
var scroll = $(window).scrollTop();
TweenLite.to('.contents**bg--front', 1, {
y: scroll / 4
});
TweenLite.to('.contents**bg--back', 1, {
y: scroll / 10
});
}, 3);
});

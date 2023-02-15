# React Native - PBL

### 🦋 캐시 제거 및 패키지 인식 오류

```shell
watchman watch-del-all
npm cache clean --force
rm -rf ./node_modules/
yarn install
rm -rf /tmp/metro-*
```

---

## Mac

- Android SDK 경로: **~/Library/Android/sdk/emulator**
- Emulator를 CLI로 실행
  1. `emulator -list-avds`
  2. `emulator -avd {기기명} -gpu {type}`
     - type : auto, host, mode, mesa

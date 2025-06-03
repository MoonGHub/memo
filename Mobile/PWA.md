# Mobile - PWA

- [참고 - mdn](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
- [참고 - web.dev](https://web.dev/articles/pwa-checklist?hl=ko)
- [참고 - MS](https://learn.microsoft.com/ko-kr/microsoft-edge/progressive-web-apps-chromium/how-to/best-practices)

## Installability

`<link rel="manifest" href="manifest.json" />`

- If the PWA has more than one page, every page must reference the manifest in this way.
- Must be served over HTTPS(localhost, 127.0.0.1 and file:// are also considered secure.)
- Must include a [service worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) with a [fetch event handler](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/fetch_event) that provides a basic offline experience.

### Required manifest members

- `name`
- `icons`
  - [참고(vite-plugin-pwa)](https://vite-pwa-org.netlify.app/assets-generator/#pwa-minimal-icons-requirements)
- `start_url`
- `display` and/or `display_override`
  - fullscreen: 상태표시줄도 제외한 전체화면으로 표시

[every member](https://developer.mozilla.org/en-US/docs/Web/Manifest)

<br />

- share_target\
  시스템의 공유 대화상자에 노출
- [file_handlers](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Associate_files_with_your_PWA)\
  PWA로 지정 파일 처리 가능

<br />

## 서비스워커

- [생명 주기](https://web.dev/articles/service-worker-lifecycle?hl=ko)
- [등록 처리](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers#registering_your_worker)
- [새로운 등록 처리](https://web.dev/articles/service-worker-lifecycle?hl=ko#handling_updates)

<br />

## [Workbox](https://developer.chrome.com/docs/workbox?hl=ko)

...

<br />

## [Caching](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching#cache_first_with_cache_refresh)

install 이벤트는 클라이언트를 제어하기 전에 필요한 모든 것을 캐시할 수 있는 기회입니다.

- [참고](https://web.dev/articles/service-worker-lifecycle?hl=ko#install)

<br />

## 지원 기능

- [Offline and background operation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation)
- [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
- [Background Synchronization API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API)
- [Background Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Fetch_API)
- [Periodic Background Synchronization API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Periodic_Background_Synchronization_API)
- [Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API)
- [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API)

<br />

- [mac 또는 윈도우 타이틀바 커스텀](https://web.dev/articles/window-controls-overlay?hl=ko)
  - "display_override": ["window-controls-overlay"]

### [Provide an app-like experience](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Best_practices#provide_an_app-like_experience)

- [standalone display mode](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Create_a_standalone_app)
- [Define your app icon](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons)
- [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)
- [Customize your app's theme and background colors](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Customize_your_app_colors)

<br />

- [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API)
- [file_handlers](https://developer.mozilla.org/en-US/docs/Web/Manifest/file_handlers)
- [Display badges](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Display_badge_on_app_icon)
- [data sharing between apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Share_data_between_apps)

<br />

### manifest

### 노치영역 제어

도큐먼트 영역을 노치영역까지 확대

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1.0, viewport-fit=cover"
/>
```

노치영역을 아래와 같은 `safe-area-inset-*`로 제어

```css
body {
  padding-top: env(safe-area-inset-top, 0);
  padding-left: env(safe-area-inset-left, 0);
  padding-right: env(safe-area-inset-right, 0);
  padding-bottom: env(safe-area-inset-bottom, 0);
}
```

### Triggering the install prompt

This is not supported on iOS.

- [beforeinstallprompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeinstallprompt_event)

<br />

## 빌드, 배포

### packaging and publishing

[PWABuilder](https://docs.pwabuilder.com/#/builder/quick-start)

- It supports the Google Play Store, Microsoft Store, Meta Quest Store, and iOS App Store.

[How to publish a PWA to the Google Play Store](https://chromeos.dev/en/publish/pwa-in-play)\
[How to publish a PWA to the Microsoft Store](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/microsoft-store)

---

## [vite-plugin-pwa](https://vite-pwa-org.netlify.app/)

- [PWA Minimal Requirements(vite-plugin-pwa)](https://vite-pwa-org.netlify.app/guide/pwa-minimal-requirements.html)
- [사용법 참고 그림](https://vite-pwa-org.netlify.app/guide/cookbook.html)

### [VitePWAOptions](https://github.com/vite-pwa/vite-plugin-pwa/blob/4abcd5462f7ce030c7418303ba5bc6d5dd5b2634/src/types.ts#L236)

- [manifest](https://vite-pwa-org.netlify.app/guide/pwa-minimal-requirements.html#web-app-manifest)
  - `false`: manifest.webmanifest 자동 생성 안할 경우
- srcDir: injectManifest strategy인 경우
- filename: injectManifest strategy인 경우
- [strategies](https://vite-pwa-org.netlify.app/guide/service-worker-strategies-and-behaviors.html#service-worker-strategies)
  - [injectManifest](https://developer.chrome.com/docs/workbox/modules/workbox-build?hl=ko#injectmanifest): sw 직접 만드는 경우
  - [generateSW](https://developer.chrome.com/docs/workbox/modules/workbox-build?hl=ko#generatesw): default, sw 자동 생성
- [injectRegister](https://vite-pwa-org.netlify.app/guide/register-service-worker.html#register-service-worker)
  - `inline`
  - `script`
  - `auto`: default
- registerType

  - `autoUpdate`\
    injectManifest 인경우 [SW 업데이트 코드](https://vite-pwa-org.netlify.app/guide/inject-manifest.html#auto-update-behavior) 필요

    ```javascript
    import { clientsClaim } from "workbox-core";

    self.skipWaiting();
    clientsClaim();
    ```

  - `prompt`: default\
    injectManifest 인경우 [SW 업데이트 코드](https://vite-pwa-org.netlify.app/guide/inject-manifest.html#prompt-for-update-behavior) 필요

    ```javascript
    self.addEventListener("message", (event) => {
      if (event.data && event.data.type === "SKIP_WAITING") self.skipWaiting();
    });
    ```

- workbox
- injectManifest
  - injectionPoint
    - `undefined`: [precaching](https://vite-pwa-org.netlify.app/guide/inject-manifest.html#service-worker-code)을 사용하지 않는 경우
- [devOptions](https://vite-pwa-org.netlify.app/guide/development.html#development)\
  enable sw on development
  - enabled
  - type
    - `classic`: [generateSW strategy](https://vite-pwa-org.netlify.app/guide/development.html#generatesw-strategy) 인 경우
    - `module`: [injectManifest strategy](https://vite-pwa-org.netlify.app/guide/development.html#injectmanifest-strategy) 인 경우

### [virtual:pwa-register/react](https://vite-pwa-org.netlify.app/frameworks/react.html)

> PWA 업데이트 관련 동작 지정

`workbox-window` 설치 필요

- useRegisterSW

  - [immediate](https://vite-pwa-org.netlify.app/guide/auto-update.html#automatic-reload)

    - `true`: registerType가 autoUpdate인 경우

  - onNeedRefresh
  - onRegisteredSW
  - onOfflineReady
  - onRegisterError

### Workbox

- workbox-precaching
  - [precacheAndRoute](https://vite-pwa-org.netlify.app/guide/inject-manifest.html#service-worker-code)

### [PWA Assets Generator](https://vite-pwa-org.netlify.app/assets-generator/)

...

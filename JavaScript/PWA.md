# PWA

- [참고 - mdn](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
- [참고 - web.dev](https://web.dev/articles/pwa-checklist?hl=ko)
- [참고 - MS](https://learn.microsoft.com/ko-kr/microsoft-edge/progressive-web-apps-chromium/how-to/best-practices)

<br />

## Installability

`<link rel="manifest" href="manifest.json" />`

- If the PWA has more than one page, every page must reference the manifest in this way.
- Must be served over HTTPS(localhost, 127.0.0.1 and file:// are also considered secure.)
- Must include a [service worker](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) with a [fetch event handler](https://developer.mozilla.org/en-US/docs/Web/API/ServiceWorkerGlobalScope/fetch_event) that provides a basic offline experience.

### Required manifest members

- `name`
- `icons`
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

### packaging and publishing

[PWABuilder](https://docs.pwabuilder.com/#/builder/quick-start)

- It supports the Google Play Store, Microsoft Store, Meta Quest Store, and iOS App Store.

[How to publish a PWA to the Google Play Store](https://chromeos.dev/en/publish/pwa-in-play)\
[How to publish a PWA to the Microsoft Store](https://learn.microsoft.com/en-us/microsoft-edge/progressive-web-apps-chromium/how-to/microsoft-store)

<br />

### Triggering the install prompt

This is not supported on iOS.

- [beforeinstallprompt](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeinstallprompt_event)

<br />

## [Offline and background operation](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation)

- [Service Worker API](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API)
- [Background Synchronization API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API)
- [Background Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Background_Fetch_API)
- [Periodic Background Synchronization API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Periodic_Background_Synchronization_API)
- [Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API)
- [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API)

<br />

## [Caching](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching#cache_first_with_cache_refresh)

<br />

## [Provide an app-like experience](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Best_practices#provide_an_app-like_experience)

- [standalone display mode](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Create_a_standalone_app)
- [Define your app icon](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Define_app_icons)
- [prefers-color-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)
- [Customize your app's theme and background colors](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Customize_your_app_colors)

<br />

- [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API)
- [file_handlers](https://developer.mozilla.org/en-US/docs/Web/Manifest/file_handlers)
- [Display badges](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Display_badge_on_app_icon)
- [data sharing between apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/How_to/Share_data_between_apps)

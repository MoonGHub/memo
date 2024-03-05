# JavaScript - BOM

- [window](#window)
- [document](#document)
- [screen](#screen)
- [location](#location)
- [history](#history)
- [navigator](#navigator)

## window

### 조작

- alert(str)
- prompt(strQue, strAns)
- confirm(strConf)
- open(url, name, option)
  -option: "parameterName=value, ..."
  parameterName: width, height, left, top, scrollbars, location, status, toolbars, ...
- close()
- open("URL", "새 창 이름", "새 창 옵션")
  옵션 ex) "width=350, height=350, location=no, scrollbars=no"
- focus
- blur // 포커스 제거

<br />

### 위치 및 크기

- moveBy(x, y) // 지정 위치만큼 이동
- moveTo(x, y) // 지정 위치로 이동
- resizeBy(x, y) // 지정 크기만큼 변경
- resizeTo(x, y) // 지정 크기로 변경
- innerHeight // 스크롤바영역 포함
- innerWidth // 스크롤바영역 포함
- outerHeight // 브라우저 크기
- outerWidth
- scrollX
- scrollY // 높이
- scrollTo(x, y)
- pageYOffset
- scrollTo(가로,세로);
- innerWidth
- innerHeight
- screenLeft
- screenTop
- closed
- length
- name
- parent
- top

<br />

### 기타

- frames[] // iframe 요소들 반환
- setInterval
- clearInterval
- setTimeout(func(){...}, time) // func전역에 등록,
- clearTimeout(refer)

<br />

## document

<br />

## screen

- width // 사용자 모니터 크기? 화면 너비값?
- height
- availWidth
- availHeight // 작업 표시줄을 제외한
- colorDepth // 사용자 모니터의 표현 가능한 컬러 bit

<br />

## location

- href
- hash // 주소에 #이후 값
- hostname // 호스트이름(찐주소)
- host // 호스트이름 + 포트번호
- protocol
- search // 쿼리
- reload
- replace\
   뒤로가기 불가

<br />

## history

- back()
- forward()
- go(num) // -2는 2단계 이전 사이트
- length // 방문기록 개수

<br />

## navigator

Navigator
.language // ko
appName // 브라우저 이름 ex) Netscape
appVersion
appCodeName // 브라우저 코드명 ex)Mozilla
.product // 엔진이름, Gecko
.platform // 브라우저 정보 ex) Win32, MacIntel
.onLine // 인터넷 연결, true or false
.userAgent // 브라우저 정보 + 운영체제, windows, macintosh, iphone, android 등 출력
.geolocation // 위치정보
.getCurrentPosition(successCallBack, errCallBack, option...)
successCallBack의 전달인자 position
.coords // coordinate: 좌표
.latitude // 위도
.longitude // 경도

- javaEnabled
- cookieEnabled

- clipboard
  - readText

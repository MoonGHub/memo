window
document  
 body, div, img, a, ...
screen
location
history
navigator

window
.open(url, name, option)
option: "parameterName=value, ..."
parameterName: width, height, left, top, scrollbars, location, status, toolbars, ...
.alert(str)
.prompt(strQue, strAns)
.confirm(strConf)
.moveBy(x, y) // 지정 위치만큼 이동
.moveTo(x, y) // 지정 위치로 이동
.resizeBy(x, y) // 지정 크기만큼 변경
.resizeTo(x, y) // 지정 크기로 변경
.setInterval(func(){...}, time, arguments) // func전역에 등록, clearInterval(refer)
.setTimeout(func(){...}, time) // func전역에 등록, clearTimeout(refer)
.close()
.
.innerHeight // 스크롤바영역 포함
.innerWidth // 스크롤바영역 포함
.outerHeight // 브라우저 크기
.outerWidth
.scrollX
.scrollY // 높이
.scrollTo(x, y)
.
.
.
.

screen
.width // 사용자 모니터 크기
.height
.availWidth // 작업 표시줄을 제외한
.availHeight
.colorDepth // 사용자 모니터의 컬러bit
.

location
.href
.hash // 주소에 #이후 값
.hostname // 호스트이름(찐주소)
.host // 호스트이름 + 포트번호
.protocol
.search // 쿼리
.reload()

history
.back()
.forward()
.go(num) // -2는 2단계 이전 사이트
.length

Navigator
.language // ko
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

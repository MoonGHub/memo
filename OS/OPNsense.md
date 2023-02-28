# OS - OPNSense

### 🦋 Shell(8) 인스톨러 실행

`opnsense-installer`

---

## 웹 관리 콘솔에서의 설정

크롬 브라우저에서 실행

### 🦋 포트 추가(OPT1)

1. Firewall > Rules > OPT1 > Add
2. Default로 설정된 값들로 바로 저장

### 🦋 플러그인 추가

System > Firmware > Plugins\

- 설치 후 새로고침 시, Services에 표시

### 🦋 SSL 발급 및 설정 - ACME Client

Services > ACME Client >

1. Settings > Settings > Enable Plugin [x]
2. Settings > Update Schedule\
   갱신 자동 스케줄 추가(자동으로 추가되어 있음)
3. Accounts > Accounts > add\
    아래의 값 입력 후, 저장
   - Name
   - E-Mail Address
4. Automations > Automations > add\
   Restart HAProxy 추가
5. Challenge Types > Challenge Types > add
   - Name: Duck_Challenge
   - DNS Service: DuckDNS\
   - DNS Sleep Time: 120\
   - API Token: duckdns.org에 로그인하여 토큰 복사
6. Certificates > Certificates > add
   - Common Name: 기본 도메인 추가
   - Alt Names: 사용 할 서브 도메인들을 추가
   - ACME Account: 추가한 계정 선택\
   - Challenge Type: 추가한 타입 선택
   - Key Length: ec-384
   - Automations: 추가한 값
   - DNS Alias Mode: Automatic Mode (uses DNS lookups)

### 🦋 리버스 프록시 - HAProxy

### 🦋 IPS(침입탐지시스템) 활성화

### 🦋 웹 관리 콘솔 접근 제한

### 🦋 내부망(NAT) 원격접속

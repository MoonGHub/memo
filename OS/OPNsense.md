# OS - OPNSense

- 초기 ID/PWD
  - ID: root
  - PWD: opnsense
- 설치 위치 경로 및 설정 파일
  - /usr/local/etc/
  - /usr/local/etc/haproxy
  - /usr/local/etc/haproxy.conf

### 🦋 Shell(8) 인스톨러 실행

`opnsense-installer`

---

## 웹 관리 콘솔에서의 설정

크롬 브라우저에서 실행

### 🦋 포트 추가(OPT1)

1. Firewall > Rules > OPT1 > Add
2. Default로 설정된 값들로 바로 저장(아웃바인드 허용)

### 🦋 웹 관리 콘솔 접속 제한(포트)

1. System > Settings > Administration
2. Listen Interfaces에서 설정

### 🦋 플러그인 추가

System > Firmware > Plugins

- 설치 후 새로고침 시, Services에 표시

### 🦋 NAT(Network Address Translation)설정

Firewall > NAT > Port Forward > add(방화벽 자동 등록됨)

- Interface: WAN\
   IPv4/TCP
- Source: all
- Destination: This Firewall\
   port range: HTTP\
   Redirect target IP: 내부망 서버 GW IP

### 🦋 리버스 프록시 설정 - HAProxy

1. Real Servers 등록
   - FQDN or IP: WAS IP
2. Virtual Services > Backend Pools 등록
   - Servers: 1.번의 서버
3. Rules & Checks > Conditions 등록
   - Condition type: Host starts with
   - Host Prefix: 도메인 이름
4. Rules & Checks > Rules 등록
   - Use backend pool: 2.번의 백엔드 풀
5. Virtual Services > Public Services 등록
   - Listen Addresses: 1.번의 IP:포트
   - Select Rules: 3.번의 규칙

- 시작 에러(WARNING: failed to start haproxy)
  1. `service haproxy status` 및 `service haproxy start`으로 먼저 실행
  2. `haproxy -d -f /usr/local/etc/haproxy.conf`으로 상세 에러 확인

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

### 🦋 IPS(침입탐지시스템) 활성화

### 🦋 내부망(NAT) 원격접속

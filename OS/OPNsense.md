# OS - OPNSense

## 설치(23.1 - 23.1.1_2)

1. Shell(8) - 인스톨러 실행(`opnsense-installer`)
   - ID: root
   - PWD: opnsense
2. Assign interfaces(1) - WAN과 LAN을 지정
3. Set interface IP address(2) - 지정한 인터페이스에 IP및 서브넷 마스크 설정

- 설치 위치 경로 및 설정 파일
  - /usr/local/etc/
  - /usr/local/etc/haproxy
  - /usr/local/etc/haproxy.conf

<br />

## 웹 관리 콘솔에서의 설정

**크롬 브라우저에서 실행**

### 포트 추가(OPT1)

1.  Firewall > Rules > OPT1 > Add
2.  Default로 설정된 값들로 바로 저장(아웃바인드 허용)

### 웹 관리 콘솔 접속 제한(포트)

1.  System > Settings > Administration
2.  Web GUI > Listen Interfaces에서 설정

### NAT(Network Address Translation)설정

Firewall > NAT

- 포트 포워딩(> Port Forward > add - 방화벽도 자동 등록됨)
  - Interface: WAN\
     IPv4/TCP
  - Source: all
  - Destination: This Firewall\
     port range: IN 포트 지정\
     Redirect target IP: NAT IP\
     Redirect target port: NAT port

<br />

## 플러그인

**플러그인 추가(System > Firmware > Plugins)**\
(설치 후 새로고침 시, Services에 표시)

- os-acme-client - 3.15
- os-haproxy - 4.1

### HAProxy - 리버스 프록시 설정

1.  Real Servers 등록
    - FQDN or IP: WAS IP
    - Port: 접속 port
    - Verify SSL Certificate 체크 해제
2.  Virtual Services > Backend Pools 등록
    - Servers: 1.번의 서버
3.  Rules & Checks > Conditions 등록
    - Condition type: Host starts with 또는 Host contains
    - Host Prefix 또는 Host contains: 도메인 이름
4.  Rules & Checks > Rules 등록
    - Select conditions: 3.번의 조건
    - Execute function: Use specified Backend Pool
    - Use backend pool: 2.번의 백엔드 풀
5.  Virtual Services > Public Services 등록
    - Listen Addresses: 외부 접속 IP:Port
    - Select Rules: 3.번의 규칙

- 시작 에러(WARNING: failed to start haproxy)
  1.  `service haproxy status` 및 `service haproxy start`으로 먼저 실행
  2.  `haproxy -d -f /usr/local/etc/haproxy.conf`으로 상세 에러 확인

### ACME Client - SSL 발급 및 HAproxy 설정

1.  Settings > Settings
    - Enable Plugin 체크
    - Auto Renewal 체크
2.  Settings > Update Schedule\
    갱신 자동 스케줄 추가(자동으로 추가되어 있음)
    - enabled 체크
3.  Accounts > Accounts > add
    - Name
    - E-Mail Address
    - ACME CA: Let's Encrypt
4.  Automations > Automations > add\
    Restart HAProxy 추가
5.  Challenge Types > Challenge Types > add\
    지원하지 않는 DNS를 사용중으로 HTTP-01타입을 사용
    - Name: HTTP-01
    - Challenge Type: HTTP-01
    - HTTP Service: HAProxy HTTP Frontend Integration(OPNsense plugin)
    - Enable Auto-Configuration: 체크
    - HAProxy Frontends: HAProxy에서 백엔드 풀이 등록되어있는 public service
6.  Certificates > Certificates > add
    - Common Name: 도메인 이름
    - Alt Names: 사용 할 서브 도메인들을 추가...? 일단 공백
    - ACME Account: 3.의 계정
    - Challenge Type: 5.의 타입
    - Key Length: ec-384
    - Automations: 4.의 자동화
    - DNS Alias Mode: Automatic Mode (uses DNS lookups)
7.  인증서 발급에 성공 되었으면, 5.에서 등록한 HAProxy의 public service의 설정을 변경
    - Enable SSL offloading 체크
    - SSL Offloading > Certificates: 6.에서 발급된 인증서를 등록

### HAProxy - http to https 리다이렉트 설정

1. NAT 포트포워딩 설정을 추가(방화벽은 자동으로 추가 됨)
   - WAN(all, all) -> Destination(This Firewall, 80) -> NAT(HAProxy public service의 리스닝 IP, 80)
   - WAN(all, all) -> Destination(This Firewall, 443) -> NAT(HAProxy public service의 리스닝 IP, 443)
2. HAProxy > 백엔드 풀이 설정된 public service의 리스닝 포트를 443으로 변경
3. Rules & Checks > Conditions > add
   - Name: Traffic_is_HTTP
   - Condition type: Traffic is HTTP
4. Rules & Checks > Rules > add
   - Name: redirect_https
   - Select conditions: 3.에서 추가한 Traffic_is_HTTP
   - Execute function: http-request redirect
   - HTTP Redirect: **scheme https code 301**
5. Virtual Services > Public Services > add
   - Name: ridirect_to_https
   - Listen Addresses: GW IP:80
   - Rules > Select Rules: 4.에서 추가한 redirect_https

<br />

---

## ETC

### 🦋 HAProxy 서브 도메인 추가

### 🦋 IPS(침입탐지시스템) 활성화

### 🦋 내부(NAT)망 원격접속

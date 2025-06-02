# Platform - OPNSense

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

<br />

### 포트 추가(OPT1)

1.  Firewall > Rules > OPT1 > Add
2.  Default로 설정된 값들로 바로 저장(아웃바인드 허용)

<br />

### 웹 관리 콘솔 접속 제한(포트)

1.  System > Settings > Administration
2.  Web GUI > Listen Interfaces에서 설정

<br />

### NAT(Network Address Translation)설정

> 외부 접속 허용 포트 추가 시 설정

Firewall > NAT

- 포트 포워딩(> Port Forward > add - 방화벽도 자동 등록됨)
  - Interface: WAN
  - TCP/IP Version: IPv4
  - Protocol: TCP
  - Source: any(all)\
    내부 네트워크에 도메인으로 접속하기 위하여 any
  - Destination: This Firewall
    - port range: IN 포트 지정(HTTP -> HTTP, HTTPS -> HTTPS)
    - Redirect target IP: NAT IP(OPT1의 GW)
    - Redirect target port: NAT port(HTTP or HTTPS)

<br />

## 플러그인

**플러그인 추가(System > Firmware > Plugins)**\
(설치 후 새로고침 시, Services에 표시)

- os-acme-client - 3.15
- os-haproxy - 4.1

<br />

### HAProxy - 리버스 프록시 설정

1.  Real Servers 등록
    - Name or Prefix: Server Name
    - FQDN or IP: WAS의 IP
    - Port: 접속 port
    - Verify SSL Certificate 체크 해제
2.  Virtual Services > Backend Pools 등록
    - Servers: 1.번의 서버
    - Enable Health Checking 체크 해제
3.  Rules & Checks > Conditions 등록
    - Condition type: Host starts with 또는 Host contains
    - Host Prefix 또는 Host contains: 도메인 이름
4.  Rules & Checks > Rules 등록
    - Select conditions: 3.번의 조건
    - Execute function: Use specified Backend Pool
    - Use backend pool: 2.번의 백엔드 풀
5.  Virtual Services > Public Services 등록
    - Listen Addresses: 외부 접속 IP:Port(80)
    - Select Rules: 3.번의 규칙

> 3~5에서 Map File로 조건 대체
>
> - Advanced > Map Files에 라인 당 `{domain명} {2.의 백엔드 풀 이름}` 형식으로 작성
> - Rules & Checks > Conditions 등록(Map Domains to backend pools using a map file과 위의 작성 Map파일 선택)
> - Public Services의 규칙에 위의 rule을 등록

- 시작 에러(WARNING: failed to start haproxy)

  1.  `service haproxy status` 및 `service haproxy start`으로 먼저 실행
  2.  `haproxy -d -f /usr/local/etc/haproxy.conf`으로 상세 에러 확인

- Jenkins - Git webhook 연동 추가
  1. real server와 backend pools는 Jenkins의 port로 위와 동일하게 생성
  2. 새 condition을 path regex로 Git에서 webhook에 추가한 경로로 하나만 추가(ex: ^/github-webhook/$)
  3. Advanced > map file을 생성하여 `{domain명} {1.의 백엔드 풀 이름}`형식으로 작성
  4. 새 rule에서 2.의 조건을 추가 후, Map domains to backend pools using a map file로 3.의 map파일 지정
  5. Public Service에 추가한 reverse_proxy_https에 4.의 rule추가(제일 앞에 위치해야 함)

<br />

### ACME Client - SSL 발급 및 HAproxy 설정

1.  Settings > Settings
    - Enable Plugin 체크
    - Auto Renewal 체크
    - HAProxy Integration 체크(중요!!)
      - HAProxy에 인증전용의 로컬 서버가 추가 됨(real, back, public?, condition, rule)
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
    지원하지 않는 DNS 및 HAProxy Integration로 인해 HTTP-01타입을 사용
    - Name: HTTP-01
    - Challenge Type: HTTP-01
    - HTTP Service: HAProxy HTTP Frontend Integration(OPNsense plugin)
    - Enable Auto-Configuration: 체크
    - HAProxy Frontends: HAProxy에서 acme 인증 백엔드 풀이 등록되어있는 public service
6.  Certificates > Certificates > add
    - Common Name: 도메인 이름
    - Alt Names: HTTP-01 타입은 와일드 카드 및 서브도메인 설정 불가
    - ACME Account: 3.의 계정
    - Challenge Type: 5.의 타입
    - Key Length: ec-384
    - Automations: 4.의 자동화
    - DNS Alias Mode: Automatic Mode (uses DNS lookups)
7.  인증서 발급에 성공 되었으면, real server - backend pool이 등록된 HAProxy의 public service의 설정을 변경
    - Enable SSL offloading 체크
    - SSL Offloading > Certificates: 6.에서 발급된 인증서를 등록

- HTTP-01 챌린지
  - 와일드카드(서브도메인) 인증서 발급 불가
- HAproxy의 public service에서 노출되는 인증서 삭제
  - OPNsense콘솔 > System > Trust > Certificates > 제거

<br />

### HAProxy - http to https 리다이렉트 설정

1. Firewall > NAT > Port Forward 설정을 추가(방화벽은 자동으로 추가 됨)
   - WAN(all, all) -> Destination(This Firewall, 80) -> NAT(HAProxy public service의 리스닝 IP, 80)
   - WAN(all, all) -> Destination(This Firewall, 443) -> NAT(HAProxy public service의 리스닝 IP, 443)
2. HAProxy > real server들의 백엔드 풀이 설정된 public service를 동일하게 생성하여 리스닝 포트를 443으로 변경
   - github-webhook도 생성한 443의 public service로 이동
   - 80의 public service는 Enable SSL offloading 체크 해제
3. Rules & Checks > Conditions > add
   - Name: Traffic_is_HTTP
   - Condition type: Traffic is HTTP
4. Rules & Checks > Conditions > add
   - Name: acme-challenge-negate
   - Condition type: Path regex
   - Negate condition 체크
   - Path Regex: `^/\.well-known/acme-challenge/?`
5. Rules & Checks > Rules > add
   - Name: redirect_https
   - Select conditions: 3.에서 추가한 Traffic_is_HTTP과 4.에서 추가한 acme-challenge-negate
   - Execute function: http-request redirect
   - HTTP Redirect: **scheme https code 301**
6. Virtual Services > Public Services > ~~add~~(~~또는~~ 2.의 기존 80포트 편집)

   ~~- Name: ridirect_to_https~~\
   ~~- Listen Addresses: GW IP:80~~\
   ~~- Rules > Select Rules: 5.에서 추가한 redirect_https~~

   또는 ACME Client 세팅에서 HAProxy Integration 체크로 자동 추가된 public services에서

   - Listen Addresses: GW IP:80
   - Rules > Select Rules: 5.에서 추가한 redirect_https(후 순위로 지정)

<br />

---

## ETC

<br />

### IPS(침입탐지시스템) 활성화

[참고](https://docs.opnsense.org/manual/ips.html)

1. Services > Intrusion Detection > Administration
2. 모두 체크
   - Enabled : IDS 활성화(탐지만)
   - IPS mode : IPS 모드 활성화(차단)
   - Promiscuous mode : 모든 트래픽을 감시
3. 추가 설정
   - Pattern matcher: HyperScan
   - Interfaces: WAN보호할 인터페이스(기본적으로 외부와 연결된 인터페이스)
4. Download 탭에서 Download & Update Rules 후, 모두 활성화
5. Rules 탭에서 필요한 부분을 Drop룰로 변경
6. Schedule 탭에서 cron(System > Settings > Cron) 업데이트 활성화

<br />

### 내부(NAT)망 원격접속 - SSH

> [!NOTE]
> HTTP 트래픽과 달리 SSH는 헤더 정보나 도메인 정보를 포함하지 않기 때문에, HAProxy는 요청이 어떤 도메인에 해당하는지 직접 알 수 없습니다.

- 당장은 사용하고자 하는 서버를 Default Backend Pool로 지정하여 사용
- 추후 HAproxy의 sni 기능 서치

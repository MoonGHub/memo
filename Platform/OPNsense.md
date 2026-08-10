# Platform - OPNSense

- [설치(26.7)](#설치267)
- [설정](#설정)
  - [웹 콘솔 접속 제한(포트)](#웹-콘솔-접속-제한포트)
  - [NAT(Network Address Translation)설정](#natnetwork-address-translation설정)
    - [HAproxy 사용 시, 80과 443은 방화벽 설정만 추가](#haproxy-사용-시-80과-443은-방화벽-설정만-추가)
  - [기타](#기타)
    - [공유기망 아래에서 도메인 접속 시](#공유기망-아래에서-도메인-접속-시-interfaces--wan--block-private-networks-체크-해제)
  - [IPS(침입탐지시스템) 활성화](#ips침입탐지시스템-활성화)
- [플러그인](#플러그인)
  - [HAProxy(리버스 프록시) - os-haproxy](#haproxy리버스-프록시---os-haproxy)
    - [Jenkins Git webhook 연동 추가](#jenkins-git-webhook-연동-추가)
    - [http to https 리다이렉트 설정](#http-to-https-리다이렉트-설정)
    - [내부망 원격접속(SSH)](#내부망-원격접속ssh)
      - [Predefined 방식](#predefined-방식)
      - [Dynamic 방식](#dynamic-방식)
  - [ACME Client(SSL) - os-acme-client](#acme-clientssl---os-acme-client)

---

## 설치(26.7)

1. Shell(8) - 인스톨러 실행(`opnsense-installer`)
   - ID: root
   - PWD: opnsense
2. Assign interfaces(1) - WAN과 LAN을 지정
3. Set interface IP address(2) - 지정한 인터페이스에 IP및 서브넷 마스크 설정
   > [!IMPORTANT]
   > WAN 설정 시 게이트웨이도 지정 할 것, LAN은 안해도 됨 => 내부망 인터넷 자동으로 됨

- 설치 위치 경로 및 설정 파일
  - /usr/local/etc/
  - /usr/local/etc/haproxy
  - /usr/local/etc/haproxy.conf

---

## 설정

### 웹 콘솔 접속 제한

1.  System > Settings > Administration
2.  Web GUI > Listen Interfaces > LAN

<br />

### NAT(Network Address Translation)설정

> 외부 접속 허용 포트(80, 443 또는 윈도우 원격접속 등) 추가 시 설정

Firewall > NAT > Destination NAT

- Interface: WAN
- Version: IPv4
- Protocol: TCP
- Source Address: any\
   외부 접근 IP
- Source Port: any\
   외부 접근 포트
- Destination Address: This Firewall\
   외부에서 접속 시 지정하는 IP(OPNsense WAN IP)
- Destination Port: Single port or range\
   외부에서 접속 시 지정하는 포트
- Redirect Target IP: Single host or Network\
   포트 포워딩 할 IP
- Redirect Target Port: Single port\
   포트 포워딩 할 Port
- **Firewall rule: Pass**\
   **중요! 방화벽 자동 등록**

#### HAproxy 사용 시, 80과 443은 방화벽 설정만 추가

WAN / IPv4 / TCP / Source any
→ This Firewall / 80 / Pass

WAN / IPv4 / TCP / Source any
→ This Firewall / 443 / Pass

<br />

### 기타

#### 공유기망 아래에서 도메인 접속 시, Interfaces > WAN > Block private networks 체크 해제

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

---

## 플러그인

**플러그인 추가(System > Firmware > Plugins)**\
(설치 후 새로고침 시, Services에 표시)

<br />

### HAProxy(리버스 프록시) - os-haproxy

1.  Real Servers 등록
    - Name or Prefix: Server Name
    - FQDN or IP: WAS의 IP
    - Port: 접속 port(80)
    - Verify SSL Certificate 체크 해제
2.  Virtual Services > Backend Pools 등록
    - Name: 1.번의 Server Name과 동일하게
    - Servers: 1.번의 서버
    - Enable Health Checking 체크 해제
3.  Advanced > Map Files 등록
    - Type: dom - Domains
    - Content: 라인 당 `{domain명} {2.의 백엔드 풀 이름}` 형식으로 작성
4.  Rules & Checks > Rule 등록
    - (Rule type)Type: Map Domains to backend pools using a map file
    - (Parameters)Map file: 3.에서 작성한 Map파일 선택
5.  Virtual Services > Public Services 등록
    - Listen Addresses: OPNsense WAN IP:Port(80)
    - Select Rules: 4.번의 규칙

- 시작 에러(WARNING: failed to start haproxy)
  1.  `service haproxy status` 및 `service haproxy start`으로 먼저 실행
  2.  `haproxy -d -f /usr/local/etc/haproxy.conf`으로 상세 에러 확인

<br />

#### Jenkins Git webhook 연동 추가

1. real server와 backend pools는 Jenkins의 port로 위와 동일하게 생성
2. 새 condition을 path regex로 Git에서 webhook에 추가한 경로로 하나만 추가
   - Path Regex: `^/github-webhook/$`
3. Advanced > map file을 생성하여 `{domain명} {1.의 백엔드 풀 이름}`형식으로 작성
4. 새 rule에서 2.의 조건을 추가 후, Map domains to backend pools using a map file로 3.의 map파일 지정
5. Public Service에 추가한 reverse_proxy_https에 4.의 rule추가(제일 앞에 위치해야 함)

#### http to https 리다이렉트 설정

1. real server들의 백엔드 풀이 설정된 public service(80)를 동일하게 생성하여 리스닝 포트를 443으로 변경\
   - github-webhook도 생성한 443의 public service로 이동
   - 80의 public service는 Enable SSL offloading 체크 해제
2. Rules & Checks > Conditions > add
   - Name: Traffic_is_HTTP
   - Condition type: Traffic is HTTP
3. Rules & Checks > Conditions > add\
    **ACME 추가 시 필수, 먼저 해놓아도 됨**
   - Name: acme-challenge-negate
   - Condition type: path_reg - Path regex
   - Negate condition 체크
   - Path Regex: `^/\.well-known/acme-challenge/?`
4. Rules & Checks > Rules > add
   - Name: redirect_https
   - Select conditions: 2.에서 추가한 Traffic_is_HTTP과 3.에서 추가한 acme-challenge-negate
   - (Rule Type)Type: http-request
   - (Parameters)Action: redirect
   - (Parameters)Options/Values: `scheme https code 301`
5. Virtual Services > Public Services > 80 포트의 Public Service
   - Rules > Select Rules: 4.에서 추가한 redirect_https(순서 상관 없음 - 아마)

#### 내부망 원격접속(SSH)

> [!NOTE]
> HTTP 트래픽과 달리 SSH는 헤더 정보나 도메인 정보를 포함하지 않기 때문에, HAProxy는 요청이 어떤 도메인에 해당하는지 직접 알 수 없음

> https://www.haproxy.com/blog/route-ssh-connections-with-haproxy 참고

##### Predefined 방식

1. 공유기 포트 포워딩 TCP로 추가(ex. 2222)
2. OPNsense > Firewall > NAT > Destination NAT > Add
   - Interface: WAN
   - Version: IPv4
   - Protocol: TCP
   - Source Address: any
   - Destination Address: This Firewall
   - Destination Port: IN 포트 지정(ex. 2222)
   - Redirect Target IP: NAT IP(내부 포트망의 GW)
   - Redirect Target Port: NAT port(ex. 2222)
   - **Firewall rule: Pass**\
      **중요! 방화벽 자동 등록**

   > [!NOTE]
   > 내부망이 아닌 OPNsense WAN으로 받으면 방화벽만 추가해주면 됨
   >
   > WAN / IPv4 / TCP / Source any
   > → This Firewall / 2222 / Pass

3. HAProxy > Virtual Services > Public Services > Add
   - advanced mode: 체크
   - Listen Addresses: OPNsense WAN IP 또는 내부 포트망의 GW:지정 포트(ex.2222)
   - Type: SSL/HTTPS (TCP mode)
   - Enable SSL offloading: 체크
   - Certificates: Web GUI TLS certificate
   - Option pass-through

     ```
     log-format "%ci:%cp [%t] %ft %b/%s %Tw/%Tc/%Tt %B %ts %ac/%fc/%bc/%sc/%rc %sq/%bq dst:%[var(sess.dst)] "

     tcp-request content set-var(sess.dst) ssl_fc_sni
     use_backend %[ssl_fc_sni]
     ```

4. 접속
   > [!IMPORTANT]
   > Real Servers에 22포트가 열려있고, 해당 서버를 Backend Pools에 등록해야 함
   - `ssh -o ProxyCommand="openssl s_client -quiet -connect {ISP 공인 IP}:2222 -servername {Real Servers의 22번 포트가 열린 서버와 연결된 Backend Pools의 Server Name}" 유저명@호스트명`

위 방법은 Predefined 방식으로, Real Servers와 Backend Pools를 각 서버마다 등록해줘야 함
생략하는 방법은 Dynamic 방식으로 아래와 같음

##### Dynamic 방식

Predefined 방식의 1과 2 선행

1. HAProxy > Virtual Services > Public Services > Add
   - advanced mode: 체크
   - Listen Addresses: OPNsense WAN IP 또는 내부 포트망의 GW:지정 포트(ex.2222)
   - Type: SSL/HTTPS (TCP mode)
   - Enable SSL offloading: 체크
   - Certificates: Web GUI TLS certificate
   - Option pass-through

     ```
     log-format "%ci:%cp [%t] %ft %b/%s %Tw/%Tc/%Tt %B %ts %ac/%fc/%bc/%sc/%rc %sq/%bq dst:%[var(sess.dst)] "

     tcp-request content set-var(sess.dst) ssl_fc_sni
     default_backend ssh-all
     ```

2. HAProxy > Real Servers > Add
   - Name or Prefix: ssh-all
   - FQDN or IP: 0.0.0.0
   - Port: 22
   - Verify SSL Certificate 체크 해제
3. HAProxy > Virtual Services > Backend Pools > Add
   - advanced mode: 체크
   - Name: ssh-all
   - Mode: TCP(Layer 4)
   - Servers: 2.에서 등록한 ssh-all
   - Enable Health Checking 체크 해제
   - Option pass-through

     ```
     acl allowed_destination var(sess.dst) -m ip {허용 내부망 ip x.x.x.x}
     acl allowed_destination var(sess.dst) -m ip {허용 내부망 ip x.x.x.x}

     tcp-request content set-dst var(sess.dst)

     tcp-request content accept if allowed_destination
     tcp-request content reject
     ```

4. 접속
   - `ssh -o ProxyCommand="openssl s_client -quiet -connect {ISP 공인 IP}:2222 -servername {Real Servers의 IP}" 유저명@호스트명`

<br />

### ACME Client(SSL) - os-acme-client

1.  Settings > Settings
    - Enable Plugin 체크
    - Auto Renewal 체크
    - HAProxy Integration 체크(중요!)
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
    - HAProxy Frontends: HAProxy의 80포트 public service
6.  Certificates > Certificates > add
    - Common Name: 도메인 이름
    - Alt Names: HTTP-01 타입은 와일드 카드 불가능, 서브도메인이 있는경우 하나씩 추가
    - ACME Account: 3.의 계정
    - Challenge Type: 5.의 타입
    - Key Length: ec-384
    - Automations: 4.의 자동화
    - ~~DNS Alias Mode: Automatic Mode (uses DNS lookups)~~: DNS-01 관련 기능
7.  인증서 발급에 성공 되었으면, HAProxy의 public service(443)의 설정을 변경
    - Enable SSL offloading 체크
    - SSL Offloading > Certificates: 6.에서 발급된 인증서를 등록

- HTTP-01 챌린지
  - 와일드카드(서브도메인) 인증서 발급 불가
- HAproxy의 public service에서 노출되는 인증서 삭제
  - OPNsense콘솔 > System > Trust > Certificates > 제거

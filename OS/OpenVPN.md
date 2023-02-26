# OS - OpenVPN

### 🦋 설치

1. OpenVPN Access Server 설치 파일 다운로드(OVA)
   - [링크](https://as-portal.openvpn.com/get-access-server)
2. 설치 후, ID: `root`, PWD: `openvpnas`
3. 동의 관련 입력 요구가 나올 경우, `Ctrl c`로 빠져나옴
4. `nano /etc/netplan/01-netcfg.yaml`의 내용을 아래와 같이 수정\
   ```yaml
   network:
     version: 2
     renderer: networkd
     ethernets:
       eth0:
         dhcp4: no
         addresses:
           - 지정IP/서브넷마스크
        gateway4: 게이트웨이
        nameservers:
          addresses: [8.8.8.8, 8.8.4.4]
   ```
5. `netplan apply`\
   설정파일 적용
6. `ifconfig`\
   적용 확인
7. `ovpn-init`
8. 이후 초기화
   - 약관 동의 > yes
   - primary Access Server node? > yes
   - ip 설정 > 2(위에서 설정한 IP)
   - 이후 Default로 패스
9. `passwd openvpn`\
   openvpn계정 비밀번호 설정
10. 위에서 설정한 `https://아이피:943/admin`으로 접속
    - 버전 확인 후, `apt update`
    - `apt install openvpn`로 최신버전으로 업데이트
11. `https://아이피:943/`에서 client.ovpn 파일 다운
12. 텍스트 편집기에서 해당 파일의 remote부분의 IP와 포트를 외부 접속 IP와 포트로 변경
13. OpenVPN Connect를 통해 접속

### 🦋 Port 변경

1. `https://OpenVPN호스트 IP:943/admin` 접속
2. Configuration > Network Settings
3. 서버 프로토콜(TCP 또는 UDP) Port 및 웹 서버 접속 포트 변경

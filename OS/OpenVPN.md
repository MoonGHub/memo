# OS - OpenVPN

### ๐ฆ ์ค์น(2.8.5)

1. OpenVPN Access Server ์ค์น ํ์ผ ๋ค์ด๋ก๋(OVA)
   - [๋งํฌ](https://as-portal.openvpn.com/get-access-server)
2. ์ค์น ํ, ID: `root`, PWD: `openvpnas`
3. ๋์ ๊ด๋ จ ์๋ ฅ ์๊ตฌ๊ฐ ๋์ฌ ๊ฒฝ์ฐ, `Ctrl c`๋ก ๋น ์ ธ๋์ด
4. `nano /etc/netplan/01-netcfg.yaml`์ ๋ด์ฉ์ ์๋์ ๊ฐ์ด ์์ \
   ```yaml
   network:
     version: 2
     renderer: networkd
     ethernets:
       eth0:
         dhcp4: no
         addresses:
           - ์ง์ IP/์๋ธ๋ท๋ง์คํฌ
        gateway4: ๊ฒ์ดํธ์จ์ด
        nameservers:
          addresses: [8.8.8.8, 8.8.4.4]
   ```
5. `netplan apply`\
   ์ค์ ํ์ผ ์ ์ฉ
6. `ifconfig`\
   ์ ์ฉ ํ์ธ
7. `ovpn-init`
8. ์ดํ ์ด๊ธฐํ
   - ์ฝ๊ด ๋์ > yes
   - primary Access Server node? > yes
   - ip ์ค์  > 2(์์์ ์ค์ ํ IP)
   - ์ดํ Default๋ก ํจ์ค
9. `passwd openvpn`\
   openvpn๊ณ์  ๋น๋ฐ๋ฒํธ ์ค์ 
10. ์์์ ์ค์ ํ `https://์์ดํผ:943/admin`์ผ๋ก ์ ์
    - ๋ฒ์  ํ์ธ ํ, `apt update`
    - `apt install openvpn`๋ก ์ต์ ๋ฒ์ ์ผ๋ก ์๋ฐ์ดํธ
11. `https://์์ดํผ:943/`์์ client.ovpn ํ์ผ ๋ค์ด
12. ํ์คํธ ํธ์ง๊ธฐ์์ ํด๋น ํ์ผ์ remote๋ถ๋ถ์ IP์ ํฌํธ๋ฅผ ์ธ๋ถ ์ ์ IP์ ํฌํธ๋ก ๋ณ๊ฒฝ
13. OpenVPN Connect๋ฅผ ํตํด ์ ์

### ๐ฆ Port ๋ณ๊ฒฝ

1. `https://OpenVPNํธ์คํธ IP:943/admin` ์ ์
2. Configuration > Network Settings
3. VPN Server์น์์์ ์๋ฒ ํ๋กํ ์ฝ(TCP ๋๋ UDP) ๋ฐ ํฌํธ ๋ณ๊ฒฝ\
   => OpenVPN Connect๋ฅผ ์ฌ์ฉํ์ฌ ์ธ๋ถ์์ ์ ์ํ๋ ํฌํธ
4. Admin Web Server์์ ํฌํธ ๋ณ๊ฒฝ\
   => ์น ์ฝ์ ์ ์ ํฌํธ

### ๐ฆ ์น ์ฝ์ ๋ก๊ทธ์ธ ๋ฝ ํด์  ๋ฐฉ๋ฒ

[์ฐธ๊ณ ](https://openvpn.net/faq/how-do-i-unlock-users-that-are-locked-out-now/)

```shell
cd /usr/local/openvpn_as/scripts/
./sacli --key "vpn.server.lockout_policy.reset_time" --value "1" ConfigPut
./sacli start
sleep 2
./sacli --key "vpn.server.lockout_policy.reset_time" ConfigDel
./sacli start
```

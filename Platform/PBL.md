# Platform - PBL

## MAC 또는 Ubuntu

### 에러: zsh: command not found: ls

`export PATH=%PATH:/bin:/usr/local/bin:/usr/bin`\
또는 위 명령행을 **~/.zshrc**에 추가

<br />

### 에러: bash: lerna: command not found

`alias lerna="yarn lerna"`
를 ~/.bashrc에 추가

<br />

### 에러: E: Unable to locate package vim

```shell
apt-get update
apt-get install apt-file
apt-file update
apt-get install vim
```

또는

```shell
apt-get update && apt-get install apt-file -y && apt-file update && apt-get install vim -y
```

<br />

### 에러: Temporary failure resolving ...(apt에러) 또는 dial tcp lookup server ... misbehaving(도커 관련)

- `/etc/resolv.conf` 파일에 `nameserver 8.8.8.8`와 `nameserver 8.8.4.4` 두 줄 추가
- ~~`vim ~/.bashrc`에 아래 추가 후, `source ~/.bashrc`~~ 자동 적용이 안됨
  ```shell
  sudo echo "nameserver 8.8.8.8" >> /etc/resolv.conf
  sudo echo "nameserver 8.8.4.4" >> /etc/resolv.conf
  ```
- 자동 적용 `vim /etc/netplan/00-installer-config.yaml`의 nameservers.addresses 부분에 `[8.8.8.8, 8.8.4.4]`추가\
  `sudo netplan apply`실행

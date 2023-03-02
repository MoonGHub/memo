# OS - PBL

### 🦋 에러: zsh: command not found: ls

`export PATH=%PATH:/bin:/usr/local/bin:/usr/bin`\
또는 위 명령행을 **~/.zshrc**에 추가

### 🦋 에러: bash: lerna: command not found

`alias lerna="yarn lerna"`
를 ~/.bashrc에 추가

### 🦋 에러: E: Unable to locate package vim

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

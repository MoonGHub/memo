# OS - PBL

### π¦ μλ¬: zsh: command not found: ls

`export PATH=%PATH:/bin:/usr/local/bin:/usr/bin`\
λλ μ λͺλ Ήνμ **~/.zshrc**μ μΆκ°

### π¦ μλ¬: bash: lerna: command not found

`alias lerna="yarn lerna"`
λ₯Ό ~/.bashrcμ μΆκ°

### π¦ μλ¬: E: Unable to locate package vim

```shell
apt-get update
apt-get install apt-file
apt-file update
apt-get install vim
```

λλ

```shell
apt-get update && apt-get install apt-file -y && apt-file update && apt-get install vim -y
```

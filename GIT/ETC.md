# GIT - ETC

### π¦ SSH Key gen μμ±

`ssh-keygen -m PEM -t rsa -b 4096 -C answlgus1122@gmail.com`

- -f ~/.ssh/moonghub_rsa: μμΉ(κΈ°λ³Έ- ~/.ssh/) λ° νμΌ λͺ μ§μ (rsaλ₯Ό μ¬λ¬κ° μ¬μ© μ)
- νμΌλͺμ μμ μ§μ  μ, μλμ κ°μ μ€μ μ΄ νμ
  1. config νμΌ μμ±\
     **~/.ssh/config**
     ```conf
     # Git κ³μ  λ΄κΊΌ
     Host moonghub_rsa
       HostName github.com
       IdentityFile ~/.ssh/moonghub_rsa
     ```
  2. `eval $(ssh-agent -s)`
  3. `ssh-add ~/.ssh/moonghub_rsa`
  4. `ssh -T git@moonghub_rsa`

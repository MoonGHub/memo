# GIT - PBL

## SSH Key gen 생성

`ssh-keygen -m PEM -t rsa -b 4096 -C answlgus1122@gmail.com`

- -f ~/.ssh/moonghub_rsa: 위치(기본- ~/.ssh/) 및 파일 명 지정(rsa를 여러개 사용 시)
- 파일명을 임의 지정 시, 아래와 같은 설정이 필요
  1. config 파일 생성\
     **~/.ssh/config**
     ```
     # Git 계정 내꺼
     Host moonghub_rsa
       AddKeysToAgent yes
       HostName github.com
       IdentityFile ~/.ssh/moonghub_rsa
     ```
  2. `eval $(ssh-agent -s)`
  3. `ssh-add ~/.ssh/moonghub_rsa`
  4. `ssh -T git@github.com`
  - `Hi {owner}! ...` 해당 레포의 `owner`가 표시되어야 함, 실패 시, 2번 부터 재시도

<br />

## 이슈 브랜치 자동 생성 및 삭제

1. robvanderleek/create-issue-branch 을 이용\
   Issue -> Create branch -> Create pr

   - 할당자와 label을 부여하여 이슈 생성
   - label만 부여해 이슈를 생성하고, 나중에 할당자를 부여

2. Settings > General > Automatically delete head branches 체크
3. 로컬에서 브랜치 동기화는 [참고](./Grammar.md#동기화)

<br />

## Git Action

### 오류 - ssh: handshake failed: ssh: unable to authenticate, attempted methods [none publickey], no supported methods remain

1. Repository secrets에 공개키(id_rsa.pub)가 아닌 개인 키(id_rsa)를 등록
2. 호스트 서버에서 `cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys`

### 오류 - Failed to CreateArtifact: Artifact storage quota has been hit

```text
Build_Project
Failed to CreateArtifact: Artifact storage quota has been hit. Unable to upload any new artifacts. Usage is recalculated every 6-12 hours.
More info on storage limits: https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions#calculating-minute-and-storage-spending
```

- [참고](https://docs.github.com/en/rest/actions/artifacts?apiVersion=2022-11-28)

- 아티팩트 전체(100개) 삭제 명령어

  ```shell
  gh api \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    -XGET /repos/MoonGHub/app/actions/artifacts \
    -F per_page=100 | \
  grep -o '"id":[0-9]\+,"node_id"' | \
  sed -e 's/"id"://' -e 's/,"node_id"//' | \
  while read artifact_id; do
    echo "Deleting artifact with ID: $artifact_id"
    gh api --method DELETE --silent \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      /repos/MoonGHub/app/actions/artifacts/$artifact_id
  done
  ```

- 아티팩트 전체(100개) 삭제 명령어 - 오래된 순부터 제거
  ```shell
  gh api --jq '.artifacts | sort_by(.created_at) | .[].id' \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      -XGET /repos/MoonGHub/app/actions/artifacts \
      -F per_page=100 | \
  while read artifact_id; do
    echo "Deleting artifact with ID: $artifact_id"
    gh api --method DELETE --silent \
      -H "Accept: application/vnd.github+json" \
      -H "X-GitHub-Api-Version: 2022-11-28" \
      /repos/MoonGHub/app/actions/artifacts/$artifact_id
  done
  ```

1. 위 명령어로 아티팩트 수동 제거 후
2. 워크플로우의 기능 옵션/환경변수 추가

- actions/upload-artifact@v4
  - 옵션
    - retention-days: 1
- docker/build-push-action@v6
  - 환경 변수
    - DOCKER_BUILD_RECORD_UPLOAD: false

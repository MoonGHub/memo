# GIT - Grammar

-     git rebase -i --root 	# pick →  s (squash) 전체 합치기
-     			# --root 옵션은 첫 커밋부터 최신까지 표시
-     			# --root 대신 커밋해쉬^   (^에 주의!) 입력 시, 지정 커밋부터 최신까지

- 중간 수정은 git rebase --interactive 지정커밋해쉬^
-     # 커밋포커싱이 지정커밋해쉬로 바뀜
- 지정커밋해쉬의 pick → edit && ZZ
- 수정 후, git add .
- git commit --amend
- (+ 커밋 메세지 수정!)

- git rebase --continue
- no conflict시, 바로 5번
- conflict시, 해당 파일이 conflict로 수정 됨 → resolve해줌
- (resolve로 수정하는 파일은 지정커밋 이후 버젼의 파일임!!!)
- resolve후, 다시 git rebase --continue
- (+ conflict난 버젼의 메세지 수정(지정 커밋 이후임!))
- Successfully 뜨면 성공 !
-
-
-
- 브랜치에서 브랜치따기
- $​​git branch BIZWAVE-5362 origin/dev

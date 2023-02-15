-webkit-~: 크롬, 사파리
-moz-~: 파이어폭스
-ms-~: 익스플로러
-o-~: 오페라

static: 문서 흐름대로(margin 등)
relative: 문서 흐름(margin 등) + 상대적 위치(left, top 등)
fixed: 보이는 화면에서의 절대 위치 (left, top 등)
absolute: 부모 요소(static이 아닌)를 기준으로 한 상대적 위치 (left, top 등), 보통 body아래 구성

user-select: none // 드래그 안됨

// 트랜지션은 요소의 속성이 변하면 발생(특정 속성 listen)
transition-property: all; // listen할 속성 지정
transition-duratiojn: 1s;
transition-timing-function: ease-in-out;
transition: all 1s ease-in-out;

// 애니메이션은 키프레임과 세트로 작동
@keyframes name{
from {
// ...
}

    50% {
        // ...
    }

    to{
        // ...
    }

}

animation-name : @keyframes 규칙을 이용하여 기술
animation-duration : 한 싸이클 시간
animation-delay : 로드 후 지연 시간
animation-direction : 애니메이션이 종료 후 순방향, 역방향 지정
normal: 순반향
alternate: 순, 역 반복
reverse: 역박향
alternate-reverse: 역, 순 반복
animation-iteration-count : 반복횟수. infinite: 무한
animation-play-state : 멈추거나, 다시 시작
running
paused
animation-timing-function : @keyframes의 상태들의 시간간격
ease
ease-in-out
animation-fill-mode : 애니메이션이 전후의 적용 값

# React - PBL

### 🦋

React

컴포넌트 = 속성 값 + 상태 값

useState, useEffect, useRef, useCallback, useContext, useMemo,
useReducer, useImperativeHandle
기타 훅 : useLayoutEffect, useDebugValue

✔︎useState

1.  상태값 변경 함수에 함수(a)를 대입 시, 함수(a)의 매개로 이전의 상태값을 받을 수 있다.
2.

✔︎useEffect

1. 컴포넌트 렌더링 결과가 dom에 반영 후 호출 됨(비동기)
2. 매개는 무조건 함수

✔︎export default React.memo(컴포넌트 [,F])

1. 해당 컴포넌트의 속성값이 변경 될 때에만 재렌더링(보통은 부모컴포넌트 재랜더링 시, 하위 컴포넌트는 전체 재랜더링됨)
   // -> 자신만의 메모리 공간 할당
2. F는 컴포넌트의 전후 매개변수를 비교하기 위한 커스텀 함수
   // -> F(prevProps, nextProps), true면 이전 컴포넌트 사용, false면 가상 돔을 업데이트 후 변경 부분만 실제 돔에 반영
   // 생략 시, 얕은 비교로 수행됨

✔︎컴포넌트에서 return null or boolean 시에 렌더링 안함
✔︎컴포넌트에서 return ReactDom.createPortal(Element, ParentElement)
// 사용된 위치에 상관없이 렌더링 할 위치 선택, ex) modal창

✔︎컴포넌트 밖에서 const testContext = React.createContext(‘default value’);
-> 컴포넌트에서 <testContext.Provider value={}>
<testContext.Consumer>{v => (<…></…>)}</..>
</..>
// testContext.Consumer대신에 const test = useContext(testContext);로 사용

✔︎useRef

1. class형 컴포넌트 및 일반 DOM요소에 사용 가능 // ref.current로 컴포넌트의 함수 호출 가능
2. 함수형 컴포넌트에 사용 불가 // useImperativeHandle 훅 사용 시, 외부로 변수와 함수를 노출 가능
   // React.forwardRef((props, ref) => ( … )); // 예약어인 ref를 그대로 사용 가능
3. 컴포넌트의 ref속성의 값이 함수일 때, 해당 요소가 제거, 생성 또는 ref값 변경 시 실행 됨
4. 단순 데이터 저장 시 사용 
   ✔︎const setXxX = useCallback(ref => ref && setXXX(), []);
   -> ref속성 값에 ref={setXxX}
   ✔︎const onSave = useCallback(() => saveToServer(name, age), [name, age]);
   -> 함수를 속성값으로 전달 하는 곳에 사용
5. 렌더링 성능을 위해 제공됨, React.memo를 사용해도 함수전달 시 새로 생성되어 재렌더링 되기 때문에 함수를 고정하기 위함
6. 한 번 생성된 함수를 재사용(재 랜더링시)

✔︎const value = useMemo(() => 함수, [의존성 배열]);

1. 이전의 값(함수의 결과 값)을 기억해 재사용
2. 함수의 결과 값을 기억
3. 의존성 배열 값이 변경 시, 함수(첫 매개변수) 재 실행 후, 결과 값 기억

✔︎useReducer 176P

✔︎useImperativeHandle

1. 부모 컴포넌트에서 ref.current로 접근가능
2. 자식 컴포넌트는 forwardRef로 생성해 ref를 부모로 부터 받아 useImperativeHandle(ref, ()=> { 함수명 : 함수 })

✔︎useLayoutEffect

1. 음… 그냥 useEffect를 사용하자

✔︎useDebugValue

1. 개발 편의를 위해 제공(console.log 같은 느낌 .. )
2. useDebugValue(value ? ‘on’ : ‘off’);

👀가독성과 생산성

1. 컴포넌트 작성법
   1. 컴포넌트 타입정의
   2. 컴포넌트 정의
      1. 연관된 코드-기능 별로 작성
      2. 기능을 커스텀 훅으로 정의해 사용
   3. 기타 변수(상수로 정의!) 및 함수 정의
2. 배열 변수의 경우 기본 값으로 빈 배열을 넣어줌
3. 조건부 렌더링에서 삼항연산자 대신 &&를 활용할 것
4. 관심사 분리
   1. 프레젠테이션
   2. 컨테이너
   3.

✔︎ getDerivedStateFromProps

1. 속성 값으로 부터 상태값을 생성함

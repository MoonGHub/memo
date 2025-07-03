# Kotlin - Thymeleaf

- [표현식](#표현식)
- [Attribute](#attribute)
  - [th](#th)
  - [layout](#layout)
- [Utility Objects](#utility-objects)

### 표현식

- `${...}`: 변수 표현식
- `*{...}`: 선택 변수 표현식
- `#{...}`: 메시지 표현식
- `@{...}`: Link URL 표현식, 컨텍스트 경로 포함
- `~{...}`: Fragment Expressions, fragment, layout 등 템플릿 파일 경로

---

## Attribute

### th

> html에 `xmlns:th="http://www.thymeleaf.org"` 추가

- `th:text`
- `th:utext`: 태그도 적용해서 출력
- `th:attr`
- `th:value`
- `th:href`
- `th:src`
- `th:action`
- `th:object`
- `th:field`
- `th:each`
- `th:if`
- `th:unless`
- `th:switch`: `th:case`와 함께
- `th:case`: `th:case="*"`는 default
- `th:fragment`
- `th:insert`
- `th:replace`
- `th:include`: deprecated
- `th:remove`
- `th:inline`: `th:inline="javascript"`와 같이 사용하며, `[[${user}]]`와 같이 서버 데이터 파싱
- `th:id`

  ```html
  <script th:inline="javascript">
    /*<![CDATA[*/

    // js 코드...

    /*]]>*/
  </script>
  ```

- `th:class`
- `th:classappend`
- `th:style`
- `th:selected`
- `th:checked`
- `th:disabled`
- `th:readonly`
- `th:with`: 블럭 내 사용할 변수 지정
- `th:block`: 태그 그룹핑용

### layout

- `layout:decorate`: 사용할 레이아웃 선택
- `layout:fragment`: 대치하거나 대치될 슬롯 지정, 문자열이어야 함
- `layout:insert`
- `layout:replace`
- `layout:title-pattern`: `"$LAYOUT_TITLE - $CONTENT_TITLE"` 형식으로 사용

---

## Utility Objects

- `#ctx`: 컨텍스트 (Context) 정보
- `#vars`: 변수 맵 (모든 모델 변수 접근 가능)
- `#locale`: 현재 로케일 정보
- `#request`: HttpServletRequest 객체
- `#response`: HttpServletResponse 객체
- `#session`: HttpSession 객체
- `#servletContext`: ServletContext 객체
- `#lists`: 리스트 관련 함수
- `#sets`: Set 관련 함수
- `#maps`: Map 관련 함수
- `#arrays`: 배열 관련 함수
- `#strings`: 문자열 관련 함수
- `#numbers`: 숫자 관련 함수
- `#dates`: 날짜 관련 함수
- `#bools`: Boolean 관련 함수
- `#objects`: null 체크, equals 등 일반 유틸
- `#messages`: 국제화 메시지

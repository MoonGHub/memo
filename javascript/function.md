encodeURI('?query=값')             // 유니코드로 인코딩, 영숫자 및 일부문자 제외
encodeURIComponent('?query=값')    // 영숫자만 제외, GET방식에 사용(form은 기본구현되있음)
decodeURI('?query=%EA%B0%92')
decodeURIComponent('?query=%EA%B0%92')
parseInt('5.12')
parseInt('5px')                    // 숫자로 시작해 첫 문자까지
parseFloat('13.2%')
String(123)
Number('123')
Boolean(1)
isNaN('a')                     // is not a number, 문자존재 시 false
eval('1+2')                    // 문자열을 코드로 처리, JSON은 JSON.parse를 사용하자
JSON.parse('{"name":"man", "age":"12"}')

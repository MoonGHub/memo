0b110       # 6
0o110       # 72
0x110       # 272
# ^ : 배타 or
# ~ : 반전
# << 는 *2, >> 는 /2

7 // 2      # 3
7 % 2       # 1
3 ** 4      # 81
divmod(13,5)    # (몫, 나머지) 반환

type(1)         # int
type(1.1)       # float
type('a')       # str

int(True)       # 1
int(False)      # 0
int(123.456)    # 123, 소수점 아래 버림
int(1.0e3)      # 1000
int('1')        # 1
int('1.1')      # err
googol = 10 ** 100  # py3에선 long이 없고, int가 가변사이즈

float(1)        # 1.0
float('2')      # 2.0
float('2.1')    # 2.1
float('2.3e-3') # 0.0023

print("'single' quote ")    # 'single' quote
print('"double" quote ')    # "double" quote
text = '''a
b
    c'''
print('te\nst')     # 연속 행 실행시, \사용

str(1.3e6)          # '1300000.0'
str(False)          # 'False'
str(1234)[0]        # 1
str(1234)[-1]       # 4
'abc ' * 3           # abc abc abc

'1234567890'[:]         # 전체
'1234567890'[1:]        # index1~
'1234567890'[:3]        # ~idex2(3-1)
'1234567890'[2:-1:3]    # index2~index끝에서-2(-1-1) 까지 3등차로 뽑음, 369
'1234567890'[::3]       # 
'1234567890'[::-1]      # 역순

len('123')      # 3
len([1,2,3,4])  # 4

string함수 
    .split(deli)         # 배열 반환, 파라미터 maxsplit
    .join(arr)           # 문자열 반환, 요소가 문자열이어야 함
    .startswith(st)      # st로 시작하면 True
    .endswith(st)        # st로 끝나면 True
    .find(st)            # 일치하는 첫 글자의 인덱스 반환, 없으면 -1
    .rfind(st)           # 마지막으로 일치하는 첫 글자의 인덱스 반환, 없으면 -1
    .count(st)           # 갯수 카운트
    .isalnum()           # 모두 숫자?
    .isalpha()           # 모두 영자?
    .strip(st)           # 양단의 st의 각 글자들을 제거 
    .lstrip(st)
    .rstrip(st)
    .capitalize()        # 첫 글자만 대문자
    .title()             # 각 단어의 머리를 대문자로 
    .upper()
    .lower()
    .swapcase()          # 대소를 역전
    .center(100)         # 100칸 공백의 중앙에 문자열을 배치, 2번째 인수로 채움
    .ljust(100)          # 100칸 공백의 왼쪽정렬, 2번째 인수로 채움
    .rjust(100)          # 오른쪽 정렬, 2번째 인수로 채움
    .replace(st1, st2, num)         # st을 st2로 치환, num횟수만큼(생략시 전체에 대해 치환)

def test():
    pass
print(len(['1', 1, 1.1, True, [1, 2], test]))       # 튜플, 집합, 사전도 배열 요소로 가능

list()                      # []
list('lcmz')[-1]            # z
list(range(1,6))[::-1]      # [5, 4, 3, 2, 1]
del [1, 2, 3][0]            # index로 지움
[1, 'z', 3].remove('z')     # 동일요소를 지움
1 in [1, 2, 3]              # True

arr함수
    .append(el)
    .extend(otherArr)       # arr1 += arr2
    .insert(index, el)
    .pop(index)             # index생략 시, 맨 뒤 추출
    .index(el)
    .count(el)
    .sort(reverse=True, key=str.lower)      # 원본 변환, 오름차순을 reverse
sorted(arr, reverse=True, key=str.lower)    # 새로운 리스트 반환, dict사용가능(key만 사용됨)
    .copy()         # [:] or list(arr)

tuple1 = '1',           # 하나일 때는 콤마
tuple2 = ('1', '2')     # 괄호 생략 가능
a, b = tuple2
print(tuple2[0])
tuple(arr)

dic1 = {}; dic1[11] = 2             # {11: 2}, 키로 객체 가능 
del dic1[11]
dic2 = dict([[1, 2], [3, 4]])       # {1: 2, 3: 4}, 리스트의 튜플도 가능
dic3 = dict(['12', '23'])           # {'1': '2', '2': '3'}
{'a' : 1}['b']                      # err
'a' in {'a' : 1, 'b' : 2}
sorted({1:1, 3:3, 2:2}.items())     # 사전의 키로 정렬 - 튜플의 리스트
dict함수
    .update(otherDict)          # 합침, 동일키는 업데이트
    .clear()
    .get(key, 'default value')  # 키가 없으면 err때문에 사용, str지정 안할 시 None반환 
    .keys()
    .values()
    .items()
    .copy()
    .setdefault(k, v)           # 키가 없으면 넣고, 있으면 무효

set1 = set()
set2 = {1, 2, 3}
set3 = set('aabbc')         # dict는 key가지고 만듬

{1, 2, 3} & {1, 3}      # {1, 3}, a.intersection(b)
{1, 2} | {2, 3}         # {1, 2, 3}, a.union(b)
{1, 2} - {2}            # {1}, a.difference(b)
{1, 2} ^ {2, 3}         # {1, 3}, a.symmetric_difference(b)
{1, 2} <= {1, 2}        # True, a.issubset(b) <-> a.issuperset(b)
{1, 2} < {1, 2}         # False, 

not True    # False
if True and not (1 != 1):       # if -> elif -> else, and/or + not
    pass

False값
    None
    0
    0.0
    ''
    []
    ()
    {}
    set()
    
input('your input :')

for-else    # break안되면 else문 실행
while-else

for a, b in zip(['a', 'b'], [1, 2]):
    print(a, b)     # a 1, b 2, 가장 작은 리스트를 다돌면 멈춤
    
li1 = [num for num in range(1, 6) if num % 2 == 0]
li2 = [[row, col] for row in range(1, 4) for col in range(1, 3)]    # if, 중복for 가능
dict1 = {word : 'aabbcdd'.count(word) for word in set('aabbcdd')}    # if, 중복for 가능

generator1 = {num for num in range(1, 6)}       # 제네레이터는 1회용
def generator2(a=1, b=11):
    while a < b:
        yield a
        a += 1
var_gene2 = generator2()
for a in var_gene2:
    print(a)

함수 내 전달받은 변수 : parameter
함수 호출 시 전달하는 변수 : argument
* 리스트, 사전은 id가 같기 때문에 복제(copy, [:])해서 전달! 

str1 = None
str1 is None        # str1 == None
# str, int 등 타입 확인할 때는 isinstance로 확인

def func1(a=1, b=2):
    '''
    doc string2
    '''
    print(a, b)
func1(3)
help(func1)         # func1.__doc__

li = list(range(1, 6))
print(sum(li)/len(li))

print((lambda x, y: x + y)(1, 2))

def func1(func):
    def new_func(*args, **kwargs):
        print(args, kwargs)
        return func(*args, **kwargs)
    return new_func
@func1
def func2(a, b):
    print(a + b)
func2(1, 2)

var1 = 1
def change_global_var(*args):
    global var1
    var1 = 2
    var2 = 3
    print('global :', globals(), '\n', 'locals :', locals(), '\n', 'vars :', vars())
change_global_var(4)

class CustomError(Exception):
    pass
try:
    # [1, 2, 3][3]
    raise CustomError('good')
except IndexError as err:           # 모듈에도 as 가능
    print('err message :', err)
except CustomError as cse:
    print('err message :', cse)
except Exception as other:
    print('err message :', other)

패키지(모듈이 모인 디렉토리)를 지정하기 위해서는 __init__.py 를 생성, 내용은 없어도 됨
모듈은 싱글톤(몇 번 참조되어도 한번만 로드)
모듈 sys
    .argv       # 프롬프트 실행 시 넘어온 arguments 배열 반환
    .path       # 모듈 찾는 경로

모듈 random
    .choice(arr)
    .sample(arr, num)       # arr에서 num개수 추출
    .shuffle(arr)

모듈 collections
    .defaultdict(defaultValue)      # 사전 반환, 없는 키를 조회 시, 자동으로 키가 생성, defaultValue(함수/람다 사용 가능-return값)가 설정 됨
    .Counter(arr)                   # 요소 수 계산하여, 사전 반환
from collections import Counter as C
a = {1:1, 2:2, 3:3}
b = [1, 1, 2, 3, 4]
print(sorted((C(a) + C(b)).most_common()))      # sorted는 사전의 배열은 지원안됨
                                                # Counter객체는 +, - , &, | 지원
    .OrderedDict(dic or tup sequence)       # 추가한 순서 기억
    .deque                          # 스택 + 큐
    .namedtuple                     # 불변의 dict, 일반 class보다 적은 메모리 사용, .name으로 접근가능
from collections import namedtuple
from math import sqrt
Point = namedtuple('Point', 'x y')
pt1 = Point(**{'x' : 1, 'y' : 2})
pt2 = Point(2, 3)
length = sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)
print('{:X<10.3f}'.format(length))

모듈 itertools
    .chain(arr1, arr2)      # 하나의 리터럴로 반환
    .cycle(arr)             # 무한 반복
    .accumulate(arr, func)        # 디폴트 : 0에서 각 요소의 합을 차례로 더해나가는 배열

모듈 math
    .sqrt(num)              # 제곱근

모듈 re         # regex
    .match(pattern, source)     # 첫 글자부터 검사 객체 반환 or None
        .group(name)            # 여러 패턴을 동시에 추출 할 때, (?P<name>pattern)를 사용해 name으로 추출
        .groups()
    .compile(pattern)           # 반환 된 객체로 사용
        .match(source)
        ...아래 함수들
    .search(pattern, source)    # 처음 매치된 것을 객체로 반환 or None
        .group()
        .groups()
    .findall(pattern, source)   # [] or 매칭된 문자열 리스트
    .split(pattern, source)     # [] or 스플릿 된 문자열 리스트
    .sub(pattern, replaceStr, source)   # 변환된 문자열 or 원본문자열
    
--pattern의 특수문자
숫자 : \d
숫자 이외 : \D
영자 : \w
영자 이외 : \W
공백 : \s 
공백 이외 : \S
--pattern의 메타 문자
expr1 | expr2       # 또는
prev{m}             # m번 연속
prev{m, n}          # m이상 n이하
prev(?=next)        # next가 있는 prev, 출력은 prev만
prev(?!next)        # next가 없는 prev, 출력은 prev만
(?<= prev) next     # prev가 있는 next, 출력은 next만
(?<! prev) next     # prev가 없는 next, 출력은 next만

클래스는 모듈을 지원안함? 
class A():
    count = 0                           # 클래스 변수
    def __init__(self, name):           # self이면 인스턴스 함수
        self.__name = name
        A.count += 1
    @classmethod
    def clsfunc(cls, str):              # cls면 클래스 함수
        print(f'{cls.__name__}\' this is description {str}', cls.count)
    @staticmethod
    def stafunc():                      # self나 cls를 받지않음
        print('static func')
class B(A):
    def __init__(self, name, num):      # 오버라이드
        super().__init__(name)
        self.__num = num
    def get_num(self):
        print('getter')
        return self.__num               # __name 사용 시 에러, A에서 정의해야 함, 
    def set_num(self, num):
        print('setter')
        self.__num = num
    hiddened_num = property(get_num, set_num)
test = B(1, 2)
print(test.hiddened_num)
test.hiddened_num = 2
test.clsfunc('test')
test.stafunc()

class C(A):
    def __init__(self, name, num):
        super().__init__(name)
        self.__num = num
    @property
    def hiddened_num(self):
        print('getter')
        return self.__num
    @hiddened_num.setter
    def hiddened_num(self, num):
        print('setter')
        self.__num = num
test2 = C(2, 3)
print(test2.hiddened_num)       # test2._C__num 로도 접근 가능함
test2.hiddened_num = 4

print(isinstance(test2, A))     # True
print(isinstance(test2, C))     # True


클래스 기본 정의 함수
    __str__(self)           # print, str 메소드 사용시 호출
    __repr__(self)          # 에코 출력
    __len__(self)           #
    __eq__(self, other)     # ==
    __ne__(self, other)     # !=
    __lt__(self, other)     # <
    __gt__(self, other)     # >
    __le__(self, other)     # <=
    __ge__(self, other)     # >=
    __add__(self, other)    # +
    __sub__(self, other)    # -
    __mul__(self, other)    # *
    __floordiv__(self, other)   # //
    __truediv__(self, other)    # /
    __mod__(self, other)    # %
    __pow__(self, other)    # **

import unicodedata
print('\u2603')         # 16진수,  면번호 2자리 + 인덱스 2자리, 상위면 문자는 '\U0' + 7자리 
print(unicodedata.lookup(unicodedata.name("\u2603")))
print('\N{snowman}')
snowman = '☃'
snowman.encode('utf-8', 'unicode-escape').decode('utf-8')     # utf-8로 인코딩(1~4 바이트) 안될 시, unicode-escape(파이썬 형식) 사용, 다른 소스에서 복붙시 utf-8으로 인코딩이 되어있는지 확인

'{:!<10d} {:-^10s} {:*^10.5f} {} {:<3.3e}'.format(1, 'd', 1.1, 123, 123 )
# 1!!!!!!!!! ----d----- *1.10000** 123 1.230e+02

bytes(range(0, 256))        # Immutable, range(0, 256)만 가능 -> ascii로 포현
bytearray([1, 2, 3])        # mutable
import struct
w1, h1 = struct.unpack('>LL', b'\x00\x00\x00\x9a\x00\x00\x00\x8d')        # 바이너리 디코딩
w2, h2 = struct.unpack('>3xB3xB', b'\x00\x00\x00\x9a\x00\x00\x00\x8d')        # 바이너리 디코딩
    # 포맷 : <(리틀에디안), >(빅에디안)
    # 서식 : x(1바이트 날림), B(부호없는 1바이트), L(부호없는 긴 4바이트 정수), ...
print(f'w1 : {w1}, h1 : {h1}')
print(f'w2 : {w2}, h2 : {h2}')

import binascii
hexlified = binascii.hexlify(b'\x89PNG\r\n\x1a\n')       # \xXX + ascii --> 16진수 시퀀스
print(binascii.unhexlify(hexlified))

with open('./test', 'wt') as fout:     # x는 파일이 없으면 쓰기, b는 바이너리
    fout.write('test1 good \n')
    print('test2 good', 'test3 good', file=fout)      # 각 인수 사이에 ' ', 끝에는 개행추가
    print('test4 good', 'test5 good', file=fout, sep='', end='')      # write처럼 동작
with open('./test', 'rt') as fin:
    print(fin.readline)             # for을 써도 동일
    fin.tell()                      # offset 반환
    fin.seek(100)                   # offset이동, 두번 째 인수: 0(디폴트-선두부터), 1(현재위치부터), 2(끝에서)
    print(fin.readlines())          # 한 줄씩의 리스트 반환
    # print(fin.read())

try:
    with open('./test', 'xt') as fout:
        fout.write('first')
except FileExistsError:
    print('already exists')

def outString(str):
        print(f'str : {str}')   #js의 템플릿 리터럴, return값은 None

csv(모듈 csv), xml(모듈 xml or defusedxml(보안).etree.ElementTree), yaml(모듈 yaml), 
ini(모듈 configparser), xlrd(모듈 xlrd 서드파티)
230p
HDF5(대규모 데이터 랜덤 액세스, 정규화, 데이터베이스 대용 등.. WORM-wirte once/read many- 으로 사용 )
기타.. h5py, PyTables

import json
num_json = json.dumps({1:1, 2:2, 3:3})      # 객체는 안됨
print(json.loads(num_json))

import pickle, datetime
now = datetime.datetime.utcnow()
pickled = pickle.dumps(now)                 # 바이너리로 직렬화
print(pickle.loads(pickled))

li = ['a', 'b', 'c', 'd']
for i, e in enumerate(li ,5):
    print(i, e)
for i in range(0, len(li)):
    print(i, li[i])

def func(num):
    return num + 5
li = [1, 2, 3, 4]
print(list(map(func, li)))          # 각 요소에 대해 func 적용

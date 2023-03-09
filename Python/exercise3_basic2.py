def test1(name: str, num: int) -> str:
    st = f'name: {name}, num: {num}'
    print(st)
    return st
test1('mg', 1)

def test2(name: [(int)]) -> []:
    print(name)
    return name
test2([(1, 2), (1, 2, 3)])


모듈 os
    .path.exists(name)
    .path.isfile(name)
    .path.isdir(name)
    .path.isabs(name)
    .rename(name1, name2)
    .link(name, linkname)
    .symlink(name, symname)
    .path.islink(name)
    .chmod(name, 0o777)
    .chown(name, uid, gid)
    .path.abspath(name)
    .path.realpath(name)     # 링크 파일의 실제링크
    .remove(name)
    .path.exists(name)
    .mkdir(name)
    .rmdir(name)
    .listdir(name)
    .chdir(name)            # cd
    .getpid()
    .getuid()
    .getcwd()               # pwd
    
import shutil
shutil.copy('file', 'copied_file')

import glob2
glob2.glob('*')       # 매칭된 파일들을 배열로 반환

import calendar
print(calendar.isleap(2021))    # 윤년(약 4년마다 d+1) 확인


from datetime import datetime, date, time
dt = datetime.now()
d = date.today()
t = time(12, 0, 0)
print(f'date time : {dt} \ndate : {d} \ntime : {t}')
print(dt.strftime('fmt : %Y %m(%b) %d(%a), %H:%M:%S'))


import time
now = time.time()
cnow = time.ctime(now)
utcnow = time.ctime(time.mktime(time.gmtime(now)))      # now생략 가능
print(f'unix now : {now} \ncnow : {cnow} \nutc now : {utcnow}')


from datetime import datetime
import time
dt = datetime.now()
print(time.mktime(dt.timetuple()))


import locale
for k, v in locale.locale_alias.items():
    print(k, ':', v)

--------------------------------------------------------------------------------

from timeit import timeit, repeat

def test():
    start = 0
    for num in range(0,2**10):
        start += num
    return start

print(timeit(test, number=1), 'sec')
print(repeat(test, number=1, repeat=3), 'sec')

성능향샹 : Cython, Numpy, C extension, ...           
--------------------------------------------------------------------------------
DEBUG
INFO
WARNING - default
ERROR
CRITICAL

import logging

def __get_logger():

    __logger = logging.getLogger('logger')

    formatter = logging.Formatter(
        'BATCH##AWSBATCH##%(levelname)s##%(asctime)s##%(message)s >> @@file::%(filename)s@@line::%(lineno)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    __logger.addHandler(stream_handler)
    __logger.setLevel(logging.DEBUG)

    return __logger

logger = __get_logger()

# logger.info("[BATCH EXCHANGE WAIT] %s @@RunTime[%.02f] @@SendCount[%d]" % (
#         __BATCH_MODE, running_time, send_count))

logger.info('((info log))')

--------------------------------------------------------------------------------

TCP/IP 소켓 통신 353p~

크롤러 / 스파이더 : 읽기(크롤)
스크레이퍼 : 탐색, 분석
BeautifulSoup4(간단-html분석용), scrapy(본격용)

자동화 : buildbot, jenkins, travis-ci, ...
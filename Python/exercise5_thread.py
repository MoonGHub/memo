import subprocess
comm = 'echo $HOME'
result1 = subprocess.getoutput(comm)       # 쉘 명령어 수행
print(result1)
result2 = subprocess.getstatusoutput(comm)
print(result2)

멀티프로세스 모듈 : multiprocessing(315p)
스레드 모듈 : threading(333p)
기타 이벤트 루프 : twisted, asyncio, Redis, (340p~)

----------------------------------------------------------------------------------

import gevent       # 이벤트 루프로 구동(nginx), 코루틴(협력형 멀티 태스팅-지연되는 동안 다른 일을 함)
                    # gevent는 비동기 처리, gevent사이에서는 동기 처리
import time

def func1(num):
    time.sleep(1)
    print('event', num, ': 1 sec suspend')
    return num

jobs = [gevent.spawn(func1, num) for num in range(0,6)]

print('not gevent code1')

extra_job = [gevent.spawn(func1, 999)]      # 이벤트 루프의 마지막에 추가됨
gevent.wait(extra_job)                      # 앞의 모든 루프가 끝나고, extra_job이 끝날 때 까지 기다림
print(extra_job[0].value)

print('not gevent code2')

gevent.joinall(jobs, timeout=10)            # joinall과 wait는 동일?, 위의 wait로 인해 무용지물 
for job in jobs:
    print(job.value)

print('wait나 joinall에서 기다림')



모듈 gevent
    .socket
    .monkey


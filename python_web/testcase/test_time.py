'''
perf_counter():用来计算程序运行时间
'''
import time,os
from time import strftime
def test_time_demo():
    start=time.perf_counter()
    for x in range(10):
        time.sleep(0.1)
    end=time.perf_counter()
    print(f'use time:{end-start}')


def test_02():
    return strftime('%Y-%m-%d %H:%M:%S',time.localtime())


print(test_02())
print(os.path.curdir)
print(os.path.abspath(os.path.curdir))
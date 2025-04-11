# 내 파이썬 프로그램의 이름을 알아보자.
#psutil 아이디 조회, 08.py 이름과 같은 아이디를 찾으면 그 아이디 출력한다

import os
import psutil
from multiprocessing import Process

import psutil

def ps_id() :
    print('프로세스 아이디 조회', os.getpid)

for proc in psutil.process_iter() :
    ps_name = proc.name()

if __name__ == '__main__' :
    print('08.py 프로세스 이름:', proc.name())
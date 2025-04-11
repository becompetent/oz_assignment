from multiprocessing import Process
import os
import time

def func() :
    print('안녕, 나는 실험용으로 대충 만들어 본 함수!') 
    print('나의 프로세스 아이디:', os.getpid())
    print('나의 부모프로세스 아이디:', os.getppid()) #부모프로세스 아이디(파이썬프로그램)

if __name__ == '__main__' :
    print('06.py 프로세스 아이디:', os.getpid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=func)
    child2.start()
    child3 = Process(target=func)
    child3.start()
    child4 = Process(target=func)
    child4.start()
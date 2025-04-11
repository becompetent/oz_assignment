from multiprocessing import Process
import os

def func() :
    print('안녕, 나는 실험용으로 대충 만들어 본 함수!') 
    print('나의 프로세스 아이디:', os.getpid())
    print('나의 부모프로세스 아이디:', os.getppid()) #부모프로세스 아이디(파이썬프로그램)

if __name__ == '__main__' :
    print('05.py 프로세스 아이디:', os.getpid())
    child = Process(target=func).start()
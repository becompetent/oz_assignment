from multiprocessing import Process
import os
import time

def coke() :
    print("콜라 프로세스 아이디 : ", os.getpid())
    print("부모 프로세스 아이디 : ", os.getppid())

def cider() :
    print("사이다 프로세스 아이디 : ", os.getpid())
    print("부모 프로세스 아이디 : ", os.getppid())

def juice() :
    print("주스 프로세스 아이디 : ", os.getpid())
    print("부모 프로세스 아이디 : ", os.getppid())

if __name__ == '__main__' :
    print('07.py 프로세스 아이디:', os.getpid())
    child1 = Process(target=coke)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=cider)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=juice)
    child3.start()
    time.sleep(0.5)
    
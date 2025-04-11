from multiprocessing import Process
import os
import time

def coke() :
    while True :
        try :
            print("콜라 프로세스 아이디 : ", os.getpid())
            print("부모 프로세스 아이디 : ", os.getppid())
        except KeyboardInterrupt :
            break

def cider() :
    while True :
        try :
            print("사이다 프로세스 아이디 : ", os.getpid())
            print("부모 프로세스 아이디 : ", os.getppid())
        except KeyboardInterrupt :
            break

def juice() :
    while True :
        try :
            print("주스 프로세스 아이디 : ", os.getpid())
            print("부모 프로세스 아이디 : ", os.getppid())
        except KeyboardInterrupt :
            break

if __name__ == '__main__' :
    print('11.py 프로세스 아이디:', os.getpid())
    child1 = Process(target=coke)
    child1.start()
    time.sleep(0.5)
    child2 = Process(target=cider)
    child2.start()
    time.sleep(0.5)
    child3 = Process(target=juice)
    child3.start()
    time.sleep(0.5)
    
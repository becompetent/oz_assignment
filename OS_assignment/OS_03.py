# pip install psutil 모듈 설치
# 내 컴퓨터에서 돌아가는 프로세스 조회하기

import psutil

for proc in psutil.process_iter() : #iteration: 반복적으로 수행한다
    
    ps_name = proc.name()
    if "Chrome" in ps_name :   # Chrome 이라는 프로세스 프린트
        print(ps_name, proc.pid)
## 운영체제 01일차 챌린지 과제

### 1. CPU 구성요소 ALU, CU 그리고 레지스터의 각각의 역할을 간략하게 정리
   * 전체 흐름<br>
     : 응용프로그램 실행 --> 실행명령어나 함수 Register Set에 잠시 저장 --> CU(Control Unit)에서 명령어, <br>
       함수 등 코드 해석하여 ALU에게 전달 --> ALU(Arithmetic and Logical Unit)에서 전달받은 코드로 산술 혹은 논리 연산 진행

   * CPU의 구성요소 및 역할<br>

    a. 구성요소: CPU(Central Processing Unit)는 ALU이라는 연산자 유니트, CU라는 제어유니트, 레지스터(Register Set)로 구성되어 있다.  
     
    b. Register Set : 레지스터로서 CPU가 처리할 명령어를 임시 저장하는 곳
    
    c. CU(Control Unit) : 제어유니트로서 CPU가 처리할 명령어를 ALU로 전달하기 위한 해석(Decode)역할
     
    d. ALU(Arithmetic and Logical Unit) : 연산자 유니트로서 CU(Control Unit)에서 해석해준 코드를 산술 혹은 논술을 연산해주는 역할
        
### 2. 메인메모리와 보조기억장치의 차이 간략 설명<br>
     메인메모리는 프로그램이 실행되는 파일이 실행되는 공간이고 RAM(Random Access Memory)라고도 한다.
     보조기억장치는 프로그램이 실행되기 전, 또는 프로그램 종료 후 저정되는 공간을 말하고 하드디스크(HDD)나 SSD가 이에 속한다.
   
### 3. 버스시스템은 데이터를 주고받기 위한 경로로, 데이터의 종류에 따라 세 가지로 구분할 수 있다.<br>
### 세 가지는 무엇인지 말해보자.<br>
   
   * 데이터 버스시스템 : CPU - 메모리 사이의 데이터 이동을 위해 필요한 버스
   
   * 컨트롤 버스시스템 : CPU가 원하는 바를 메모리에 전달하기 위한 버스

   * 어드레스 버스시스템 : 주소값을 이동하기 위해 필요한 버스

    * 내가 이해한 어드레스 버스시스템 
     Django의 경우 "from rest_framework import serializers" 처럼
     "rest_framework에 있는 serializers 기능"을 불러오기 위해 주소처럼 위치를 입력해주거나

     터미널에서 디렉토리 위치로 이동하는 경우 " cd ~/Desktop/oz_assignment/" 라는 명령어로 위치를 입력하는 것처럼
     주소값을 어드레스 버스시스템을 통해 이동하여 CPU가 빠르게 처리할 수 있는 역할을 어드레스 버스시스템이 하는 것이라고 생각한다. 

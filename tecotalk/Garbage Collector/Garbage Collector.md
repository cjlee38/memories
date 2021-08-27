# Garbage Collector

## JVM ?
운영체제의 메모리 영역에 접근하여 메모리를 관리하는 프로그램

## Garbage Collector ?
동적으로 할당한 메모리 영역 중 사용하지 않는 영역을 탐지하여 해제하는 기능.  
즉, 참조되지 않는 객체의 메모리를 해제(free in C)

## stack과 heap
stack 영역에는 지역 변수를 보관, 객체를 생성할 경우 참조변수(포인터)가 스택에 저장되고, 해당 변수가 가리키는 실제 객체는 heap에 저장.

## gc 과정
1. stack의 모든 변수를 스캔하면서, 어떤 객체를 참조하는지 마킹
2. 해당 객체가 참조하고 있는 객체도 찾아서 마킹
3. 마킹되지 않은 객체를 제거
= markAndSweep

## gc가 언제 일어나는가 ?
heap 영역을 new generation (eden / survival 0 / survival 1)
old generation 으로 나눌 수 있음.

eden에 가득 차면, mark and sweep을 하고, 남은 객체를 survival 0로 이동(= minor gc) & 반복  
survival 0가 가득차면 ? survival 0 영역에 대해서 mark and sweep, 남는 녀석을 survival 1로 이동 (age 증가)

survival 1이 가득차면 ? survival 0 으로 이동. (age 증가)

이 과정을 계속 반복하다가, age 값이 특정 값 이상이 되면 old generation으로 promotion

old generation이 가득 차면 major gc

## stop the world
gc를 수행하기 위해 프로세스의 실행을 멈추는것.

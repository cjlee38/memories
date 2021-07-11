# spring webflux
## spring framework의 특징 ?
DI, IOC, PSA, POJO... 경량 프레임워크 ...

## spring framework 5.x 의 특징
- jdk 8 이상
- 코틀린 기반 함수형 프로그래밍
- junit 5
- jdbc 4, hibernate 5
- 그리고 ::reactive programming:: 지원

**reactive programming ??**
## spring webflux가 생겨난 배경
: 적은 수의 스레로 동시성을 처리 / Non-blocking / Functional Programming
![](spring%20webflux/88651709-1574-40A6-B299-E84D0B3D58EC.png)

기존 Spring MVC에서는 "요청 하나를 스레드 하나가 전담마크"
따라서 그 I/O 중에는 스레드가 멈추게 됨
![](spring%20webflux/F2DF9859-DFE6-42EC-9E7D-83CEB491D3C1.png)

**그렇다면 Webflux가 MVC보다 빠른가?**
꼭 그렇지는 않다. 적은 스레드와 메모리를 효율적으로 사용할 수 있을 뿐

## so..
**Reactive Stream ?**
Async, Non-blocking 기반의 stream (확장 버전?)
publisher에서 데이터가 발생하면(혹은 변경이 생기면), subscriber에게 push

**backpressure**
subscriber로 들어오는 stream의 양을 조정.

*엑셀에서, 다른 셀을 참조하는 셀의 실시간 변화를 생각해보자*

## Flux & Mono
0 - N 개의 item을 갖는 stream이라고 생각.. ( list, set 등의 자료구조라고 생각하면 될 듯)
0 - 1 개의 item을 갖는 것. ( primitive data type을 생각하면 될 듯)

<기능 설명>
16:53 ~ 20:22

## spring mvc vs spring webflux
![](spring%20webflux/8F1FCDEA-02FF-4094-BF33-57BBA62649D1.png)

이분적인게 아니고, 서로 상호보완적

## webflux를 쓰려면
1. 일단 end to end 로 모두 reactive를 적용해야한다 (mvc 사용 x)
2. 그런데 기존에 제대로 동작하고 있는 mvc가 있다면, 굳이 바꿀 필요는 없다
3. reactive programming의 learning curve는 가파르다.






#테코톡
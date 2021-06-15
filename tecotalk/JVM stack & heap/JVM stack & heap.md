# JVM stack & heap
[YouTube](https://www.youtube.com/watch?v=UzaGOXKVhwU) by 무민

## 문제상황
OS & CPU 에 따라 system call inteface와 instructions set 이 다르다
--> 플랫폼이 다를 경우 실행이 안됨

따라서 java는 JVM 이라는 layer를 통해 해결
즉, java byte code는 플랫폼에 관계없이 jvm 위에서 동작
(물론, jvm은 플랫폼에 종속적)

## 굳이 JVM 을 도입한 이유?
C/C++ 도 크로스컴파일해서 배포하면 되는데, 굳이 JVM을 사용해야 하는 이유가 있을까?
--> 자바는 네트워크에 연결된 모든 디바이스에서 작동하는 것이 목적.
이러한 디바이스마다 운영체제와 하드웨어가 다르기 때문에, 플랫폼에 종속적이지 않도록 언어를 설계


![](JVM%20stack%20&%20heap/EE5E579A-F70D-4CE8-B839-C01AAC7237A4.png)
**자바가 컴파일 되는 과정**

일반적(웹)으로 프론트엔드가 클라이언트에 종속적인데,
컴파일러는 서버(플랫폼)에 종속적임 = 프론트엔드는 공유.

* JIT 컴파일러 -> 런타임 과정에서 벌어지는 최적화

# Runtime Data Areas
: JVM이 java bytecode를 실행하기 위해 사용하는 메모리 공간

![](JVM%20stack%20&%20heap/20981134-93BE-4F89-8C54-F7054863C2FD.png)

* method area : 클래스 로더가 클래스 파일을 읽고, 파싱해서 method area에 저장. 
(클래스는 무엇이 있고, 변수는 무엇이 있고, 함수는 무엇이 있고 ...)
* heap : 프로그램을 실행하면서 생성한 객체 instance를 저장하는 곳.
* stack, pc register, native method stacks는 스레드마다 존재
	1. pc ? program counter : 각 스레드는 메소드를 실행하고 있는데, pc는 그 메소드에서 몇 번째 줄을 실행하는지 가리키는 역할	
	2. stack은 메소드가 호출될때마다 생성됨, 메소드 실행이 끝나면 stack frame이 pop.
  stack frame : 내 메소드가 어디에 속하는지, 나를 호출한 메소드가 누구인지, 갖고있는 변수 들에 대한 정보를 갖고 있음.
	3.  java bytecode가 아니라, c 혹은 c++ 등으로 작성된 메소드(빠른 속도를 위해)

## byte code 동작
동영상을 직접 보는 편이 이해가 빠를듯 (9:46)

![](JVM%20stack%20&%20heap/E040E7CA-7A7B-47D0-B9E7-2ED2BF5498CF.png)

## 레지스터가 아니라 stack frame을 쓴 이유 
: 디바이스 별 레지스터의 개수를 보장할 수 없기 때문에 (=호환성)
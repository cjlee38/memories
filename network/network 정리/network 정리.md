# network 정리

## IP Address
컴퓨터 네트워크에서 장치들이 서로 인식하고 통신하기 위해 사용하는 주소

* IPv4 =  32개의 비트를 갖는 2진수
* IPv6 =  128개의 비트를 갖는 2진수

초기에는 IPv4로 모두 표현할 수 있을거라 생각했지만, 곧 고갈되어 IPv6로 전환중

각 8비트를 옥텟(Octet)이라 부름.

## IP Address Class
네트워크 주소와 호스트 주소를 구분하는 약속.
(서울시 동대문구 ... 101호 != 대전시 서구 ... 101호)

- A class = 첫 비트가 0
- B class = 첫 두 비트가 10
- C class = 첫 세 비트가 110
- D class = 첫 네 비트가 1110 (mutlicast)
- E class = 첫 네 비트가 1111 (reserved)

e.g. A class
0000 0000. 0000 0000. 0000 0000. 0000 0000 ~ 0111 1111. 1111 1111. 1111 1111. 1111 1111
를 가질 수 있음
즉, 0.0.0.0 ~ 127.255.255.255
이 때, 127은 제외하고 1.0.0.0 ~ 126.0.0.0 으로 규정되어 있음
(0.0.0.0은..?)

**A클래스는 첫 octet는 네트워크를, 나머지는 호스트를 나타냄**

> Note. 호스트 주소에서 모두 0이면 네트워크 주소, 모두 1이면 브로드캐스트 주소  
> 따라서 호스트 주소의 개수는 2^(호스트 비트) - 2  

B 클래스는 128.0.0.0 ~ 191.255.255.255
따라서 네트워크 범위는 2^14 개, 호스트 범위는 2^16 - 2 개
**B 클래스는 첫 두 octet은 네트워크를, 나머지는 호스트를 나타냄**

정리하면 이렇게

![](network%20%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%B5/8EDA28A7-4AAD-4C7B-9B07-1D02667DFFAF.png)

> Note. loop back adress(localhost) = 127.0.0.1  

> Note. 왜 이런짓을 하느냐?  
> -> 동대문구 101호 vs 동대문구 회기로 ...번지 101호는 다름.  
> 즉, 효율적인 통신을 위해 사용하는 것  

## 사설 IP
기존의 IP 주소를 할당받기 위해서는 돈을 내야 함. 왜? 한정되어 있기 때문에
따라서 사설 네트워크를 구축함.

사설 IP 주소의 범위는 다음과 같음.
10.0.0.0 ~ 10.255.255.255 (10.0.0.0/8) : 1개의 A 클래스
172.16.0.0 ~ 172.31.255.255(172.16.0.0/12) : 16개의 B 클래스
192.168.0.0 ~ 192.168.255.255(192.168.0.0/16) : 256개의 C 클래스

**공인 IP는 사설IP 영역을 사용할 수 없다**## 서브넷 마스크
CIDR = Classless Inter Domain Routing. 클래스 없는 도메인간 라우팅 기법
기존의 Class System을 보완하기 위해 나옴.

e.g. 123.123.123.123/24

뒤에 붙은 24가 CIDR 표기법. 이러한 CIDR은 0부터 32까지의 값을 가질 수 있음.

example = 143.7.65.203/23

비트로 표현하면
10001111 . 00000111 . 01000001 . 11001011 ::IP address::
11111111   . 11111111    .  11111110    . 00000000 ::CIDR::

그러면, 3옥텟의 마지막에 있는 0은 0 또는 1이 될 수 있음.
말인 즉슨, IP 주소의 3옥텟에 있는 주소값이 0100 0000 혹은 0100 0001 
따라서, 0100 0000 = 64 // 0100 0001 = 65
뒤 4옥텟은 0 부터 255일테니.... 결국
143.7.64.0 ~ 143.7.65.255 의 대역을 사용함을 의미.

### 근데 지금까지 얘기한건 CIDR이고...
서브넷 마스크란건, subnetting, 즉 기존의 네트워크를 분할하겠다는 의미임.
따라서, 기존 A클래스, B클래스, C클래스를 좀 더 쪼개겠다는 의미.

예를 들어, C class의 default subnet mask는
11111111 . 11111111 . 11111111 . 00000000

10.0.0.1 에 서브넷을 적용하면?
기존 10.0.0.1 은 A클래스였는데, 서브넷을 저렇게 쓴다는 것은,
A클래스가 아니라 C클래스처럼 사용하겠다는 의미.
다시 말해, 뒤 8자리만 호스트로 사용하겠다는 의미.
다시 말해, 네트워크 영역을 늘리고 호스트 영역을 줄이겠다는 의미가 됨.








#network


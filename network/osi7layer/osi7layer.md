
OSI 7 Layer 던, TCP/IP 던, 결국 **통신 절차 표현**

e.g.  
서울에서 부산에 있는 친구에게 편지를 보내고 싶다. 그러면  
1. 편지지를 구해서, 글을 쓴다.
2. 편지봉투를 구해서, 보내는 사람과 받는 사람의 주소를 쓴다.
3. A 우체국에 편지를 보낸다. 이 때, 일반과 등기 우편이 있다.  
일반은 보내고 나면 끝, 등기는 잘 받았는지 확인하고, 못받으면 반송되기도 함. 이 차이점을 "신뢰성" 이라고 부름. 즉, 일반은 신뢰성이 떨어짐.
4. B 우체국에서는 다음 목적지를 향해 분류를 한다(서울에서 부산으로 직통으로 가는것이 아니기 때문)
5. 전달받은 B 우체국은, 주소를 보고 C 우체국으로 보냄.
6. 이 과정을 반복해서 결국 부산 우체국으로 보냄.
7. 부산 우체국에서 집배원이 부산에 있는 친구의 우체통에 편지를 넣어줌
8. 친구는 편지의 보내는 사람(나)과 받는 사람(친구)를 확인하고 편지를 뜯음.

이를 컴퓨터 프로그래밍에 적용하면 ?
1. 편지지에 편지를 씀 : Application(e.g. 카카오톡 프로그램)
2. ((Presentation과 Session은 생략...)) --> Application & Presentation & Session을 묶어서 TCP/IP 에서는 Application이라 부름.
3. 일반 or 등기 : Transport layer
4. 받는사람 & 보내는 사람 써놓은것 : Network
5. A 우체국 -> B 우체국 : Data Link
6. 우체국 간 배송을 어떻게 할것인가? (자동차? 비행기?) : Physical

> Note. TCP 랑 TCP/IP 랑 같은건가?  
When TCP and IP are mentioned separately then they mean a transport layer (RFC 793) and a network layer protocol (RFC 791) respectively. But when mentioned in TCP/IP format they mean a stack which TCP/IP suite.

TCP/IP 에서의 Transport 는 OSI의 Transport
TCP/IP 에서는 Internet을 OSI의 Internet
TCP/IP 에서의 Network는 OSI의 DataLink & Physical

---

OSI 7 계층이 표준이고, TCP/IP 는 비표준인데, 비표준임에도 불구하고 TCP/IP 를 위주로 씀. 사실상 표준.

네트워크의 장애는 1계층부터 올라가야 한다.

# 출처
https://www.youtube.com/watch?v=f4u1fKaZ4Jo

# proxy
단어 자체로는 "대리" 라는 뜻

# proxy server
클라이언트와 서버간의 중계 서버. 통신을 대리 수행하는 서버  
캐시/보안/트래픽 분산 등 여러 장점을 가질 수 있다.

# forward proxy
일반적인 proxy는 forward proxy.  
client 와 internet 사이에 있음.

## 특성 1. 캐싱
e.g. client A 가 server에 오늘 날씨를 물어봄. (중간에 proxy와 internet이 있음). server가 client A에게 응답을 해주기 전에 날씨정보를 캐싱. 다음에 B가 날씨 정보를 물어보려 할 때에 proxy가 대신 대답.  
-> 1. 전송시간 절약 2. 불필요한 외부 전송 X 3. 외부 요청 감소 (= 트래픽 감소)

## 특성 2. 익명성
server 입장에서는 forward proxy가 요청한 정보이기 때문에, 누가 보냈는지 알지 못함. 즉, server가 받은 요청 ip = proxy ip 

# Reverse Proxy
forward랑 비슷하지만, server 와 internet 사이에 있음.

## 특성 1. 캐싱
은 forward랑 같음

## 특성 2. 보안
client는 reverse proxy를 실제 서버라고 생각하여 요청 -> 실제 서버의 IP가 노출되지 않음.

## 특성 3. load balancing
: 부하 분산, 해야할 작업을 나누어 서버의 부하를 분산시키는 것
즉, 받은 요청을 서버들에게 공평하게 나눠줌.

server가 감당이 불가능해질 경우, scale up으로 임시 조치는 가능하지만 너무 많아지면 scale out을 해야 한다.

L4 로드밸런싱 : Transport Layer(IP & Port) level에서 로드밸런싱. 즉, 쉽게 생각하면 도메인을 기준으로 로드밸런싱
L7 로드밸런싱 : Application Layer level에서 로드밸런싱. 간단하게 생각하면 MSA에서 담당하는 서비스에 따라 로드밸런싱


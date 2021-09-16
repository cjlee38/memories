# hadoop ssh connection refused

* 시도 : ssh localhost도 잘 동작하는데, start-all.sh 를 실행하면 에러 발생
* 원인 : 접속하려는 곳의 이름이 cjlee-MacBookPro.local 이 아니고 cjleeui-MacBookPro.local
* 해결 : 시스템 환경설정 - 공유 - 컴퓨터 이름 수정

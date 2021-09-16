# Singleton

: 애플리케이션이 시작될 때, 최초 한번만 메모리에 할당되는 클래스(= static)
즉, 하나의 클래스에 단 하나의 인스턴스만 만들어진다.

**특징**   
* 메모리의 낭비를 방지할 수 있다.  
* 전역적으로 사용될 수 있기 때문에, 데이터의 공유가 쉽다.  
* 인스턴스의 단 생성이 단 한번만 이루어지기를 보장하고 싶을 때 사용한다.

**Example**
게임을 할 때 "설정"과 같은 부분은 전역적으로 이루어져야 하고, 여러 개가 있을 필요가 없다.



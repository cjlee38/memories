# Database Index

## index ?
임의의 규칙대로 부여된, 임의의 대상을 가리키는 무언가
e.g. 주민번호, 지도의 주소, 배열의 인덱스

## Clustered index vs Non-Clustered Index

### clustered index는...
: Cluster = 군집화
Clustered = 군집화
Clustered Index = 군집화된 인덱스.
즉, 인덱스가 데이터가 가까이 있다(=군집화되어있다.)

e.g.
index 41 -> A
index 42 -> B
index 43 -> C

**이런 상황에서, 새로운 데이터가 추가되어야 한다면 ?**
뒤쪽의 값을 모두 밀어내야 한다(마치 array처럼)

### non-clustered index는..
41 과 123 <- -> 123과 data
즉, 약한 참조
이 123이라는 숫자는 해쉬값

### clustered index는 pk와 비슷하다.
1. 순서대로 저장된다
2. 한 테이블에 하나만 존재한다.
3. 범위 검색에 유리하다
BUT
4. 존재하는 PK 사이에 INSERT 할 경우 대참사..
5. 그렇기 때문에 auto_increment를 사용한다.

## non clustered index는 반대
1. 순서와 관계 없다.
2. 한 테이블에 여러개가 존재할 수 있다.
BUT 
3. 추가 저장 공간이 필요하다
4. INSERT 시 인덱스를 생성하는 작업이 필요하다.
5. Cardinality -> 카디날리티가 낮으면, 인덱스가 의미가 약해지고, 카디날리티가 높을수록 인덱스가 큰 효과를 발휘한다.

## Advanced
* 실행계획
* B - Tree // Page(Block)
* Cardinality
* Composite Key (복합키)
* innodb_buffer_pool_size
* log_throttle_queries_not_using_index


#테코톡#
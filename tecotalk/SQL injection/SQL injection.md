# SQL injection
## SQL injection이란?
: 데이터베이스와 연동된 웹 애플리케이션에서,  
공격자가 입력이 가능한 폼에 ::조작된 질의문을 삽입:: 하여 웹 서비스의 데이터베이스 정보를 열람 또는 조작할 수 있는 취약점

## 피해사례
: 여기어때, 뽐..

## 공격하는 법 
query문 : select * from "table_name" where id = "some_id" and password = "some_password"
![](SQL%20injection/7484DFE0-5D3C-449E-BFC0-4A7D7A3DAFA9.png)

1. id 에 test(그냥 아무거나)
password에 패스워드가 아니라 '123' or '1' = '1'; 
이런식으로 넣으면 로그인이 성공한다.
2. id 뒤에 'something'; drop table "table_name(e.g.users)";
users 테이블의 내용을 모두 삭제

## 방어하는 법
* jdbc를 직접 사용하는 경우
preparedStatement 를 활용 ( = **파라미터 바인딩**)
```java
String query = "SELECT * FROM "table_name" WHERE id = ? and password = ?";
preparedStatement ps = connection.prepareStatement(query);
ps.setString(1, param_id);
ps.setString(2, param_password);
```

 **왜 파라미터 바인딩이 안전한가?**
파라미터 바인딩 함수 내부에, isEscapeNeededForString 이라는 조건검사 함수가 있는데, 이 함수가 escape sequence를 붙여줌.

* JPA 는 save() 같은 메소드를 활용할 경우, 파라미터 바인딩이 적용되기 때문에 괜찮다
### ::BUT::
jpa도 만약 쿼리를 직접 날리면 위험

#테코톡
# lambda expression
## 람다의 특징
1. 익명 : 일반적인 메소드와 다르게 이름이 없다.
2. 함수 : 특정 클래스에 종속되지 않으므로 함수(!= method) 라고 부른다.
3. 전달 : 람다를 메소드 인수로 전달하거나, **변수로 저장할 수 있다**
4. 간결성 : 익명 클래스처럼 자질구레한 코드를 구현할 필요가 없다.

## 람다의 구성
e.g. 
`(Apple a1, Apple a2) -> a1.getWeight().compareTo(a2.getWeight());`

* 파라미터 리스트 = (Apple a1, Apple a2)
* 화살표 = ->
* 람다 바디 = a1.getWeight().compareTo(a2.getWeight());

## 람다가 만들어질 수 있는 근원. 즉, 어디에 람다를 쓸 수 있을까?
::함수형 인터페이스::
즉, 하나의 abstract method만 갖는 인터페이스.

example =
```java
public interface Predicate<T> {
	boolean test(T t);
}

// or

public interface Runnable {
	void run();
}

// or

public interface Callabe<V> {
	v call() throws Exception;
}
```

람다 표현식이 함수형 인터페이스에 있는, **한 개의 abstract method**를 구현할 수 있음.
즉, 다시 말해 **람다 표현식을 함수형 인터페이스를 구현한 클래스의 인스턴스로 취급** 할 수 있다.

따라서, 다음의 두 코드는 같은 동작을 한다

```java
Runnable r1 = () -> System.out.println("Hello world");
Runnable r2 = new Runnable() {
	public void run() { // override
		System.out.println("Hello world");
	}
}
```

> Note : `@FunctionalInterface` annotation  
> 함수형 인터페이스를 가리키는 어노테이션. 즉, 함수형 인터페이스의 조건(=하나의 추상 메소드만 가져야한다)을 만족시키지 못하면 컴파일 에러가 발생한다.  

## 활용
다음과 같이, 파일을 **한 줄** 읽는 메소드가 있다고 해보자.

```java
public String processFile() throws IOException {
	try (BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
		return br.readLine();
	} ...
}
```

> Note : 이와 같이 초기화/준비 코드 이후에(*파일 열기*), 실제 수행(*한 줄 읽기*), 그리고 닫기(*파일 닫기*) 의 형태를 갖는 코드를 **실행 어라운드 패턴** 이라고 부른다.  

그런데, 한 줄이 아니라 두 줄을 읽고싶다면 어떻게 해야 할까?
즉, 다음과 같이 실행하고 싶다면 어떻게 해야 할까?
`String twoLineRead = processFile((BufferedReader br) -> br.readLine() + br.readLine());`

우선 함수형 인터페이스를 다음과 같이 만들자.

```java
@FunctionalInterface
public interface BufferedReaderProcessor {
	String process(BufferedReader br) throws IOExpcetion;
}
```

그리고, 메소드가 이에 해당하는 함수형 인터페이스를 받을 수 있도록 다음과 같이 작성할 수 있다.
```java
public String processFile(BufferedReaderProcessor p) throws IOException {
	try {BufferedReader br = new BufferedReader(new FileReader("data.txt"))) {
		return p.process(br);
	}
}
```


## 특징
1. 형식 추론
대상의 형식에 따라 함수 디스크립터를 알 수 있으므로, 람다의 시그니처로 추론할 수 있다. 즉, 파라미터의 형식을 추론할 수 있다.

example =
```java
// before
(Apple a1, Apple a2) -> a1.getWeight().compareTo(a2.getWeight())
// after
(a1, a2) -> a1.getWeight().compareTo(a2.getWeight())
```

2. 지역 변수 사용
파라미터로 넘겨진 변수가 아니라, 외부에서 정의된 변수(자유변수)를 활용할 수 있다 -> 이를 ::람다 캡쳐링:: 이라고 부른다.

example =
```java
int portNumber = 443;
Runnable r = () -> System.out.println(portNumber);
```

하지만, 다음과 같은 제약이 있다
1) 명시적으로 final로 선언되어 있어야 하거나
2) final로 선언된 변수와 똑같이 사용되어야 한다(=즉, 값을 재정의해서는 안된다)





#modern-java
# (Python) @Property까지 가는 길 - 1. @Property란

> Note 1. 개인적으로 공부해가며 작성한 글이기 때문에 틀린 내용이 있을 수 있습니다. 틀린 내용을 발견하시면 언제든 지적 부탁드립니다.
> Note 2. 이해를 돕기 위해 일부 내용은 Java와 비교해가며 글을 작성했습니다.

# 0. 들어가며
: 한동안 Java를 애용하다가, Python을 다뤄야 하는 일이 생겨서 다시 Python을 붙잡게 되었습니다. Java의 syntax에 대해서 어느정도 이해하고 있다고 자만하던 중이었기 때문에, Python을 사용하면서 "왜 Python에는 Java의 이런 기능이 없지? 역시 Java가 짱이야" 라는 생각도 하곤 했습니다.

getter와 setter에 대해서 알아보던 중, @property 라는 녀석을 이해해보려고 자료를 찾다 보니, Python의 진면목을 엿볼 수 있었습니다.

<center>
<iframe src="https://giphy.com/embed/cNO6wb9sEzK8N9rp5E" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/twitter-bravo-bravocon-con-cNO6wb9sEzK8N9rp5E"></a></p>
</center> 

<center>누가 파이썬이 쉽다 했습니까</center>

파이썬의 아주 기본적인 문법만 알고 있던 사람들에게 본 글이 시야를 넓히는데 도움이 되길 바라면서, 시작하겠습니다.

# 1. 그래서 @Property 가 뭔가요 ?
흔히 "객체지향" 에서는, 객체가 갖고 있는 `Field` 를 적절하게 외부로 노출시키거나 숨기기 위해, `getter/setter`를 사용합니다.

Java에서는 `private` 이라는 키워드로 갖고 있는 멤버변수들을 모두 숨기고, 보여줄 내용은 `getter` 메소드를, 외부에 의해 변경되어도 되는 변수는 `setter` 메소드를 활용해 데이터를 관리하죠. 

따라서 직접적으로 변수에 접근하는 것은 원천적으로 금지되어 있고, 메소드 호출을 통해서만 데이터를 조작할 수 있습니다.

```java

class Person {

    private String name;
    private int age;
    
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) {
        if (age <= 0) 
            throw new IllegalArgumentException("나이는 0 이하가 될 수 없습니다.");
        this.age = age;
    }

}
public class Main {
    public static void main(String[] args) {
        Person person = new Person("Mr.Kim", 26);
        System.out.println(person.getName()); // "Mr.Kim";
        person.setAge(-62); // IllegalArgumentException("나이는 0 이하가 될 수 없습니다.")
    }
}
```

그러나 python 에서는 programming language 수준에서 접근 권한을 제어할 수 없습니다. 따라서 _(언더스코어) 를 활용하는 방법을 제공하지만, 결국 `_{클래스명}__{변수명}` 으로 접근이 가능합니다.

따라서 python 에서는 기본적으로 모두 `public` 이라고 생각하면 됩니다. 하지만 그렇다고 해서 `getter/setter`를 쓸 필요가 없다는 것은 아닙니다. 당장 위와 같은 예시만 보더라도, `setAge()` 메소드를 호출할 때, 나이가 음수인지 아닌지 검증하는 로직이 필요하기 때문입니다. 위 코드를 파이썬으로는 다음과 같이 쓸 수 있습니다.

```python
class Person :
    def __init__(self, name, age) :
        self._name = name
        self._age = age
    
    # 다른 메소드는 편의상 생략합니다.

    def set_age(self, age) :
        if age <= 0 :
            raise Exception("나이는 0 이하가 될 수 없습니다.")
        self._age = age

if __name__ == '__main__' :
    person = Person("Mr.Kim", 26)
    person.set_age(-62) # Exception('나이는 0 이하가 될 수 없습니다.')
```

여기까지는 Java와 똑같습니다. 하지만, 이런 식의 코드 사용은 `explicit` 하지 못하다는 단점이 있습니다. 기존 나이에서 1살을 더해준다면, 다음과 같이 작성해야 합니다.

```python
person.set_age(person.get_age() + 1)
```

뿐만 아니라, `person._age = -62` 와 같은 코드는 방어할 수가 없어진다는 문제도 여전히 남아있죠. 그러나 `@Property` 를 활용하면 다음과 같은 코드가 가능합니다.

```python
person.age += 1
person.age = -62 # Exception('나이는 0 이하가 될 수 없습니다.')
```

??? 어떻게 된 일일까요? 변수에 값을 직접 대입하는 것 같은데, 로직에 따른 Exception을 던지고 있습니다. 어떻게 이것이 가능한지는 차차 알아보기로 하고, 일단 생김새부터 살펴봅시다. 위 `Person` 클래스에 `@Property`를 적용하면 다음과 같이 작성할 수 있습니다.

```python
class Person :
    def __init__(self, name, age) :
        self._name = name
        self._age = age
    
    @property
    def age(self) :
        return self._age
    
    @age.setter
    def age(self, age) :
        if age <= 0 :
            raise Exception("나이는 0 이하가 될 수 없습니다.")
        self._age = age
```

대충 살펴 봤을때, 눈에 띄는 차이점은 다음과 같습니다.

1. 함수의 이름이 `get_age` 혹은 `set_age` 가 아니라, 그냥 `age` 자체로 바뀌었습니다.
2. 계속 언급했던 `@property` 가 `age` 메소드 위에 붙었습니다. 또한, `@age.setter` 라는 녀석도 두 번째 `age` 메소드 위에 붙었습니다.

이러한 변화가 어떻게 앞서 언급했던 동작에 영향을 미쳤는지 하나씩 알아가봅시다. 

`@Property`를 이해하기 위한 배경지식들은 다음과 같습니다.
1. Everything is Object
2. Decorator
3. Descriptor Object

# 1. Everything is Object
파이썬에서 다루는 모든 
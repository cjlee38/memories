# Composite Pattern

![](../../../assets/images/2021-09-05-14-36-10.png)

: 단일 객체든, 객체들의 집합이든 같은 방법으로 취급하는 경우에 사용.  
e.g. 파일은 단일 객체, 폴더는 객체들의 집합이지만, 폴더 내에 폴더가 있을 수 있듯이 File System 관점에서는 둘의 차이가 없다.

즉, 객체들 간에 계급 및 계층구조가 있어서, 이를 표현해야 할 때.  
혹은, 클라이언트가 단일 객체와 집합 객체를 구분하지 않고 동일한 형태로 사용하고자 할 때.

## 장점
* 객체들이 모두 같은 타입으로 취급되기 때문에, 새로운 클래스를 추가하기에 용이하다.

`Component.java`
```java
public interface Component {
    String getName();
}
```

`File.java`
```java
public class File implements Component {

    private String name;

    public File(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return name;
    }
}
```

`Directory.java`
```java
public class Directory implements Component {

    private String name;
    private List<Component> components = new ArrayList<>();

    public Directory(String name) {
        this.name = name;
    }

    public void add(Component component) {
        components.add(component);
    }

    public Component get(int index) {
        return components.get(index);
    }

    public void recursivePrint(int depth) {
        String prefix = "-".repeat(depth + 1) + " ";

        if (depth == 0) System.out.println(this.getName());
        for (Component component : components) {
            System.out.println(prefix + component.getName());
            if (component instanceof Directory)
                ((Directory) component).recursivePrint(depth + 1);
        }
    }

    @Override
    public String getName() {
        return name;
    }
}
```

`Client.java`
```java
public class Client {
    public static void main(String[] args) {
        File file = new File("file_1");
        Directory dir_1 = new Directory("myFolder");
        dir_1.add(file);
        Directory dir_2 = new Directory("myFolder2");
        dir_2.add(new File("file_2"));
        dir_1.add(dir_2);
        dir_1.add(new File("file_3"));

        dir_1.recursivePrint(0);
    }
}
```

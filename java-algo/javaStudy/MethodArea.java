/**
 * MethodArea
 */

 // method area
 // 1. field info => 멤버변수 info, String 데이터타입, 접근제어자 private
 // 2. method info => 메서드 이름 main, return type (void), String []args 함수의 매개변수, 접근제어자 public
 // 3. type info => class인지 interface인지에 대한 정보를 저장해즉 MethodArea가 class 인지 interface인지의 대한 정보를 Type info 에다가 저장한다고 볼 수 있음.

 // 그래서 JvM의 Runtime Data Area의 Method Area는 JVM시작시 공간을 할당 받게 되고, 
 // 프로그램의 종료시까지 유지가 되어짐.

 // Method Area에는 Runtime Constant pool이라는게 존재하는데
 // MethodArea에 같이 존재하지만, 사실상 별개의 영역이다.
 // 각 클래스 또는 인터페이스마다 constant pool 테이블이 존재한다.
 // 클래스 생성할때 참조해야 할 정보들을 상수로 가지고 있는 영역이다.
 // JVM은 이 Constant pool을 통해 해당 메서드나, 필드에 있는 실제 메모리 상 주소를 찾아서 참조한다.

 // Heap Area
 // 힙 영역도 마찬가지로 MethodArea처럼 모든 쓰레드에서 공유되는 영역인데

 // 마찬가지로 데이터를 저장하기 위한 영역이며, 런타임시, 동적으로 할당하여 사용하는 영역이다.
 // 즉 Reference type이 저장되는 공간인데, new 연산자로 클래스의 인스턴스를 생성한다던지, 인스턴스 변수를 저장한다던지
 // 배열의 타입을 저장한다던지 이러한 참조형 타입들을 저장하는 공간이라고 보면된다.

 // 당연히 MethodArea 영역에 저장된 클래스만이 생성이 되어 적재된다.
 // 객체가 더 이상 사용되지 않거나, 명시적으로 null을 선언하게되면 GC의 대상이되어 메모리를 회수하게 된다.

 // 힙 영역에 생성된 객체와 배열은,레퍼런스 타입으로서, JVM의 스택영역이나 다른 객체의 필드에서 참조된다는 점이다.
 // 즉 힙의 주소는 스택이 갖고 있고, 스택이 갖고 있는게 힙의 주소이므로, 그 주소를 따라가서 값을 가지고 오는 형태다.
public class MethodArea {
    private String info = " sd";

    public static void main(String[] args) {
        Person p = new Person ();
        // new 연산자를 통해서 Person이라는 class가 reference type이기 때문에
        // Heap 영역에 저장이되게 되는데 new Perosn() 에 대한 정보를 Heap에다가 저장을 하고
        // 그에 대한 참조는 Stack에다가 저장을하게 되낟.
        // main메서드가 실행되면 thread가 시작되게 되면
        // 메소드에 필요한 정보들을 이런식으로 저장을 한다느것.
    }
}
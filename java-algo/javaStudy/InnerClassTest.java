/**
 * InnerClassTest
 */
class Outer {
	// static variable
	static String value = "> Outer class static variable";

	// static final variable
	static final String value2 = "> Outer class static final variable";

	// constructor
	Outer() {}

	// static method
	static void getInstance(){
        System.out.println("> Outer class static method");
    }

	// inner class
	class Inner {
		Inner() {
            System.out.println("Inner class Constructor");
        }
	}

	// static inner class 
	static class StaticInner{
		static String value = "> static variable of StaticInner";
		static final String value2 = "> static final variable of StaticInner";
	}
}

// 이 상태로 main함수를 디버깅하게 되면
// InnerClassTest만 Complier에 의해 compile된 InnerClassTest.class 바이트 코드를
// JVM 로더에 의해서, 동적으로 .class파일을 가지고 가게 되며, 
// JVM의 메모리 영역인 Runtime Data Areas영역에 저장하게 된다.
// 이때 Load, Linking, Initialization 과정을 거치게 된다.

// Load 같은 경우, JVM 메모리 영역에 적제하는 것을 의미하는데 
// JVM 로더는 의미 없이, .class 파일을 메모리에 적제하지 않는다.
// 그렇다는 것은, .class파일의 사용 필요성이 존재할때, 클래스와 static 변수들을
// runtime data areas영역에 저장한다는 것이다.
// 이래서 동적으로 관리한다라고 한다.

// 아래와 같이 main 메서드만 실행하게 되면, main method실행으로 인해서 Inner classTest 클래스가 로드되어야 할 필요성이 생기게 되고
// JVM은 이때 InnerClassTest class를 JVM에 로드하게 된다.

// 이때 위 OuterClass에 static 변수가 존재한다고 하여도, JVM의 RunTime Data Areas영역에 OuterClass와 static 변수를 저장하지 않는다.
// 이 처럼 JVM 로더가 필요에 의해서 InerrClassTest만 필요로 되어지는 것을 알게 되고, InnerClassTest만 JVM로더가 Runtime Data Areas에 적제 하는 것이다.

public class InnerClassTest {

    public static void main(String[] args) {
		// Outer 클래스를 로드한다.
		// Outer 클래스의 인스턴스를 생성한다는 것은, 해당 클래스의 인스턴스를 메모리에 적제하겠다는 의미가 된다.
		// 따라서 인스턴스가 생성되면 메모리에 올라간다라고 하는것은 JVM 로더에 의해서 Outer 클래스의 필요성을 인식하게 되었고
		// 그로 인해 Loading 단계에서, 메모리에 로드가 된다는 것이다.
        new Outer();

		// Outer 클래스가 만약 인스턴스화 하지 않았다면
		// 클래스가 메모리에 적제 되기 위해서 반드시 new 키워드를 사용해서 클래스의 인스턴스를 생성해야 하는 것은 아니다.
		// 메모리에 적제 시키고자 하는 클래스의 static 변수를 호출하는 것으로도, 클래스가 메모리에 적제 될 수 있다.
		// 따라서 JVM Runtime Data Areas 메모리 영역에 해당 클래스가 적제되기 위해서는, 두 가지 방법이 있다.
		// 1. Class를 instance화 시킨다
		// 2. Class의 static 변수를 호출한다.
		System.out.println(Outer.value);

		// 하지만 static final은 다르다.
		// 왜냐하면 final은 상수를 의미하기 때문에, JVM의 Method Area에 Constant Pool에 따로 저장한다.
		// 그러므로 OuterClass를 메모리에 적제시키지 않는다.
		System.out.println(Outer.value2);
		
		// static method를 호출하는 것도 static 변수를 호출하는 것과 마찬가지로, 클래스가 JVM 메모리 영역에 적제 된다.
		Outer.getInstance();

		// 그렇다면 내부에 있는 Inner class를 호출하기 위해서는 어떻게 해야할까
		// Inner Class를 호출하기 위해서는 외부 클래스를 먼저 생성한 다음에
		// 내부 클래스를 생성한다.
		// 따라서 아래와 같은 코드가 성립한다.
		// 먼저 Outer() 클래스의 인스턴스를 만든다음(외부), 내부에 있는 Inner class를 인스턴스화 한다.
		// 이렇게 하게 되면, Outer()클래스와 Inner() 클래스 둘 다 로드되게 된다.
		// 이렇게 사용하게 되면, 메모리 누수가 발생된다.
		new Outer().new Inner();
		
		// static inner 클래스는 단순 inner class와는 다르게, 외부 클래스의 생성 없이
		// 바로 인스턴스화가 가능하다.
		// 따라서, 단순 inner class와의 차이점은, static이 붙어 있느냐의 차이보다, 물론 그 차이도 있지만
		// 외부클래스를 생성해야 하는지 하지 않아도 되는지의 차이점이 존재한다.

		// 이런식으로 static inner class는 Outer()인 외부 클래스를 생성하지 않더라도, 직접 인스턴스화가 가능하다.
		new Outer.StaticInner();
		// 마찬가지로 static inner 클래스의 static 변수를 참조하게 되면, 이런식으로, Outer 클래스는 로드되지 않고
		// static 변수를 참조하여 클래스를 메모리에 올린 것 처럼, 마찬가지로 StaticInner가 메모리에 로드되게 된다.
		// 단 마찬가지로 StaticInner의 static final을 사용한다고 해서, StaticInner가 메모리에 로드 되지 않는다.
		// -> JVM의 MethodArea의 Constant Pool에서 관리하고 있기 때문이다.
		System.out.println(Outer.StaticInner.value);
    }
}
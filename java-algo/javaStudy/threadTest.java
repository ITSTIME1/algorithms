/**
 * threadTest
 */

 // 확인해볼 테스트 사항은
 // Thread class를 확장했을때는 run메소드를 강제적으로 구현하라고 하는지를 테스트해보자.
 // 아 이건 뭐 안봐도 알겠네
 // Runnable이 interface인데, interface는 추상메서드를 가지고 있기 때문에
 // 구현하는 클래스에서 반드시 추상메서드를 구현해야 함.
 // 근데 Thread는 interface가 아닌 class이고, Runnable interface를 구현하고 있는상태.
 // 그래서 추상메서드인run()을 강제적으로 구현하고 있고
 // ThreadTest_1이 Thread클래스를 상속했을때, 강제적으로 구현할 필요가 없다는 것은 곧
 // 이미 Thread에서 구현된 것을, Override하는 것이기 때문에
 // 다형성 개념이 적용됨. 따라서 추상메서드가 아니므로, run()을 강제적으로 구현할 필요가 없는것.

 // 그래서 만약 runnable interface를 직접 implements해서 구현하게 된다면
 // 결국, 추상 메서드의 강제구현이 되는것.
 // Thread 클래스에서는 run()메서드 내부 구현을 target의 설정 여부에 따라서
 // run()메서드를 실행함.
 // 그렇다는것은, target이 설정이 되어 있다면, override된 Run()메서드를 실행시킬테지만
 // 만약 설정되어 있지 않다면, 아무것도 하지 않게됨.
 // 하지만 run()을 구현해두고 부모 run()을 다시 호출하게 되면
 // 무한루프빠질거같은데.


 // Thread는 그리고 실행순서를 보장하지 않아. OS에 의존적임.
 // 실행순서가 보장이 안되는 이유는 Thread Scheduler 때문임.
 // run()메서드를 직접 호출하는것은 멀티쓰레드 시나리오가 아니다.

 // 즉 run()메서드를 호출하게 되는것은 single-thread가 된다는 것인데 왜?
 // 결과만 놓고 보면 start()메서드는 사실상, new thread를 만든다.
 // 그래서 start()메서드로 인해 생성된 새로운 쓰레드가 run()메서드를 실행시킨다.
 // 그래서 run()메서드로 directly하게 실행하게 되면 새로운 쓰레드가 만들어지지 않으므로
 // 그냥 run()메서드가 실행되는 꼴이다.
class ThreadTest_1 extends Thread{

    
}

class ThreadTest_2 implements Runnable{
    
}

public class threadTest {

    public static void main(String[] args) {
        
    }
}
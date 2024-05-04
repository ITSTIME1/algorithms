// 만약 기말고사, 중간고사 라는 시험이 존재한다고 하자.

// 그럼 이 두가지 객체에 대한 공통점은 시험이라는 것에 있다.

// 중간고사와 기말고사 모두 국,영,수,사,과에 대한 시험을 보게 되고
// 두 시험에서 모두 점수의 합계를 계산한다.

// 그렇다면, 두 시험이 모두 공통된 값을 가지고 있다면
// RunTimeDataArea의 메모리 영역에 저장되는 내용들이 중복된 데이터들이 많아지게 되고
// 즉, 클래스의 개수가 N개라고 하자.
// 그러면 클래스의 개수가 6개 라고 한다면 6개 클래스 모두에게 공통된 속성값이 존재한다면
// 메모리가 한개짜리가 6개 있는 셈이되고 그러면 6배 많은 메모리를 사용하게 된다.
// 그렇기 때문에 이를 해결하기 위해 클래스 개수는 6개지만, 공통된 영역은 1개로 만들어버리는것이다.
// 1/6로 만들어서 1/6에 해당하는 것만 다른 클래스에 확장시켜서 사용한다는 것이다.
// 그렇다면, 클래스의 공통부분의 개수가 N이라고 가정하게 되었을때, 1/N로 메모리를 확보할 수 있게 된다.
// 즉 클래스의 개수 N * 공통된 부분의 개수 M / M
// M(((N * M) / N)) 이만큼의 메모리를 확보할 수 있게 된다.
// 따라서, 이러한 메모리 확보를 하기 위해 두 시험에 대한 추상화인 '시험' 이라는 추상화 레벨을 도입시킬 수 있다.

// 그럼 각 시험에서 공통된 부분을 뽑아내면 아래와 같은 코드를 만들 수 있다.
// 시험은 세개만 본다고 가정하자. 이런식으로 추상클래스를 작성하게 되면
// 중간고사와 기말고사 이외에 어떤 시험 종류가 추가 된다면
// 그 시험에 대한 부분도 공통된 부분을 따를 수 있다. 즉 메모리를 
// abstract class Exam {
//     int kor;
//     int eng;
//     int math;

//     // 추상클래스 같은 경우 추상메소드로 작성한다.
//     // 인터페이스는, static final 상수밖에 사용하지 못하는데
//     // 추상클래스 같은 경우, static final말고도 일반적인 데이터 타입의 필드들을 정의할 수 있다.
//     // 단 추상클래스와 인터페이스 모두 인스턴스 생성이 불가능하다.
//     // 만약 상수필드가 공통된다면 추상클래스가 아닌, 공통된 기능의 분류로 보아 인터페이스로 설계가 가능할것같다.
//     abstract void total();
//     abstract void avg();
// }

// 즉 추상클래스는 부모-자식 간의 의미적으로 연관이 되어 있다.
// 즉 확장성이 필요하다. 라는 말을 잘 생각해보면, 논리적으로 관련이 있는부분들을 확장하고, 확장하는 부분에 대해서
// 강제성이 필요하며, 부모의 확장이 필요한 부분을 다형성을 이용해서 구현한다는 측면에서
// 의미가 있다고 볼 수 있다.

// class NewLecExam extends Exam {}

// class LastExam extends Exam {}

// 조금더 논리적으로 접근해보자.
// 만약 내가 SNS Sender를 구현한다고 해보자.
// 근데 통신사들마다, 통신탑이 다르기 때문에
// 통신에 필요한 구현들은 통신사들 마다 다르게 구현해야 하는 상황이다.
// 그러면 우리는 총 3개의 통신사가 있다가정하자 SKT, KT, LG
// 즉 이런 통신사들이 각자 통신매커니즘을 구현해야 한다고 가정하자.
// 이 통신사들이 구현해야 하는것은, 자신의 통신사에 맞게, 통신매커니즘을 구현하는 것이다.
// 그러므로, 그 통신 매커니즘을 설계할 공통 메서드를 중복작성하지 않도록
// 공통 분모로 추출할 수 있을것이다.
// 또한 공통 필드들도 공통 분모로 추출할 수 있을것이다.
// 이렇게 하면 위에서 계산했던 것과 같이 Method Area영역에, 중복된 값들을 저장할 필요가 없기 때문에
// 메모리 측면에서 효율적이라고 볼 수 있다.


// 그럼 이를 구현하기 위해 무엇을 해야할지 살펴보자.

// 먼저 모든 통신사들의 추상화 단계인, SMSSender를 만들자.
// 그리고 그 SMSSender가 제공해주는게 무엇일지 생각해보자.
// 먼저 각 통신사들한테 공통적으로 제공해주어야 하는 메소드가 있을것이다.
// 또 공통적으로 사용되어야 하는 멤버들도 포함하고 있을것이다.

// 따라서 이런 부분들을 공통 분모로 추출해 작성해준다.






// 추상클래스에서 접근제어자에 대한 제한은 없다.
// abstract method는 private가 아닌 public or protected중에 하나를 선택해야한다.
// protected는 같은 패키지에서, 그리고 상속받은 클래스 내에서만 사용할 수 있다.

// 추상 메서드는 body를 가질 수 없기 때문에, 3사 모두 공통적으로 동작할 수 있는 코드라면
// 일반 메서드를 추상클래스에서도 작성할 수 있기 때문에, 일반 메서드로 작성한다.
// 마찬가지로, 해당 메서드가 같은 패키지 내에서 접근을 가능하게 할 것인지, 아니면 다른 클래스에서도 사용이 가능하게 할 것인지 정한다.
// sendSMS 같은 경우 외부에서 실행을 시켜야 하므로, 상속받은 클래스 내 뿐만 아닌 외부에서도 사용하기 위해 public으로 접근을 지정한다.
// 또한 sendSMS같은 경우는, 3사가 각 회사에 맞게 연결메서드를 구현한 것을 모두 실행시킨다고 가정하자.
// 추상클래스는 또한 static final 상수 이외에도 일반 필드 사용이 가능하다.
// 만약 특정 값이 모두 공통 상수로 바라볼 수 있다면, enum을 활용하자.
// enum 매핑 클래스

import java.util.ArrayList;
import java.util.List;

enum Connection {
    TIME(1, true),
    DELAY(2, false);

    private int time;
    private int delay;

    private Connection(int time, boolean check) {
        if (check) {
            this.time = time;   
        }  
        this.delay = time;
    }

    public int getTime() {
        return time;
    }

    public int getDelay() {
    
        return delay;
    }
}
// enum의 TIME이 하나의 객체기 때문에 힙 영역에 저장되고
// 생성자를 통해서, 싱글톤으로 해당 값을 초기화 시키며, 
// enum에 매핑된 값이 생성자를 통해서 할당이 되어진다.

// 사실 enum은 시스템 레벨에서 상수기 때문에 해당 SMS Sender 값만을 위한 상수를 정의하자면 저렇게 될거고
// enum에 목적에 따라 정의가 달라질 수 있다.
// 따라서 SMSSender를 위해 필요한 공통 상수들을 enum으로 구현한다.
// 이렇게 하면, 추상클래스를 상속받게 되는 SKT, KT, LG가 부모 클래스에 있는 필드들을 상속받지 않더라도
// 시스템 레벨에서 조율이 가능하다.

// 그럼 추상클래스는 이렇게 논리적인 관계에서 사용하면 될 것 같은데
// 인터페이스는 어떻게 사용할 수 있을까
// 인터페이스는 논리적인 관계가 아닌 것들의 형제정도로 묶어버릴 수 있다고 보면 된다.
// 또 추상클래스에 선언된 추상메서드 같은 경우 메서드의 구현을 강제하게 되므로
// 추상 클래스를 상속하게 되는 자식에서, 해당 메서드에 해당되지 않음에도 불구하고
// 추상 클래스의 특징으로 인해 강제 구현이 된다는 점이다.
// 그렇다면, 그렇게 구현된 메서드는 MethodArea에 메모리를 잡아먹게 되므로, 그리 좋지 않다.
// 해당 클래스 의도에 맞지 않을 뿐더러, 실질적으로 필요가 없는 메서드를 구현하는게 옳지 않기 때문이다.
// 이러한 경우 강제구현성에서 자유롭게 구현할 수 있는 메서드들을 만들 수 있을것이다.
// 즉 이 메서드에 해당되는 클래스들에게만, 이 메서드를 구현할 수 있게끔 말이다.
// 인터페이스도 마찬가지로, 추상 메서드를 가지고 있기 때문에, 강제로 메서드를 구현해야 한다는 것은 동일하나
// 의미 없는 클래스에서 구현하지 않아도 되기 때문에, 해당되는 클래스에만 구현시킬 수 있다는 장점이 존재한다.
abstract class SMSSender {

    abstract protected void establishConnection();
    public void sendSMS(int time, int delay) {
        establishConnection();
    }
    
}
/**
 * abstractStudy
 */

 // 이런 식으로 각 회사에 맞는 연결 메서드를 구현하게 한다.
 // 오버라이드를 하기 때문에, 각 자식 클래스에서 snedSMS를 호출하게 되면
 // @Override 했기 때문에, 오버라이드 된 메서드가 실행된다.
 // 그러므로 establishConnection이 sendSMS상에서 호출된다고 보면 된다.


 // INTERFACE같은경우 변수는 static final이 고정으로 적용되기 때문에
 // 상수이며 초기화가 필요하다.
interface ConnectionModule {
    List<Double> perCount = new ArrayList<>(); 
    void cancelConnectionForTwoMinute();
}


// SMSSender에 perCount와 cacelConnection을 구현하게 되면
// 두 변수와 메서드다 필요한 클래스들에게만 구현하게 하면 되기 때문에
// SMSSender를 상속하고 있는 모든 통신사 클래스들에게 구현하게 하는 것은 옳지 않다.(SKT, KT)만 구현할 필요성이 있다한다면

// 결국 클래스들의 공통 분모는, abstract로 추출하며,
// 공통 분모에서 구현될 필요성이 없는 것들 즉 추상화 된 자식클래스들에 대해서
// 강제할 필요가 없는데, 강제하게 되는 것들인 경우는 interface에 정의한다고 보면 된다.
 class SKT extends SMSSender implements ConnectionModule{
    // 이런식으로 SKT에는 cacelConnectionForTwo라는 메서드가 필요하기 때문에
    // 이런식으로 구현이 가능하다.
    @Override
    public void cancelConnectionForTwoMinute() {
        System.out.println();
    }

    @Override
    protected void establishConnection() {}
 }

 class KT extends SMSSender implements ConnectionModule{
    
    @Override
    public void cancelConnectionForTwoMinute() {
        // TODO Auto-generated method stub
        
    }

    @Override
    protected void establishConnection() {
        System.out.println("hh");
    }
 }

 class LG extends SMSSender{
    @Override
    protected void establishConnection() {}
 }


public class abstractStudy {
    // enum에 정의된 값을 가지고 와서
    // int 필드를 정의해버리면 또 메모리가 부여되게 되는거니까
    public static void main(String[] args) {
        // SKT skt = new SKT();
        // Connection time = Connection.TIME;
        // Connection delay = Connection.DELAY;

        // skt.sendSMS(time.getTime(), delay.getDelay());

        KT kt = new KT();
        // kt.sendSMS(time.getTime(), delay.getDelay());
        // 같은 패키지 내에서만 사용이 가능하도록 제한한다.
        kt.establishConnection();
    }
}


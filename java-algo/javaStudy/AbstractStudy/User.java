package AbstractStudy;

/**
 * User
 * 
 * 유저의 조건을 생각해보자. UserEntitiy로써 기능을 하기 때문에 
 * 먼저, 유저는 디비에 저장될 ID가 필요로 할 것이고, 아래와 같이 유저에게 필요한 필드들을 정의할 수 있다.
 * id, name, level, loginCount, recommend
 * 
 * 그럼 기본적으로 user가 가지고 있어야 할 정보는 아래로 정의된다.
 */
// @Getter
// @Setter
public class User {
    private Long id;
    private String name;
    private String level;
    private int recommend;
}

/**
 * Level은 총 세가지 종류가 있다.
 * basic, silver, gold
 * 그러면, 이걸, 하나의 열거형태로 만들 수 있지.
 * Q. 그럼 이제 열거형을 왜 써야 하는가로 이야기가 흘러갈 수 있음.
 * 
 */
enum Level {
    // 열거 객체가 가지는 값은 다음 레벨
    GOLD(3, null),
    SILVER(2, GOLD),
    BASIC(1, SILVER);


    // 이건 열거형들을 받아줄 변수들.
    private final int value;
    private final Level nextLevel;

    Level(int value, Level next ) {
        this.value = value;
        this.nextLevel = next;
    }

    public int getValue() {
        return this.value;
    }

    public Level getNextLevel() {
        return this.nextLevel;
    }
}


/*
 * UserService는 어찌 되었든, user와 관련된 비즈니스 로직을 수행해야 하자나.
 * 그럼 공통적인 함수들을 abstract로 구현하게 하면 되지 않을까, interface와 abstract
 * 결국 어떤 특정 공통 추상화를 하려면 abstraction을 이용해서, 이걸 강제로 구현하게 하고
 * 나중에 UserService가 구현할 필요성이 존재하지만, 다른 서비스에서도 공통으로 쓸 수 있는 규격이라면 interface로 만드는게 맞지 않을까
 * 근데 또 생각해보면, interface를 구현해서, UserService에게 맞는 구현체를 구현하게 하는것도 맞는것 같기도 하고
 * 
 * 
 * 그럼 abstract를 사용하기 위해서 고려해야 할 부분을 생각해봐야겠지.
 * 그리고 interface를 사용하기 위해서 고려해야 할 부분을 생각해봐야겠지.
 * 
 * 1. 추상클래스를 사용하려고 한다면, 공통된 기능을 구현할 필요가 있는가.
 * 지금같은 상황에서는. UserService하나 밖에 없지만, 만약 다른 서비스들도 함께 있다면
 * 그리고 그런 여러 service들이 공통적으로 구현될 만한 내용이 존재한다면 추상클래스로 공통된 부분을 구현할 수 있다.
 * 그리고 추상클래스 내에서 구현한 내용을 사용할 수도 있고, 구현한 상속 클래스 내에서도 사용하게 할 수 있다.
 * 즉, 공통된 사항이 모두 같다면, 그 공통 사항을 구지 서브클래스에서 구현할 필요 없이, 추상클래스 단에서 처리가 가능하다는 것을 의미한다.
 * 왜냐하면, 추상메서드로 만들어서 클래스마다 구현할 바에, 공통된 기능같은 경우는, 여러 클래스에 구현하지 않고, 사용할 수 있기 때문이다.
 * 전제는 역시 모든 service에서 코드하나 틀리지 않은 완벽히 일치된 코드를 추상 클래스에서 작성한다.
 * 
 * 2. 확장성을 고려할 수 있나.
 * 공통된 기능이 여러개 생기게 된다면, 그리고 위에서 추상클래스에서 사용할 메서드들이 더 추가될 수 있다면
 * 당연히 추상클래스를 고려할 수 있다.
 * 
 * 결론, 위 두가지 사항, 여러 서비스 클래스들이, 공통으로 구현할 코드들이 존재하는가.
 * 그리고 그런 코드들중에서 부모클래스 레벨에서 처리할 수 있는 부분이 있는가.
 * 두번째, 확장될 수 있는 코드들이 생길 여지가 존재하는가를 고려할 수 있다.
 * 
 * 
 * 
 */

 /*
  * 그럼 Service가 공통된게 현재 없기 때문에, 이는 interface가 적합.
  interface같은 경우, 만약 extends하고 있는게 있다면 interface를 구현해야 하낟.
  또 각 service가 해당하는 interface를 구현함으로써, 각 클래스의 역할이 명확하게 나눠질 수 있다.
  
  따라서 내가 interface를 선택한 이유는
  1. service 레이어가한개기 때문에, 공통으로 뽑아낼 요소가 존재하지 않는다.
  2. UserService는 해당 클래스가 수행해야 할 목표가 명확하다.
  3. 그렇기 때문에 해당 목표를 수행하기 위한 개별 코드만 추가할 수 있기 때문에 확장성에 용이하다.
  */

interface UserLevelUpdatePolicy{
    boolean canUpgradeLevel(User user);
}

class UserService implements UserLevelUpdatePolicy {

    // 이런식으로 UserService가 고유하게 사용할 기능들은 interface로 관리하게 된다.
    // 만약 필요가 없어지는 기능이라면 interface에서도 삭제할 수 있다.
    // 즉 만약 이 부분이 필요가 없어진다면 부품처럼 관리할 수 있기 때문에
    // 주석으로 관리하거나, 다시 필요가 있다면, 해당 부품을 다시 끼는 형태로 구현이 가능하다.
    @Override
    public boolean canUpgradeLevel(User user) {
        Level currentLevel = user.getLevel();
        
        return false;
    }

    
}
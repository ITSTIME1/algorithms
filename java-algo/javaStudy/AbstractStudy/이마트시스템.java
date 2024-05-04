package AbstractStudy;

import java.util.HashMap;

/**
 * 새할인정책개발
 * 
 * 일단 새 할인 정책을 개발하기 위해서 어떤 것들이 있는지 우선 살펴보자.
 * 
 * 먼저 < 할인 정책 > 을 관리하는 클래스가 필요할 것이다.
 * 이 할인 정책이라고 하는것은, 다양하게 확장될 여지가 있다. 그렇기 때문에
 * 여러 할인 정책으로 나뉠 수 있는 경우들을 고려해서 클래스 확장을 고려한다.
 * ex) 이벤트 할인 정책, 서머즈 할인정책, 이마트 신세계 데이 할인정책 등을 고려해보면
 * 여러 주제들이 존재하고 그 주제에 맞는 정책을 필요로한다.
 * 
 * 
 * 그럼 이 이벤트들이, 공통으로 가지고 있어야 하는게 무엇인지 보자.
 * 
 * 일단 기존에는 기존 할인정책을 고수하고 있었다.
 * 기존 할인정책은 고정 할인율을 적용하고 있다.
 * 그러므로 User의 등급이 무엇이든지, 금액에 따른 고정할인금액만큼만 차감한다.
 * 
 * 그럼 일단 기존에 있던 고정할인은, 할인정책을 할당받게 되고, 할당 받는 메소드를 구현하게 만든다.
 * 공통 메소드는 현재 존재하지 않기 때문에, 만약 차후 통합적으로 개선될 여지가 있다면 abstract로 바꾼다.
 * 
 * 기존 정책을 건드리지 않고도, interface를 확장해서 새로운 정책을 만들어 냈다.
 * 각 할인 서비스마다, 할인을 적용하는 방법을 개별적으로 적용하면 된다.
 * 
 * 일단 유저가 요청을 할것이다. 즉 어떤 금액에 대해서, 해당 금액만큼 구입을 했으니->할인을적용해달라.
 * 
 */


 // Entitiy
class 유저 {
    private String name;
    private String level; // 등급
    private int orderPrice; // 총 주문금액

    public 유저(String level, int price, String name){
        this.name = name;
        this.level = level;
        this.orderPrice = price;
    }

    
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }

    public int getOrderPrice() {
        return orderPrice;
    }

    public void setOrderPrice(int orderPrice) {
        this.orderPrice = orderPrice;
    }


    public String getName() {
        return name;
    }
    
    
}

interface 유저기능{
    void 유저이름설정 (String name);
    void 주문요청(int price);
    void 유저생성();
}

// service
class 유저서비스 implements 유저기능 {

    @Override
    public void 유저이름설정(String name) {
        유저 유저 = new 유저("BASIC", 0, "taesun");
        // 그럼 이제 유저를 생성할거임.
    }

    @Override
    public void 주문요청(int price) {
        
        
    }

    @Override
    public void 유저생성() {
        // 유저를 데이터베이스에 저장하는 것은 repository에서 처리할 거니까
        // 유저를 생성하기 위해선, 유저 레포지토리에서 DB쿼리를 사용해야함.
        this.유저이름설정(null);

    }
    
}

// interface
interface 할인정책 {
    int discount(유저 유저) throws IllegalArgumentException;
}

// service
class 고정형할인서비스 implements 할인정책{
    private final int fixed_discount_rate = 1000;
    @Override
    public int discount(유저 유저) {
        // 주문금액에서 - 1000 뺀 금액만큼만 결제하도록
        // 그럼 이게 최종주문 금액이 되니까
        int result = 유저.getOrderPrice() - fixed_discount_rate;
        return result;
    }
    
}

// service
class 변동형할인서비스 implements 할인정책{
    private final int dynamic_discount_rate = 10;

    @Override
    public int discount(유저 유저){ 

        // 유저의 등급에 따라 할인율이 달라진다.
        // 그래서 유저의 등급이 VIP일 경우에만 변동형할인서비스가 적용됨.
        if(유저.getLevel() == "VIP") {
            int result = 유저.getOrderPrice() * ((100 - dynamic_discount_rate) / 100);
            return result;
        } else {
            // 유저 등급이 VIP가 아닌 사람들 등급중 VIP를 제외한 나머지.
            // 그런 사람들은, 할인이 적용이 안되어야 하니까 예외를 던진다.
            
        }
    }
    
}


public class 이마트시스템 {


    // ioc 
    // di 주입을 받을거임 bean container 로 부터, 객체를 받을건데 service를 처리하면 되니까
    // 주입을 받았다고 치자.
    private static final 유저서비스 유저서비스 = new 유저서비스();
    private static final HashMap<String, 유저> 유저데이터베이스 = new HashMap<>();
    public static void main(String[] args) {
        // 1. 모든 유저들이 존재한다고 하자.
        유저서비스.유저생성();

        // 2. 그럼이제 요청이 들어올 것이다. 즉 유저가 요청을한다.
        // 이마트 pos결제시스템으로부터, 결제가 들어왔다고 가정하자.
        // thread 활용을 통해서, 각기 다른 유저를 처리하기 위해 멀티 프로세싱으로 진행한다.

        // 그러나 톰캣이 멀티프로세싱 작업을 처리하므로
        // 직접구현할 필요가 없나?
        유저서비스.주문요청();

    }    
}
// 그럼 이제 등급에 따라서 변동 할인율이 적용이 되려면
// 그럼 이제 
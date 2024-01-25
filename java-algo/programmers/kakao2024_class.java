package programmers;
import java.util.*;
/**
 * kakao2024_class
 */
// 클래스화를 시켜보자
// 우선 선물과 관련된 기능이다.
// 선물을 주고받은 기록이 있는지, 없는지에 따라서 다음달에 누가 더 많은 선물을 받을지 예측하는 기능을 구현하는 것이다.
// 따라서 가장 추상화 시킬 수 있는 클래스를 만든다면 선물 클래스를 만들 수 있을것 같다.


// 카카오 선물 클래스를 만든다.
// 카카오 선물과 관련된 인터페이스를 만들어준다.
// 선물을 주기 위해서, 선물 주기 메소드를 만들어준다.
interface KakaoGiftInterface {
    // 선물주기
    public void gift_give_to_user();
    
}

// KakaoGiftInterface를 구현해서, 선물하기와 관련된 기능을 제공한다.
// 인터페이스를 만든 이유는 선물하기와 관련된 구현을 강제한다.
// 그리고 다형성을 이용한다. 만약 카카오 선물하기중에서, 이모티콘 선물하기, 상품 선물하기 등 선물을 하는 대상은 다양하다.
// 때문에 클래스를 추상화 시키고, 그 클래스가 구현해야 할 메소드를 인터페이스로부터 구현 받는다.
class KakaoGift implements KakaoGiftInterface{
    @Override
    public void gift_give_to_user(){}
}


// 유저는 각각의 사람을 의미한다.
// 즉 유저들간의 선물을 교환하기 때문에, User객체를 만들어준다.
// 유저 클래스가 가지고 있을 속성은 이름, 내가 준 선물의 개수, 내가 받은 선물의 개수, 선물지수 , 최종적으로 받은 선물의 수
class KakaoFriend {
    public static int FRIENDS_COUNT = 0; // 친구가 몇명인지.
    private String name; // 이 친구의 이름
    private int giveToUser = 0; // 내가 준 선물의 개수
    private int receiveFromUser = 0; // 내가 받은 선물의 개수
    private int giftIndex = 0; // 선물지수
    private int totalGift = 0; // 다음달에 받을 선물의 개수
    private int userNumber; // 유저 넘버
    // constructor
    KakaoFriend(String name, int number) {
        this.name = name;
        this.userNumber = number;
        FRIENDS_COUNT++;


    }

    // getter, setter
    public String getName() {
        return name;
    }
    public int getGiveToUser() {
        return giveToUser;
    }
    public int getReceiveFromUser() {
        return receiveFromUser;
    }
    public int getGiftIndex() {
        return giftIndex;
    }
    public void setGiveToUser(int giveToUser) {
        this.giveToUser = giveToUser;
    }
    public void setReceiveFromUser(int receiveFromUser) {
        this.receiveFromUser = receiveFromUser;
    }
    public void setGiftIndex(int giftIndex) {
        this.giftIndex = giftIndex;
    }

    public int getUserNumber() {
        return userNumber;
    }
   
    public int getTotalGift() {
        return totalGift;
    }

    public void setTotalGift(int totalGift) {
        this.totalGift = totalGift;
    }
    
    
    

}

// 메인에서 돌아가게 만들면 되니까
public class kakao2024_class extends KakaoGift
{  
    

    // 유저 리스트 테이블
    public static List<KakaoFriend> friendsList = new ArrayList<>();
    // 유저 이름
    public static String[] friends_name = {"muzi", "ryan", "frodo", "neo"};
    
    // 유저 로그 기록
    public static String [] log = {"muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"};

    // 관계 표현
    public static List<List<Integer>> logArray = new ArrayList<>();



    // 유저 생성
    public static KakaoFriend createUser(String name, int index) {
        // static method 는 static 메소드와 변수만 참조 할 수 있기 때문에 이런식으로 구현하면 될거 같은데.
        KakaoFriend newUser = new KakaoFriend(name, index);   
        return newUser;
    }

    // 2차원 배열 초기화
    public static void init_report() {
        for (int i = 0; i < KakaoFriend.FRIENDS_COUNT; i++) {
            logArray.add(new ArrayList<>());
            for (int j = 0; j < KakaoFriend.FRIENDS_COUNT; j++) {
                logArray.get(i).add(0);
            }
        }
    }  

    // friends 리스트에 프렌드 객체 생성.
    public static void create_friend() {
        int index = 0;
        for (String name : friends_name) {
            // 유저를 만들어서 그 객체를 hash로 관리하면 되지 않을까
            KakaoFriend createdUser = createUser(name, index);
            friendsList.add(createdUser);
            index++;
        }
    }

    
    // 관계 확인
    public static void check_report_relational(String[] log) {
        for (String logs: log) {
            String[] parts = logs.split(" ");
            String giver = parts[0]; String receiver = parts[1];

            //  1. 주거나 받은 선물의 개수를 업데이트한다.
                // 선물을 준 사람이면 giveToUser를 올리고
                // 선물을 받은 사람이면 receiveFromUser를 올린다.
            // 2. 관계를 표현한다. 서로간의 관계를 나중에 검사하기 위해서 2차원 배열에 주거나 받은 기록이 있다면 표시할것
            // 3. 만약 주거나 받은 기록이 없으면 결국 0으로 되어 있음.
            for (KakaoFriend user : friendsList) {
                int giverNumber = -1;
                int receiverNumber = -1;
                if(user.getName().equals(giver)) {
                    user.setGiveToUser(user.getGiveToUser() + 1);
                    giverNumber = user.getUserNumber();
                } else if(user.getName().equals(receiver)) {
                    user.setReceiveFromUser(user.getReceiveFromUser() + 1);
                    receiverNumber = user.getReceiveFromUser();
                }
                

                // 만약 giverNumber 이 -1이 아니고 receiverNumber가 -1 아니라면, 관계를 설정하는것.
                if(giverNumber != -1 && receiverNumber != -1) {
                    logArray.get(giverNumber).set(receiverNumber, user.getGiveToUser());  
                }
            }
        }
    }
    // 조건 검사
    // 다형성을 이용해서 선물 주기를 구현

    // 인터페이스는 메소드를 강제하기 때문에, 선물이 이모티콘 선물일 경우에도 필요없는 메소드를 전부 구현해야 하므로
    // 선물이라는 클래스를 상속받고, 선물이 가지고 있는 메소드를 재구현한다.
    @Override
    public void gift_give_to_user() {  
        for (int i = 0; i < KakaoFriend.FRIENDS_COUNT; i++) {
            for (int j = 0; j < KakaoFriend.FRIENDS_COUNT; j++) {
                if(i != j) {
                    if((logArray.get(i).get(j) == 0 && logArray.get(j).get(i) == 0) || logArray.get(i).get(j) == logArray.get(j).get(i)){

                    } else if (logArray.get(i).get(j) != 0 || logArray.get(j).get(i) != 0) {
                        // 둘중에 하나라도 0이 아니라면 기록이 있는거니까
                        // 그러면 기록이 있으니까
                        // 둘 중에 준 선물의 개수가 큰걸 살펴보자.
                        // if(userTable.get(i).getGiveToUser() > userTable.get(j).getGiveToUser()) {
                        //     // 한번만 실행하자. 이것때문에 한번만 실행하는거니까
                        //     // 어짜피 둘다 처리하지 않고 한번만 처리할 것이기 때문에
                        //     // 이전에 있던건 살펴보지 않아도 될거 같은데
                        
                        // } 
                    }
                }
                
            }
        }
    }


    

    public static void main(String[] args) {   
        
        create_friend();
        init_report();
        check_report_relational(log);
        // 조건 게산하기만 하면됨.

    }
}
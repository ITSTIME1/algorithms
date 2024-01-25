package programmers;
import java.util.*;

class kakao2014 {
    public int solution(String[] friends, String[] gifts) {
        List<String> friendsList = new ArrayList<>(Arrays.asList(friends));
        int answer = 0;
        
        HashMap<String, List<Integer>> productTable = new HashMap<>();  // 선물 관리.
        
        int length = friends.length; // 길이.
        int[][] productCount = new int[length][length]; // 2차원 배열 누가 누구에게 주었는지.
        // 배열을 0으로 초기화.
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                productCount[i][j] = 0;
            }
        }
        
        for(String user : friends) {
            List<Integer> defaultValues = new ArrayList<>(Arrays.asList(0, 0, 0, 0)); // 준 선물개수, 받은 선물 개수, 선물지수, 최종적으로 받은 선물의 수
            productTable.put(user, defaultValues);
            
        }
        for (String logs : gifts) {
            String[] parts = logs.split(" ");
            String giver = parts[0];
            String receiver = parts[1];
            
            List<Integer> giverInfo = productTable.get(giver);
            List<Integer> receiverInfo = productTable.get(receiver);
            giverInfo.set(0, giverInfo.get(0) + 1); // 준 선물 업데이트
            receiverInfo.set(1, receiverInfo.get(1) + 1); // 받은 선물 업데이트
            
            int giverIndex = friendsList.indexOf(giver);
            int receiverIndex = friendsList.indexOf(receiver);
            productCount[giverIndex][receiverIndex]++;

        }


        // 선물 지수를 계산하자.
        
        // 이제 선물지수를 계산한다.
        for(String user : productTable.keySet()) {
            List<Integer> userInfo = productTable.get(user);
            int giveValue = userInfo.get(0);
            int receiveValue = userInfo.get(1);
            userInfo.set(2, giveValue - receiveValue); // 선물 지수를 계산.
        }
        
        // 이제 누가 더 많이 받았는지를 계산하자.
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length; j++) {
                if(i != j) {

                    List<Integer> giftIndexValue1 = productTable.get(friends[i]);
                    List<Integer> giftIndexValue2 = productTable.get(friends[j]);
                    
                    // 선물 기록이 없거나, 같다면
                    if((productCount[i][j] == 0 && productCount[j][i] == 0) || (productCount[i][j] == productCount[j][i])) {
                        if(giftIndexValue1.get(2) > giftIndexValue2.get(2)) {
                            giftIndexValue1.set(3, giftIndexValue1.get(3) + 1);    
                        }
                        
                        
                    } else if(productCount[i][j] != 0 || productCount[j][i] != 0) {
                        // 선물 기록이 있다면, 서로간의 준 선물의 개수로 비교하는거지
                        if(productCount[i][j] > productCount[j][i]) {
                            giftIndexValue1.set(3, giftIndexValue1.get(3) + 1);
                        }
                    }
                }
            }
        }
        
        
        // for (String user : friends) {
        //     List<Integer> test = productTable.get(user);
        //     System.out.println(test.toString());
        // }
        
        for(String user : productTable.keySet()) {
            List<Integer> userInfo = productTable.get(user);
            int giveValue = userInfo.get(3);
            if(answer < giveValue) {
                answer = giveValue;
            }
            
        }
        return answer;
    }
}
        
        
        
        
        

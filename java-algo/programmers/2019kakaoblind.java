import java.util.*;
// O(N * M + nlogn + N)

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        // 스테이지 번호 : 실패율
        HashMap<Integer, Double> dic = new HashMap<>();
        // 스테이지는 1~N까지 
        for (int stage = 1; stage <= N; stage++) {
            int total = 0;
            // 스테이지 번호를 하나씩 가지고 와서, 현재 스테이지 번호 + 스테이지 번호보다 큰 사람들을 count로 센다.        
            int count = 0;
            for (int num : stages) {
                if (num >= stage) {
                    total++;
                }
                if (num == stage) count++;
            }
                
            // 스테이지에 도달한 유저가 없는 경우 스테이지의 실패율은 0으로 정의한다.
            // 이게 없다면?
            // 스테이지에 도달한 유저가 없다면 count = 0, total 0 or total 0이상.
            // count == 0 and total == 0 스테이지에 도전중인 사람도 없고, 스테이지를 클리한 사람 + 도전중인 사람도 없고 (스테이지에 도달하지 못한사람들) ex) stage = 3[1,1,1,1]
            // count == 0 and total >= 0 ex) stage = 3, [3,1,1,1]
            // 1번 경우를 체크하지 못하기 때문에, 0,0인 경우를 0으로 정의하는것.
            
            
            if(count == 0) {
                dic.put(stage, 0.0);
            } else {
                // 실패율을 저장해준다.
                dic.put(stage, (double) count / total);    
            }
            
        }
        
        // 이제 스테이지에서 value가 가장 높은 값으로 정렬을 해주어야 하는데.
        List<Map.Entry<Integer, Double>> list = new ArrayList<>(dic.entrySet());
        // Comparator를 직접구현.
        Collections.sort(list, new Comparator<Map.Entry<Integer, Double>> () {
            public int compare(Map.Entry<Integer, Double> o1, Map.Entry<Integer, Double> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }
        });
            
        int index = 0;
        for (Map.Entry<Integer, Double> entry : list) {
            answer[index++] = entry.getKey();
        }
        
        return answer;
    }
}
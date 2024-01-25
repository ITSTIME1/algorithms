package programmers;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * SumOfSequenceTwoPointerOptimize
 */
public class SumOfSequenceTwoPointerOptimize {
    public static final int[] sequence = {1, 2, 3, 4, 5};
    public static final int k = 7;
    public static int[] main(String[] args) {
        int start = 0;
        int end = 0;
        // 시작 인덱스 : [길이, 마지막 인덱스]
        HashMap<Integer, List<Integer>> table = new HashMap<>();
        int currentSum = sequence[0];
        // start == end
        while (start <= end && end < sequence.length) {
            if (currentSum == k) {
                if(!table.containsKey(start)) {
                    List<Integer> array = new ArrayList<>();
                    array.add(end - start + 1); // len
                    array.add(end); // last index
                    table.put(start, array);
                }
                // 아 그냥 start만 증가시키면 더해진 값은 그대로니까.
                currentSum -= sequence[start++];
            } else {
                // 큰 경우
                if(currentSum > k) {
                    while(currentSum > k) {
                        currentSum -= sequence[start++];    
                    }
                } else {
                    if(end + 1 < sequence.length) {
                        end++;    
                        currentSum += sequence[end];
                    } else {
                        break;
                    }
                }
                
            }
        }

        // 최소 길이를 찾기 위한 변수
        int minLen = Integer.MAX_VALUE;
        // 정답 배열 초기화
        int[] answer = new int[2];

        // 테이블을 순회하면서 최소 길이를 가진 부분 수열 찾기
        for (Map.Entry<Integer, List<Integer>> entry : table.entrySet()) {
            // 각 부분수열의 길이를 가지고온다.
            int currentLen = entry.getValue().get(0);
            // 각 부분수열의 키 값임 (시작인덱스)
            int currentStart = entry.getKey();

            if (currentLen < minLen || (currentLen == minLen && currentStart < answer[0])) {
                minLen = currentLen;
                answer[0] = currentStart;
                answer[1] = entry.getValue().get(1);
            }
        }

        return answer;
    }
    
}
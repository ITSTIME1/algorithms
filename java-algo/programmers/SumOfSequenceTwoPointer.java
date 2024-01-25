package programmers;
import java.util.*;
/**
 * SumOfSequenceTwoPointer
 */
public class SumOfSequenceTwoPointer {
    public static final int[] sequence = {1, 2, 3, 4, 5};
    public static final int k = 7;
    public static int[] main(String[] args) {
        int start = 0;
        int end = 0;
        // 시작 인덱스 : [길이, 마지막 인덱스]
        HashMap<Integer, List<Integer>> table = new HashMap<>();
    
        // start == end
        while (start <= end && end < sequence.length) {
            // end까지를 포함해서 부분 수열의 합을 계산
            int value = 0;
            int len = 0;

            for (int i = start; i < end + 1; i++) {
                value += sequence[i];
                len++;
            }
            // 합이 k랑 같다면,
            if (value == k) {
                // 테이블에 키가 없다면
                if (!table.containsKey(start)) {
                    // 테이블에 추가하는데, 길이와 마지막 인덱스를 추가.
                    List<Integer> entry = new ArrayList<>();
                    entry.add(len);
                    entry.add(end);
                    table.put(start, entry);
                    start++;
                }
            } else {
                // 문제점은, 다음 end를 비교해보고, k를 넘어가는지 안남어가는지를 체크해야돼.
                if( value < k) {
                    end++;    
                } else {
                    start++;
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

            // 길이가 최소 길이보다 작다면,
            // 또는
            // 길이가 최소 길이와 같고, 인덱스가 더 빠르다면, 교환.
            if (currentLen < minLen || (currentLen == minLen && currentStart < answer[0])) {
                minLen = currentLen;
                answer[0] = currentStart;
                answer[1] = entry.getValue().get(1);
            }
        }

        return answer;
    }
}
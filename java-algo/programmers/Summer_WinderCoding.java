import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

class Solution {
    public int solution(int[] d, int budget) {
        ArrayList<Integer> arr = IntStream.of(d).boxed().collect(Collectors.toCollection(ArrayList::new));
        Collections.sort(arr);
        
        int count = 0;
        int currentBudget = budget;
        int idx = 0;

        while (true) {
            // 예산이 0이 되거나 모든 부서를 고려했을 때 종료
            if (currentBudget == 0 || idx == arr.size()) {
                break;
            }

            // 예산을 초과하지 않는 범위 내에서 최대한 많은 부서를 고려
            if (currentBudget >= arr.get(idx)) {
                currentBudget -= arr.get(idx++);
                count++;
            } else {
                break; // 예산을 초과하면 루프 종료
            }
        }
        return count;
    }

    public void solve(int budget, int [] d) {
        ArrayList<Integer> arr = IntStream.of(d).boxed().collect(Collectors.toCollection(ArrayList::new));
        Collections.sort(arr);
        
        int count = 0;
        int currentBudget = budget;
        int idx = 0;

        while (true) {
            // 예산이 0이 되거나 모든 부서를 고려했을 때 종료
            if (idx == arr.size() || currentBudget < arr.get(idx) || currentBudget == 0) {
                break;
            }
            if(currentBudget >= arr.get(idx)) {
                currentBudget -= arr.get(idx++);                 
                count++;
            } 
            
        }
        // return count;

    }
}

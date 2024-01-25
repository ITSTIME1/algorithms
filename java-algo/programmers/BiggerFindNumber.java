package programmers;
import java.util.*;
public class BiggerFindNumber {

    public static final int []numbers = {9, 1, 5, 3, 6, 2};
    public static void main(String[] args) {
        // 임시배열
        

        // 이게 어떻게 스택을 이용한 코드가 되는거지.

        int start = 0;
        int end = 1;
        int index = 0;
        
        int []answer = new int[numbers.length];

        while (start < numbers.length) {
            if(start == numbers.length -1 && end == numbers.length){
               answer[index] = -1;
               break;
            }
            
            // 뒷 큰 수를 발견했다면
            if(numbers[start] < numbers[end]) {
                answer[index++] = numbers[end];
                start++;
                end = start + 1;
            } else if(start != numbers.length - 1 && end == numbers.length - 1)  {
                if(numbers[start] >= numbers[end]) {
                    answer[index++] = -1;
                    start++;
                    end = start + 1;
                }
            } else{
                end++;
            }
        }

        // return answer;

    }   

    public static void stackSolve() {
        int[] answer = new int[numbers.length];
        List<Integer> stack = new ArrayList<>();

        for (int i = 0; i < numbers.length; i++) {
            // 스택이 비어 있다면 추가한다.
            if (stack.isEmpty()) {
                stack.add(i);
            } else {

                // 스택이 비어있지 않다면, 검사한다
                int index = stack.size() - 1;
                while (index > -1) {
                    int compareIndex = stack.get(index);
                    // 뒤 큰 수가 될 수 있다면
                    if (numbers[i] > numbers[compareIndex]) {
                        answer[compareIndex] = numbers[i];
                        stack.remove(index);
                    } else {
                        break; 
                    }
                    index--;
                }
                stack.add(i); 
            }
        }

        for (int i : stack) {
            answer[i] = -1;
        }
        // return answer;
    }
}

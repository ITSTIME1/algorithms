import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class ChildrenGift {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    public static void main(String[] args) throws IOException {
        String[] inputNM = br.readLine().split(" ");
        int N = Integer.parseInt(inputNM[0]);
        int M = Integer.parseInt(inputNM[1]);

        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> students = new ArrayList<>();

        for (int i = 0; i < N; i++) maxHeap.add(Integer.parseInt(st.nextToken()));
        
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < M; i++) students.add(Integer.parseInt(st.nextToken()));

        // students.sort(Comparator.reverseOrder());
        // O(N * logN)
        boolean isPossible = true;
        while (!students.isEmpty()) {
            // 어짜피 더 적은 개수의 선물이 남아 있으면 실망하니까
            // 0은 어짜피 가장 마지막에 있을거고, 근데 사실 0을 넣는 시간을 줄이는게 더 좋은 방법인데 
            if(maxHeap.peek() >= students.get(0)) {
                int result = maxHeap.poll() - students.get(0);
                students.remove(0);
                if (result == 0 ) continue;
                maxHeap.add(result);

            } else  {
                isPossible = false;
                break;
            }
        }

        if (isPossible) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}



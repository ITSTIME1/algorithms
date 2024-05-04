import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
// import java.util.Comparator;
import java.util.PriorityQueue;

public class MaxHeap {

    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    // public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static StringBuilder sb = new StringBuilder();
    // public static PriorityQueue<Integer> maxHeap = new PriorityQueue<>(new Comparator<Integer>() {
    //     @Override
    //     public int compare(Integer o1, Integer o2) {
    //         // 가장 앞 데이터를 꺼낼것이므로 내림차순을 유지한다.
    //         return o2 - o1;
    //     }
        
    // });
    public static PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

    public static void run() throws IOException{
        // 음수 데이터는 무시하고 있는것 같다.
        int N = Integer.parseInt(br.readLine());   
        while (N --> 0) {
            int num = Integer.parseInt(br.readLine());
            if(num < 0) continue;

            // 우선순위 큐를 만들어서
            // add 하게 되면 최대힙을 유지하게 됨
            if(num > 0) {
                maxHeap.add(num);
            } else if(num == 0) {
                if(maxHeap.isEmpty()) {
                    sb.append(0).append('\n');
                } else {
                    sb.append(maxHeap.poll()).append('\n');
                }
            }
        }
        System.out.println(sb.toString());
    }
    public static void main(String[] args) throws IOException{
        run();
    }  
}
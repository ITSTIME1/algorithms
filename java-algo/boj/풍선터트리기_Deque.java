/**
 * 풍선터트리기_Deque
 */
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class 풍선터트리기_Deque {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    public static void main(String[] args) throws IOException{
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());    

        Deque<int []> q = new ArrayDeque<>();
        int []arr = new int[N];
        for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());

        int in = arr[0];
        for (int i = 1; i < N; i++) {
            // index, move횟수
            // 파이썬의 튜플처럼
            q.add(new int[] {(i + 1), arr[i]});
        }
        StringBuilder sb = new StringBuilder();
        sb.append("1 ");

        
        while (!q.isEmpty()) {
            if( in > 0) {
                for (int i = 1; i< in; i++) {
                    q.add(q.poll());
                }
                int []nxt = q.poll();
                in = nxt[1];
                sb.append(nxt[0]+" ");
            } else {
                // 이렇게도 풀 수 있구나.
                for (int i = 1; i <-in; i++) {
                    q.addFirst(q.pollLast());
                }
                int []nxt = q.pollLast();
                in = nxt[1];
                sb.append(nxt[0] + " ");

            }
        }
        System.out.println(sb.toString());

    }
}
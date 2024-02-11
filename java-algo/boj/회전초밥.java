import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.Set;
import java.util.LinkedList;

public class 회전초밥_TLE {

    // 시간초과
    // O(N * K) 인데 최대 3만이고, K는 최대 3000이니까 최악의 경우 9000만 까지 계산이 되어야 하는데
    // 이게 1초안에 안되나.
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

        int[] arr = new int[N + k];
        for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(br.readLine());
        // 8 ~ 8 + 4 - 1= 8 ~ 11
        for (int i = N; i < N + k - 1; i++) arr[i] = arr[i-N];
       
        int start = 0;
        int end = k;

        Queue<Integer> sushi_belt = new LinkedList<>();
        int max = 1;
       
        for (int i = start; i < start + k; i++) sushi_belt.add(arr[i]);

        while (start < N) {
            Set<Integer> uniqueSushi = new HashSet<>(sushi_belt);
            
            if (sushi_belt.contains(c)) {
                max = Math.max(max, uniqueSushi.size());
            } else {
                max = Math.max(max, uniqueSushi.size() + 1);
            }

            
            sushi_belt.remove();
            start++;
            sushi_belt.add(arr[end++]);

        }
        System.out.println(max);
	}
}

// 6 6 6 6
// 1
// 2
// 3
// 4
// 5
// 6
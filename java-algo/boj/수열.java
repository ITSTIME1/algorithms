import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
/**
 * 수열
 */
public class 수열 {
    

    public static int run(int n, int k, int[] arr) {
        int start = 0;
        int end = 0;
        int max_number = -100 * k;
        int current_number = 0;

        while (end < n) {
            current_number += arr[end];
            if (end - start + 1 == k) {
                max_number = Math.max(max_number, current_number);
                current_number -= arr[start];
                start++;
            }
            end++;

        }

        return max_number;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        
        int []arr = new int[n];
        
        st = new StringTokenizer(br.readLine());
        
        
        for (int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(run(n, k, arr));
    }
}

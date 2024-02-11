import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 주몽
 */
public class 주몽 {
    public static int run(int [] arr, int target) {
        int start = 0;
        int end = arr.length - 1;
        int count = 0;
        Arrays.sort(arr);
        int current_number = 0;
        while (start < end) {
            current_number = arr[start] + arr[end];
            if(current_number == target) {
                count++; start++; end--;
            } else {
                if(current_number > target) {
                    end--;
                } else if(current_number < target) {
                    start++;
                }
            }
        }

        return count;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 재료개수
        int m = Integer.parseInt(br.readLine()); // 두 재료를 합해서 나온 결과

        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(run(arr, m));
    }
}
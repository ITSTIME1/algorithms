import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 두수의합 {
    public static int run(int [] arr, int target, int length) {
        int start = 0;
        int end = length - 1;
        
        int number = 0;
        int count = 0;

        Arrays.sort(arr);

        while (start < end) {
            number = arr[start] + arr[end];
            if(number == target) {
                count++;
                start++; end--;
            } else if(number > target) {
                end--;
            } else if (number < target) {
                start++;
            }
        }
        return count;
    }

    public static void main(String[] args) throws IOException{
       
        // 결과적으로, 시간복잡도가 O((N - 2) * N) 이 되므로, O(N^2 - 2n) 시간이 걸리게 되고
        // O(N^2) 시간이 걸린다는 걸 알 수 있음.
        // 그럼 10만 * 10만 이면, 100억까지 가기 때문에 위에 계산이 맞음.

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 수열의 개수

        StringTokenizer st = new StringTokenizer(br.readLine());
        
        // 배열을 받아서 저장해주고
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 타겟을 받아줌
        int x = Integer.parseInt(br.readLine());

        // 여기서 부터 시작할 것.
        System.out.println(run(arr, x, n));



    }
}
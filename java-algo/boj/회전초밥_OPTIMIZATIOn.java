import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 회전초밥_OPTIMIZATIOn
 */
public class 회전초밥_OPTIMIZATIOn {
    // 오케이 이런식으로 하면 될거 같음


    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int d= Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        // 초밥 종류를 저장할 개수
        int[] sushi = new int[d + 1];

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = Integer.parseInt(br.readLine());

        // end를 추가하는 것을 생각해 본다면
        int end = k;
        int start = 0;

        // 전처리를 할건데
        // 먼저 k까지 있는 초밥의 개수들을 저장해서 처음 구간을 남겨놓고
        // 제거하고, 추가하는 과정을 시작해보자.
        // 1부터, 이건 쿠폰을 미리 먹고 시작한다.
        // 중복을 제외하고, 몇개인지를 처음에 max로 만들어둔다.
        int max = 1;
        sushi[c] += 1;
        for (int i = 0; i < start + k; i++) {
            if (sushi[arr[i]] == 0) {
                max++;
            }
            sushi[arr[i]]++;
        }

        // 7 9 7 30 2 7 9 25
        int result = max;
        while(start < n) {
            // 그럼 추가하는 원소가 있으니
            // 처음 원소를 제거 할건데
            sushi[arr[start]] -= 1;

            // 만약에 처음걸 뺐는데 0 이 되었다면,
            // result를 제외해준다. 만약 0이 되지 않았다면
            // 현재 배열에 이미 해당 원소가 있는 것 이므로 지우지 않는다.
            if(sushi[arr[start]] == 0) {
                result -= 1;
            }

            // 새로 들어온, 값이 만약 처음 들어온 값이라면 max값을 증가시켜준다.
            if(sushi[arr[end]] == 0) result += 1;
            max = Math.max(max, result);
            sushi[arr[end]] += 1;
            start++;
            end = (end + 1) % n;
        }

        System.out.println(max);
    }

}
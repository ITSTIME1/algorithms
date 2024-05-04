import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * 황금칵테일
 */
public class 황금칵테일 {
    private static Map<String, Integer> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String key = st.nextToken();
            map.put(key, map.getOrDefault(key, 0) + Integer.parseInt(st.nextToken()));
        }

        
        boolean isFind = false;
        for (String key : map.keySet()) {
            for (String sub_key : map.keySet()) {
                // 소수를 내림해서 가장 가까운 정수로변환.
                if(!key.equals(sub_key) && (map.get(key) == (int)(map.get(sub_key) * 1.618))) {
                    isFind = true;
                    break;
                }
            }
            if(isFind) break;
        }

        System.out.println(isFind ? "Delicious" : "Not Delicious...");

        // 만약 이게 I, j로 이루어져 있다면,
        // i, j로 구분할 수 도 있을텐데 i, j = i + 1
        // 두 개를 비교해보는걸로 해볼 수 있을텐데.. 그럼 아이디어가 똑같으니까 맞을거고
        
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class 인사성밝은곰곰이 {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static void run() throws IOException{
        int N = Integer.parseInt(br.readLine());
        HashMap<String, Boolean> map = new HashMap<>();

        // 전체 시간복잡도는 O(N * logN)
        int count = 0;
        for (int i = 0 ; i < N; i++) {
            String str = br.readLine();
            if(!str.equals("ENTER")) {
                // logN
                // get()을 사용했을때 평균적으로 O(1)의 시간복잡도를 가지나, 해쉬버킷 안에 같은 아이템들이 있다면
                // 그것을 찾는데까지 최악의 경우 O(N)시간이 걸릴 수 있다. 하지만 이 시나리오는 극히 드문 케이스.
                // 그런데 jdk 1.8에서 hashmap을 조정했고, get 메소드가 O(logN)의 시간복잡도를 갖는다고 한다.
                // 따라서 get을 쓰든 containskey를 쓰든 최선의 경우 O(1)이지만, 최악의 경우 O(logN)의 성능을 가진다고 보면 된다.
                // 그러므로 N번만큼 순회하면서 ENTER가 아닌 경우에 containskey를 사용해서, hashmap에 키가 있는지 없는지 판단해야 하므로
                // 키가 존재한다면 O(1)만큼 그렇지 않다면 O(logn)만큼의 시간복잡도를 갖게 되어 O(N * logN)의 시간복잡도를 갖게 된다.
                if(!map.containsKey(str)) {
                    count++;
                    map.put(str, true);
                }
            } else {
                // map을 비우는 행위는 매번 하는 행위가 아니므로 시간복잡도에는 큰 영향을 미치지 않는다.
                map.clear(); // 맵을 효율적으로 비울 수 있다. O(N) 시간이 걸린다.
            }
        }
        System.out.println(count);


    }
    public static void main(String[] args) throws IOException{
        run();
    }

}
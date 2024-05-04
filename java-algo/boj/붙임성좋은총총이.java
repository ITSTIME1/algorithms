import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.io.IOException;

/**
 * 붙임성좋은총총이
 * 우선, 무지가 댄스를 추지 않은 사람이, 무지개 댄스를 추는 사람을 만나게 된다면
 * 그 시점 이후로, 무지개 댄스를 추지 않은 사람은 무지개 댄스를 추게 된다는 것.
 * 그리고 기록이 시작되기 이전에 무지개 댄스를 추고 있던 사람은 총총이 뿐이라고 한다.
 * 그렇다고 하는것은, 기록이 시작되고 나서, 총총이가 나오는 시점 이전에 나오는 사람들은
 * 무지개 댄스를 추는 사람일 수 없다.
 * 왜냐하면 기록이 시작되기 이전에 총총이만, 무지개 댄스를 추고 있고,
 * 총총이가 나오는 시점전에는 총총이를 본 사람이 없으며, 총총이를 보지 못했기 때문에
 * 무지개 댄스를 추지도 못하는 것이다.
 * 
 * 
 * 그럼 N개의 시간 순서가 주어지면서
 * 먼저 ChongChong이의 출현여부가 중요할거 같다.
 * 총총이가 기록이 시작된 이후에 처음부터 나오지 않고 만약 중간에 나오게 된다면
 * 그 전까지의 사람들은 무지개 댄스를 추는 사람은 없기 때문에, 총총이의 출현여부에 따라
 * 무지개 댄스의 사람수가 달라질거 같음. 총총은 기록에서 1회 이상 주어진다고 함.
 * 그렇다는건 chongchong이만 나올 수 있는 경우도 존재할거임.
 * 1회이상 주어질 수 있으니까
 * 
 * 그렇다면, 총총이가 한번은 나왔냐 나오지 않았냐가 중요하고
 * 만약 총총이가 지금 시점까지 한번도 나오지 않았고 두 명의 이름 전부 총총이가 아니라면
 * 이 둘은 무지개 댄스를 출 수 없으므로 넘어간다.
 * 
 * 만약 총총이가 지금 시점가지 한번은 나왔으며, 둘 다 총총이가 아니면서, 둘 중의 한명은 무지개 댄스를 추는 사람이라면
 * 다른 한명도 무지개 댄스를 출 수 있다.
 * 그렇지 않고 둘 다 총총이라면, 넘어간다.
 * 그렇지 않고 둘 중 아무도 무지개 댄스를 추지 않았다면 넘어간다.
 * 
 * 
 * 이걸 해결하기 위해서, 총총이의 출현여부를 하나의 변수로 잡아놓고
 * 총총이가 처음 나왔다면 해당 변수를 true로 만들어 준 다음에, HashMap에다가, 무지개 댄스를 추는 사람으로 등록해준다.
 * 그렇다면 이후에는 총총이가 출현했으니, 출현이후에 분기문을 해결해준다.
 */

 // 시간복잡도 O(N * 2NlogN)
public class 붙임성좋은총총이 {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static HashMap<String, Boolean> map = new HashMap<>();
    public static boolean chongExist = false;
    public static String chong = "ChongChong";
    public static int count = 0;
    

    public static void putMethod(String input) {
        map.put(input, true); count++;
    }

    public static void run() throws IOException{
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String[] names = br.readLine().split(" ");
            String name1 = names[0]; 
            String name2 = names[1];

            boolean s1 = name1.equals(chong);
            boolean s2 = name2.equals(chong);
            boolean c1 = map.containsKey(name1);
            boolean c2 = map.containsKey(name2);
        
            if(!chongExist) {

                if(s1 || s2) {
                    if(s1) {
                        putMethod(name2); 
                    } else {
                        putMethod(name1);
                    }
                    putMethod(chong);
                    chongExist = true;

                } else if(s1 && s2) {
                    // 이건 둘다 총일 경우
                    putMethod(chong);
                    chongExist = true;
                }
                
            } else {
                
                if(!s1 && !s2) {
                    
                    if(c1 && !c2) {
                        putMethod(name2);
                    } else if(!c1 && c2) {
                        putMethod(name1);
                    } else continue;

                } else if(s1 || s2){
                    
                    if(s1 && !s2) {
                        if(!c2) {
                            putMethod(name2);
                        }
                    } else if(!s1 && s2) {
                        if(!c1) {
                            putMethod(name1);
                        }
                    }
                }
            }
        }
        System.out.println(count);
    }

    public static void main(String[] args) throws IOException{
        run();
    }
}
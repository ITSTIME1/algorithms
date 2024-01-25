package programmers;
import java.util.*;
/**
 * LollCake
 */
public class LollCake {
    public int solution2(int[] topping) {
        int answer = 0;
        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashMap<Integer, Integer> map2 = new HashMap<>();

        // 키에 없으면 기본값 0을 반환, 만약 키가 있다면 그 키의 값을 반환
        for (int e : topping) {
            map2.put(e, map2.getOrDefault(e, 0) + 1);
        }

        for (int e : topping) {
            map1.put(e, map1.getOrDefault(e, 0) + 1);

            // 해당 토핑을 하나 넘겨준 것이니까
                // 만약 해당 토핑을 하나 넘겨주었는데, 다른한쪽에서 토핑이 더 이상 없다면 뺄 수 없으므로
                // 해당 토핑을 삭제한다.

            // 만약 그렇지 않다면, 토핑을 하나 삭제한다. 즉 토핑의 한개 이상 있다는 거니까.
            if(map2.get(e) - 1 == 0) {
                map2.remove(e);
            } else {
                map2.put(e, map2.get(e)- 1);
            }


            // 그럼 이제 테이블의 개수를 비교해서보면, 서로 다른 토핑의 개수가 같은지를 확인할 수 있으니까
            if(map1.size() == map2.size()) answer++;
        }

        return answer;
    }

    // 이런 풀이 말고도 배열로 관리할 수도 있네
    // 모든 토핑의 개수를 전부 개수를 세어준다음에
    // 음 새로운 토핑이 들어올때만 증가해서 비교해주는 것도 가능하다.
    // 새로운 토핑의 개수만 신경써주면 되고
    // 오른쪽에서는, 토핑을 삭감시킬때, 토핑의 개수가 0이 되면 더 이상 rs가 가지고 있는 토핑에서 해당 토핑은 없는거니까. 그것만 감소시켜주면
    // 토핑의 개수를 검사하는거니까 문제 없이 되겠네. 이야..
    public int solution(int[] topping) {
        int answer = 0;
        int[] left = new int[10001], right = new int[10001];
        int ls = 0, rs = 0;
        for(int i : topping) right[i]++;
        for(int i : right) rs += i > 0 ? 1 : 0;
        for(int i : topping) {
            right[i]--;
            if (right[i] == 0) rs--;
            if (left[i] == 0) ls++;
            left[i]++;
            if (rs == ls) answer++;
        }
        return answer;
    }



    public static void main(String[] args) {
        int[] topping = {1,2,1,1,4,2,3};
        int answer = 0;
        // topping 을 하나씩 가지고 와서 비교하는것도 일이긴한데

        // map말고 set을 이용해보면
        // set은 항상 중복을 제거할거니까, map에서는 개수를 하나씩 줄여주고
        // set에는 하나씩 추가 해준다면, 두개의 사이즈를 동일하게 비교할 수 있겠는데
        HashMap<Integer, Integer> map = new HashMap<>();
        HashSet<Integer> set = new HashSet<>();

        // for (int e : topping) {
        //     map.put(e, map.getOrDefault(e, 0) + 1);
        // }
        for (int i = 0; i < topping.length; i++) {
            // containskey로 해당 key값이 있는지 확인할 수 있구나.
            if(map.containsKey(topping[i])) {
                // containskey가 true라는건, 이미 값이 1개 이상이라는것.
                int getToppingValue = map.get(topping[i]);
                map.put(topping[i], getToppingValue + 1);

            } else {
                // containskey가 false라는건 없다는것이니까.
                // for문이 돌아가는 시점에서 false라는 것. 따라서 1개로 셋팅.
                map.put(topping[i], 1);
            }
        }

        for (int i = 0; i < topping.length; i+=1) {
            set.add(topping[i]);

            int cnt = map.get(topping[i]);
            // cnt - 1 == 0이 되려면 cnt = 1이니까 
            // cnt - 1 == 0이 되면, 삭제해야지
            if (cnt == 1 || cnt - 1 == 0) {
                map.remove(topping[i]);
            } else {
                map.put(topping[i], cnt - 1);
            }


            answer += set.size() == map.size() ? 1 : 0;
        }
    }



}
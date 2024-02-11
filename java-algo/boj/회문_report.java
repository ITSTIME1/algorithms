import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

/**
 * 회문
 */
public class 회문_report {


    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    

    public static void main(String[] args) throws IOException{
        int T = Integer.parseInt(br.readLine());

        while (T > 0) {
            String string = br.readLine();
            String[] stringArray = string.split("");
            int start = 0;
            int end = stringArray.length - 1;
            HashMap<String, Integer> string_hash = new HashMap<>();
            
            for(String s : stringArray) {
                string_hash.put(s, string_hash.getOrDefault(s, 0) + 1);
            }
            

            int cnt = 0;
            boolean isGeneral = false;
            while (start < end) {
                // 서로 같은 문자라면, 증가/감소
                if(stringArray[start].equals(stringArray[end])) {
                    start++; end--;
                } else {
                    // 서로 같은 문자가 아니라면
                    // 1. 짝수or홀수 인지 홀수or짝수인지
                    // 2. 짝수짝수인지
                    int start_value = string_hash.get(stringArray[start]);
                    int end_value = string_hash.get(stringArray[end]);
                    
                    
                    // 그럼 둘다 홀수인 경우를 다시 생각해 봐야 곘네
                    if(((start_value % 2 == 0) && (end_value % 2 == 0))) {
                        isGeneral = true;
                        break;
                    }
                    // (짝,홀), (홀,짝)
                    else if(start_value % 2 == 1 || end_value % 2 == 0) {
                        string_hash.put(stringArray[start], start_value - 1); 
                        start++; 
                        cnt++;
                    }
                    else if(start_value % 2 == 0 || end_value % 2 == 1) {
                        string_hash.put(stringArray[end], end_value - 1);
                        end--; 
                        cnt++;
                    } else if(start_value % 2 == 1  && end_value % 2 == 1) {
                        // 둘다 홀수인경우
                        // 얘는 어떤걸 삭제해도 똑같자나. 그러면 상관없는거 같은데
                        // abca
                        // 서로 다른 문자 and 둘다 홀수 그때 둘 다1이라면 둘 중 홀수개수가 적은거 하나삭제


                        // 둘다 홀수인 경우에는 좀 뭔가 체크를 해야 되네
                        // 현재 index앞에 원소가 start와 같은지를 봐야 될거 같은데
                        // xabbay
                        // 이 예제랑 같은거 같은데
                        // 둘다 홀수인데 개수가 둘다 1이라면
                        // 둘다 지워야 하므로 2가되고

                    }
                    
                }
                          
            }
            if(!isGeneral) {
                if(cnt == 0) System.out.println(0);
                else if(cnt == 1) System.out.println(1);
            } else {
                System.out.println(2);
            }

            T--;
        }
        

        
    }
}

package programmers;
import java.util.*;
/**
 * kakao2024_order
 */
public class kakao2024_order {
    public static void main(String[] args) {
        // 지원자 정보
        String [] info = {"java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"};
        // 쿼리들
        String [] query = {"java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"};
        
        // 코딩테스트 점수
        HashMap<Integer, Integer> grade_list = new HashMap<>();

        // 쿼리의 길이만큼, 지원자의 개수를 세주어야 하기 때문에, 쿼리의 개수만큼 0을 추가한다.
        Integer [] answer = new Integer[query.length];
        for(int i = 0; i < query.length; i++) {
            answer[i] = 0;
        }

        // 코딩테스트 점수를 먼저 넣어놓자
        for (int i = 0; i < info.length; i++) {
            String[] parts = info[i].split(" ");
            grade_list.put(i, Integer.parseInt(parts[4]));
        }
    
        // 문자열을 분리하고, 코딩테스트 점수를 먼저 선별한다.
        int outIndex = 0;
        for(String log : query) {
            // and 로 구분
            String[] parts = log.split(" and ");
            String[] lastParts = parts[3].split(" ");


            HashSet<String> compareSet1 = new HashSet<>();
            
            // 코딩테스트 성적
            int grade = Integer.parseInt(lastParts[1]);
            // 피자 다시 넣기
            parts[3] = lastParts[0];

            // 셋에다가 넣어줌.
            for (String i : parts) {
                compareSet1.add(i);
            }
            
            // 그럼 이제 여기서 성적 이상 되는 것들만 맵에서 가지고 오면 되겠지
            List<Integer> filtering = new ArrayList<>();

            
            for(Map.Entry<Integer,Integer> entry : grade_list.entrySet()) {
                // 특정 성적 이상 이라면, filterring에서 추가.
                if(entry.getValue() >= grade) {
                    filtering.add(entry.getKey());
                } else {
                    continue;
                }
            }
            for (int index : filtering) {
                // 포함되는 인덱스들만 모아놨을 테니까, 저 값들을 하나씩 info에서 가지고 오낟
                HashSet<String> compareSet2 = new HashSet<>();
                String[] infoSplit = info[index].split(" ");
                String infoSplitParts = infoSplit[3].split(" ")[0];
                infoSplit[3] = infoSplitParts;
                
                // info 를 split함. 
                // 비교하기 위해서 set에 집어넣음.
                for (int i = 0; i < infoSplit.length - 1; i ++) {
                    compareSet2.add(infoSplit[i]);
                }

                // 교집합을 계산 해본다.
                
                HashSet<String> intersection = new HashSet<>(compareSet1);
                intersection.retainAll(compareSet2);

                // 교집합의 개수니까
                int compareSize = intersection.size();
                // 쿼리에서 - 인것의 개수를 세야하니까
                int lineCount = 0;
                for (String i : parts) {
                    if(i.equals("-")) {
                        lineCount++;
                    }
                }

                // 개수가 맞다면 지원자를 증가시킼ㄴ다.
                if(compareSize + lineCount == 4) {
                    answer[outIndex] += 1;
                }
        

            }
            outIndex++;
        }
        System.out.println(Arrays.toString(answer));

    }
}
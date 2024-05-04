// import java.io.BufferedReader;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.util.ArrayList;
// import java.util.Arrays;
// import java.util.List;

// public class 앵무새{

// 	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
// 	public static void main(String[] args) throws IOException{
// 		int N = Integer.parseInt(br.readLine());

// 		List<String> words = new ArrayList<>();
// 		for (int i = 0 ; i < N; i++) {
// 			String[] w = br.readLine().split(" ");
// 			for (String s : w) {
// 				words.add(s);
// 			}
// 		}
// 		List<String> output = new ArrayList<>();
// 		StringBuilder sb = new StringBuilder();
// 		boolean visited[] = new boolean[words.size()];

// 		String l = br.readLine();

// 		for (int i = 0 ; i < N; i++)  {
// 			permutation(words, output, 0, words.size(), l, visited);
// 		}
		

// 	}
// 	/**
// 	 * 
// 	 * @param words = 원본 배열
// 	 * @param sb = 저장할 단어
// 	 * @param depth = 현재 인덱스
// 	 * @param r = 만들어야 하는 단어의 개수
// 	 */
// 	private static void permutation(List<String> words, List<String> output, int depth, int r, String ori, boolean[] visited ) {
// 		// 모든 단어가 완성 되었다면
// 		if(depth == r) {
// 			StringBuilder sb = new StringBuilder();
// 			for (String s : output){
// 				sb.append(s);
// 			}
// 			if(sb.toString() == ori) {
// 				System.out.println("Possible");
// 				return;
// 			}

// 		}
// 		for (int i = 0; i < words.size(); i++) {
// 			if(!visited[i]) {
// 				visited[i] = true;
// 				output.add(words.get(i));
// 				permutation(words, output, depth + 1, r, ori, visited);
// 				output.remove(output.size() -1 );
// 				visited[i] = false;
// 			}
// 		}
// 	}
// }	

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class 앵무새 {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        int N = Integer.parseInt(br.readLine());

        List<String> words = new ArrayList<>();
		

        for (int i = 0; i < N; i++) {
            String[] w = br.readLine().split(" ");
            for (String s : w) {
                words.add(s);
            }
        }

		boolean[] visited = new boolean[words.size()];

        String ori = br.readLine();
		
		for (int i= 0 ; i < N; i++) {
			permutation(words, new ArrayList<>(), 0, words.size(), visited, ori);
		}
        System.out.println("Impossible");
    }

    private static void permutation(List<String> words, List<String> output, int depth, int r, boolean[] visited, String ori) {
        if (depth == r) {

            StringBuilder sb = new StringBuilder();
			for (int i = 0; i < output.size(); i++) {
				if( i !=  output.size() - 1) {
					sb.append(output.get(i)).append(" ");
				} else {
					sb.append(output.get(i));
				}
			}


			// 아 단어 자체를 조합하면 안되는거구나 그러면 이해가 가지.
			// 그럼 각각을 방문순서에 따라서 구현이 되어야 하는거네
			
            if (sb.toString().equals(ori)) {
				System.out.println(sb + ", " + ori);
                System.out.println("Possible");
                System.exit(0); // 답을 찾았으면 프로그램 종료
            }
            return; // 찾지 못한 경우에는 더 이상 진행하지 않음
        }
        for (int i = 0; i < words.size(); i++) {
			// 만약에 방문하지 않은 단어라면
			if(!visited[i]) {
				output.add(words.get(i));
				visited[i] = true;
            	permutation(words, output, depth + 1, r, visited, ori);
            	output.remove(output.size() - 1);
				visited[i] = false;
			}
        }
    }
}

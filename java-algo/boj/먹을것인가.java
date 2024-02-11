import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;



public class 먹을것인가 {
	// run case

	public static void run() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine()); // TestCase
		while ( T > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int N = Integer.parseInt(st.nextToken()); // A 의 원소 크기
			int M = Integer.parseInt(st.nextToken()); // B 의 원소 크기

			st = new StringTokenizer(br.readLine()); // A의 원소들

			// set을 통해서 이미 걸렀으니까 이걸 List로 바꾸자
			List<Integer> A_arr_list = new ArrayList<>();
			List<Integer> B_arr_list = new ArrayList<>();
			
			// HashSet<Integer> A_arr_set = new HashSet<>();
			// HashSet<Integer> B_arr_set = new HashSet<>();


			for (int i = 0; i < N; i++) A_arr_list.add(Integer.parseInt(st.nextToken()));

			st = new StringTokenizer(br.readLine());

			for (int i = 0; i < M; i++) B_arr_list.add(Integer.parseInt(st.nextToken()));



			int start = 0;
			int end = 0;


			


			// 그럼 이제 sort
			Collections.sort(A_arr_list, Collections.reverseOrder());
			Collections.sort(B_arr_list, Collections.reverseOrder());


			int count = 0;

			// end >= M or start >= N 
			while (start < A_arr_list.size() && end < B_arr_list.size()) {
			
				if(A_arr_list.get(start) > B_arr_list.get(end)) {
					int b_c = B_arr_list.size() - end;
					count += b_c;
					start++;

				} else if(A_arr_list.get(start) <= B_arr_list.get(end)) {
					end++;
				}
			}
			

			System.out.println(count);
			
			T--;
		}



	}
	public static void main(String[] args) throws IOException{
		run();
	}
}



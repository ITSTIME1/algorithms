
// O(T * N * M)
// 삭제 연산이 필요 없는 방법이 존재하네 와우
// 대단한데 방문 배열을 이용한걸 생각해 내는구만.
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.ArrayList;
import java.util.HashSet;

public class 여우는어떻게울지 {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static StringBuilder sb = new StringBuilder();
	private static String endCheckString = "what does the fox say?";

	private static void run( ) throws Exception{

		// test case
		int T = Integer.parseInt(br.readLine());

		while (T --> 0) {
			// original record string
			List<String> records = new ArrayList<>(List.of(br.readLine().split(" ")));
			// records size
			int n = records.size();
			// other animal sound
			HashSet<String> notExistFox = new HashSet<>();

			// check "what does the fox say?"
			while(true) {
				String checkString = br.readLine();
				if(checkString.equals(endCheckString)) {
					// run logic then print
					for (String sound : notExistFox) {
						for (int i = 0; i < n; i++) {
							if (records.get(i).equals(sound)) {
								records.remove(i);
								i--;
							}
						}
					}
					// end main logic
					break;
				} else {
					notExistFox.add(checkString.split(" ")[2]);
				}
			}
			// print records for fox
			sb.append(String.join(" ", records));
			System.out.println(sb);
			sb.setLength(0);
		}

	} 

	public static void main(String[] args) throws Exception{
		run();	
	}

}
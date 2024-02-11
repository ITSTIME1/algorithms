import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class 공통부분문자열 {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void run() throws IOException{
		String firstString = br.readLine();
		String secondString = br.readLine();

		String maxString = firstString.length() > secondString.length() ? firstString : secondString;

		String minString = maxString.equals(firstString) ? secondString : firstString;

		int offset = 0;
		int maxStringCount = 0;


		for (int i = 0; i < minString.length(); i++) {
			for (int j = i+ 1; j < minString.length() - offset; j++) {

				// O(N)의 시간복잡도를 가지게 됨 그럼 O(N^3 * M^3)
				String compareString = minString.substring(i, j);


				for (int k = 0; k < maxString.length(); k++) {
					for (int f = k + 1; f < maxString.length() - offset; f++) {
						// 여기서 O(M)만큼을 추가로 해야 되니까
						String compareStringTwo = maxString.substring(k, f);
						// 공통된 부분 문자열 이라면,
						if(compareString.equals(compareStringTwo)) {
							// 나이지를 제고
							int size = compareString.length();

							maxStringCount = Math.max(maxStringCount, size);
						}

					}
				}

			}	
		}




		System.out.println(maxStringCount);




	}


	public static void main(String[] args) throws IOException{
		run();
	}
}






// O ((N * N - offset) * (M * M - offset))
// O((N^2 * M^2))
// substring메소드로 인해서 N^3 * M^3이 됨.

// 최대 3200만 이기 때문에 가능함.
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class 회문 {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


	public static boolean isPalindrome(int start, int end, char[] array){
		while (start < end) {

			// 여기서 걸리게 되면, 유사회문을 만들 수 없으므로
			if(array[start] != array[end]) {
				return false;
			}

			start++;
			end--;
		}

		// 그렇지 않다면, 유사회문을 만들 수 있음
		return true;

	}

	public static void run() throws IOException{

		// 케이스
		int T = Integer.parseInt(br.readLine());


		while ( T > 0) {

			String str = br.readLine();
			// 배열로 바꿔준다. ( 문자끼리 검사하기 때문에)
			char [] array = str.toCharArray();

			// start, end
			int start = 0;
			int end = array.length - 1;
			boolean flag = true;
			while (start < end) {

				if(array[start] != array[end]) {
					// 둘중에 하나라도 참이라면, 유사회문이니까
					if(isPalindrome(start+1, end, array) || isPalindrome(start, end - 1, array)){
						System.out.println(1); flag = false; break;
					} else {
						System.out.println(2); flag = false; break;
					}
				}

				start++;
				end--;
			}
			if(flag) System.out.println(0);
			T--;

		}
	}
	
	public static void main(String[] args) throws IOException{
		
		run();
	}
}
import java.util.*;
import java.io.*;

class 탑_Monotonic_Stack {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	public static Stack<Integer> stack = new Stack<>();

	public static void run() throws IOException{
		int N = Integer.parseInt(br.readLine());
		int [] top = new int[N];
		int [] answer = new int[N]; // 50만 * 4byte = 200만바이트 = 2MB * 2 = 4MB

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i=0; i < N; i++) top[i] = Integer.parseInt(st.nextToken());

		stack.push(N - 1); // index넣어주자.

		for (int i = N - 2; i >= 0; i--){
			while(!stack.isEmpty() && top[stack.peek()] < top[i]) {
				answer[stack.pop()] = i + 1;
			}
			stack.push(i);
		} 
		
		for (int i = 0; i < N; i++) {
			bw.write(Integer.toString(answer[i]));
			if(i != N - 1) {
				bw.write(" ");
			}
		}
		bw.flush();

	}
	
	public static void main(String[] args) throws IOException{
		run();
	}
}










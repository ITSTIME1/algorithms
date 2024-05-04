import java.util.*;
import java.io.*;

public class 오큰수 {

	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static StringBuilder sb = new StringBuilder();

	public static void run() throws IOException{
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		int[] answer = new int[N];
		Arrays.fill(answer, -1); // 미리 -1로 채워두고, 변경이 필요한 부분만 바꾸면 되니까

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) arr[i] = Integer.parseInt(st.nextToken());
			

		// 리스트를 쓰면 되네
		// Stack<Integer> stack = new Stack<>();
		List<Integer> stack = new ArrayList<>();
		stack.add(0);

		// 이 방식이 가장 좋긴하네
		// stack자료구조를 이용하면 peek()참조할 수 있으니까 마지막 값을
		// 오.. stack구조.. 좋아.
		for (int i = 1; i < N; i++) {
			// 스택이 비어 있지 않고, 항상 마지막값을 참조했을때 현재값보다 크다면
			// 스택이 비어있다면 돌지 않을거고
			// 스택이 비어있진 않지만 스택의 마지막 값을 참조했을때 현재 값이 더 크다면 뺀다
			// 작다면 넣는데, 아 그럼 이전에 작은 값들은 
			while(!stack.isEmpty() && arr[stack.peek()] < arr[i]) {
				answer[stack.pop()] = arr[i];
			}
			stack.push(i);
		}
		for (int i = 0; i < N; i++){
			if (i != N - 1) {
				sb.append(answer[i]).append(" ");
			} else {
				sb.append(answer[i]);
			}
		}


		
		// int index = stack.size() - 1;
		// for (int i = 1; i < N; i++) {
				
		// 	// index참조가 너무 에바가 되니까
		// 	while(!stack.isEmpty() && stack.get(index) < arr[i]) {
		// 		int value = stack.get(index);
		// 		answer[value] = arr[i];
		// 		stack.remove(index);
		// 		index--;
		// 	}
		// 	stack.add(i);
		// }
		for (int i = 0; i < N; i++) {
			if(i != N-1){
				sb.append(answer[i]).append(" ");
			} else {
				sb.append(answer[i]);
			}
		// }
		}
		
		System.out.println(sb.toString());

// 7
// 4 3 2 1 2 3 4
// -1 4 3 2 3 4 -1


	}
	public static void main(String[] args) throws IOException{
		run();
	}
}
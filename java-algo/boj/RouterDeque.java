import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.LinkedList;



// LinkedList가 포인터로 이루어져서 가장 빠른갑네.
class RouterDeque {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static Deque<Integer> q = new LinkedList<>();
	public static StringBuilder sb = new StringBuilder();
	
	public static void commonProcess(int data) {
		if(data == 0) q.removeFirst();

	}
	public static void run() throws IOException{
		int N = Integer.parseInt(br.readLine());

		while(true) {
			int packet = Integer.parseInt(br.readLine());
			if(packet < 0 ) break;
			// 0은 공통사항
			commonProcess(packet);
			// 큐가 꽉 차 있고, packet이 양수라면
			if(q.size() == N && packet > 0) continue;
			else if(q.size() != N && packet > 0) q.addLast(packet);
		}


		for (int p : q) sb.append(p).append(" ");

		System.out.println(sb.toString().isEmpty() ? "empty" : sb.toString());


	}
	public static void main(String[] args) throws IOException{
		run();
	}
}










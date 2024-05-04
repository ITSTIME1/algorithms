import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;


class Router {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static Queue<Integer> q = new LinkedList<>(); 
	public static StringBuilder sb = new StringBuilder();
	
	public static void commonProcess(int data) {
		if(data == 0) q.remove();

	}
	public static void run() throws IOException{
		int N = Integer.parseInt(br.readLine());

		while(true) {
			int packet = Integer.parseInt(br.readLine());
			if(packet < 0 ) break;

			// 0은 공통사항
			commonProcess(packet);

			// 큐가 꽉 차 있고, packet이 양수라면
			if(q.size() == N && packet > 0) {
				continue;
			} else if(q.size() != N && packet > 0) {
				q.offer(packet);
			}
		}


		for (int p : q) sb.append(p).append(" ");

		System.out.println(sb.toString().isEmpty() ? "empty" : sb.toString());


	}
	public static void main(String[] args) throws IOException{
		run();
	}
}










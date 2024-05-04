import java.util.*;
import java.io.*;


// 우선순위 큐 문제다.
// 큐를 두개 사용해야 함.
class SayMidian {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	public static List<Integer> list = new ArrayList<>();

	// O(N * NlogN)
	// O(NlogN) 풀어야함. 그러기 위해선 -> 우선순위큐를 사용하는게 좋음.

	// 즉 logN은 힙을 정렬하는데 사용되고 N 은 
	public static void run() throws IOException{
		int N = Integer.parseInt(br.readLine());

		// 최종적으로 O(NlogN)이 걸린다는것 힙은
		// 힙을구성하는데 N 만큼
		// heapify를 유지하는데 logN만큼의 시간이 사용되므로
		// 전체 시간 복잡도는 Overall time complexity is O(NlogN)

		// 힙에 대해서 더 공부해보아야 할 것 같다.
		PriorityQueue<Integer> minHeap = new PriorityQueue<>((o1, o2) -> o1-o2); // 최소힙을 유지 
		PriorityQueue<Integer> maxHeap = new PriorityQueue<>((o1, o2) -> o2-o1); // 최대힙을 유지 

		for (int i = 0; i<N; i++) {
			int num = Integer.parseInt(br.readLine());

			if(minHeap.size() == maxHeap.size()) maxHeap.offer(num);
			else minHeap.offer(num);



			// 두 개의 힙 모두 비어 있지 않다면
			// 검사할건데, 최대힙에 들어가 있는 마지막 값이, 최소힙의 마지막 값보다 크다면
			if(!minHeap.isEmpty() && !maxHeap.isEmpty()) {
				// [5], [2] <- 서로 스왑 해서 각 힙을 유지해줌.
				if(maxHeap.peek() > minHeap.peek()) {
					int tmp = minHeap.poll(); // 마지막 값을 꺼내고
					minHeap.offer(maxHeap.poll());
					maxHeap.offer(tmp);
				}
			}	
			bw.write(Integer.toString(maxHeap.peek()) + '\n');
		}

		bw.flush();

		
	}
	public static void main(String[] args) throws IOException{
		run();	
	}
}












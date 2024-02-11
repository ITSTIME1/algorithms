import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;


public class 도키도키간식드리미 {	
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


	public static void run_case_2() {

		int N = Integer.parseInt(br.readLine());
		int[] list = new int[N];

		StringTokenzier st = new StringTokenizer(br.readLine());	


		// 배열을 이용해서, 값을 저장해주고
		for (int i = 0; i < N; i++) list[i] = Integer.parseInt(st.nextToken());


		// stack자료구조를 하나 만들어서, 스택자료구조에다가, 저장할건데
		Stack<Integer> stack = new Stack<>();

		// 그럼 한번 생각해보면, stack에 있는걸 하나씩 살펴보면서
		// 만약 current_number와 같으면, 증가해주고
		// 만약 같지 않으면 생각해야 할 부분이, 스택이 비어있지 않고, 스택에 마지막에 있는 값에서 가지고 올 수 있다면
		// 가지고 오는 부분이라는건데

		// 이 부분을 생각해낸다면, 스택이 비어있을때는, 현재 라인에 통과해야 할 번호와 같지 않으니까
		// 스택으로 옮겨야 한다는사실은 알 수 있고
		// 그럼 스택으로 옮겨야 하니까, 스택에다가 저장해준다.
		// 그럼 반대로 스택이 비어있거나, 즉 스택의 마지막값이, CURRENT_NUMBER와 다르다면
		// 넣어주면 되는거지. 이렇게 if문을 개선할 수 있으니까
		int current_nubmer = 1;

		for (int i=0; i< N; i++) {
			// list[에 있는 현재 값이] current_number오 ㅏ같다면 즉 현재 뽑아야 하는 번호라면
			if(list[i] == current_nubmer) {
				current_number++;
			} else {
				// peek() 함수로 인해서 fetching하는거네
				// 패칭을 함으로써, current_number인것을 알 수 잇는거고
				// 비어 있지 않아야, 스택의 가장 윗부분을 확인할 수 있으니까
				// 그럼 가장 윗 부분을 확인했을때, current_number라면
				// 뺄 수 있는데 i는 왜감소시키지.
				// 아 지금 이상황은, list[i]가 가리키는 값이,
				// current-number가 아닌것이고, list[i]는 원래 있던 줄을 검사하고 잇었자나
				// 근데 생각해보면, 원래 있던 줄에 있던 current_nubmer와 다르기 때문에
				// 대기 줄에 있던 사람을 확인한거고, 그러므로 list[i]에 영향이 없어야지
				// 하지만 for문은 자동적으로 i가 증가하기 때문에,
				// i를 증가시키지 않고, i를 감소시켜서, 현재 i를 유지하는거지. 그래서 i를 감소시켰네 오 좋은 기법이야
				if(!stack.isEmpty() && stack.peek() == current_number) {
					current_number++;
					i--; // 아 스택
				} else {
					// 스택이 비어있거나 또는 스택의 가장 맨 위에 헤드가, current_number가 아니라면 스택에 넣어주는거지
					// 일단 이런 상황은, 이걸 생각해보면 되는거지
					// 현재 검사하려는 줄에 있던 가장앞에 잇떤 사람의 번호가
					// 현재 들어올 사람의 번호가 아니라면 결국 그 사람이 대기해야 하니까
					// 스택이 비어 있다면 그 사람이 처음 들어가게 되는거고
					// 그 처음 들어가는 순간에는 이 대기열에서 현재 넘버와비교할 사람이 없기 때매ㅜㄴ에
					// 넣어주기만 하면되고, 어짜피 라인에 못들어가니까
					// 근데 만약에 스택에 비어있지 않고, 마지막 값에서 , 현재 번호표가 들어가기 전에
					// 빠져나올 수도 있자나, 그렇게 되면, 먼저 그 사람을 뺀 다음에
					// 이 사람을 집어 넣어야 겠지
					// 그래서 우선적으로 스택에 가장 윗부분까지도 고려한다음에 그게 위 ㅅ부분을 커버하는거ㅗ
					// 윗부분을 먼저 검사 했으므로, 라인이 맞지 않으니 넣어주는거지
					// i를 줄이는 부분에 대해서 배우게 되었네

				}
			}
		}

		// 근데 이렇게 하고나서 문제가 있지, 대기열에 존재하는 사람들이 계속 남아 있을 수 있다는거야
		// 왜냐하면, 모두 라인에 들어갈 수 있도록 되어 있다면 문제가 되지 않지만
		// 만약 순서상에서도, 라인이 들어갈 번호가 아니고, 스택에서 가장 위에 있는 값도, 현재 번호표가 아니라면
		// 이 사람은 도저히 갈 곳이 없으므로, 무조건 대기열에 들어가야 하고, 그렇게 되면
		// 도저히 갈 곳이 없어 계속 대기열에 남아 있는 사람들까지도, 해결을 해주어야 하므로
		// 이건 현재 번호가 줄에 좀 뒤에 있는 편에 속할때를 말해
		// 그런 경우라면 어쩔 수 없지. 그렇기 때문에, 대기열에 존재하는 사람들 또한, 가장 윗 스택에서부터
		// 다시 한번 뺄 수 있는 사람이 있는지 확인해야하며, 마지막으로 확인할때도, 대기열에 존재하는 사람은 다시 원래 줄로 돌아가지 못하므로 즉 이건
		// 대기열에 존재하는 사람을 다시, 원래 대기하는 줄에 다가 꺼내서, 원래 있던 값을 꺼내려고 하는 행동위 안된다는거지
		// 이렇게 되면 순서를 맞출 수 있으므로
		// 따라서 이건 허용하지 않으면서, 마지막으로 확인했을 때, 스택에서 가장 위에 있는 값이 현재번호와같지 않다면 더 이상 
		// 이건 번호가 라인의 순서와 맞지 않으므로, 이 라인은 nice하지 않은 것이지.




	}


	public static void main(String[] args) throws IOException{
		// Get total number
		int N = Integer.parseInt(br.readLine());



		StringTokenizer st = new StringTokenizer(br.readLine());
		Queue<Integer> arr = new LinkedList<>();
		for (int i =0; i < N; i++) arr.add(Integer.parseInt(st.nextToken()));

		List<Integer> wait_arr = new ArrayList<>();

		int current_number = 1;

		// 모두 비어있지 않을 동안 반복한다.
		boolean flag = true;
		while(!arr.isEmpty()) {
	
			if(arr.peek() == current_number) {
				current_number++;
				arr.remove();
			} else {
				if(wait_arr.isEmpty()) {
					wait_arr.add(arr.remove());
				} else {
					int lastIndex = wait_arr.size() - 1;
					int r = wait_arr.get(lastIndex);
					if (r == current_number) {
						wait_arr.remove(lastIndex);
						current_number++;
					} else {
						wait_arr.add(arr.remove());
					}
				}
			} 
			
		}

	

		// wait남아있을 수 있고
		while(!wait_arr.isEmpty()) {
			int p = wait_arr.get(wait_arr.size() - 1);
			if( p == current_number) {
				current_number++;
				wait_arr.remove(wait_arr.size() - 1);
			} else {
				flag = false;
				break;
			}
		}
		if(flag) {
			System.out.println("Nice");
		} else {
			System.out.println("Sad");
		}

	}
}
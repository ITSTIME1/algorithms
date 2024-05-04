/**
 * 재밌는 문제네
 * 일단 문제 이해는 되었고
 * 이게 N이 50만개가 주어져 N이 탑의 개수인데
 * 이 탑의 개수가 50만개까지 주어지면
 * 모든 탑을 확인을 해보아야 하기 때문에 50만개를 순회하는건 당연한데
 * 해당 탑에서 왼쪽으로 레이저를 발사하기 때문에
 * 가장 이 레이저를 먼저 수신하는 탑을 찾는게 목적이야.
 * 
 * 
 * 그럼 서로 같거나 레이저를 쏜 탑의 높이보다는 커야 수신이 가능하겠지
 * 만약 작으면 해당 레이저 수신을 받지 못할테니까
 * 
 * 
 * loop start > 0 && end > 0
 *  
 * 음 일관성있게 진행될거 같은데? 투포인터로 풀면 O(n)시간안에 해결이 가능하니가
 * 일정하게 index를 탐색하는 방향으로 갈 수 있음.
 * 
 * 1 1 1 1 1 
 * 6 9 5 8 8
 * 
 * 탑의 개수만큼 0으로 만들어두자.
 * 
 * 근데 기둥이 같을때에 대한 설명이 없는데..
 * 애매모하하네
 * 
 * 
 * 아 탑의 높이는 모두 서로 다르다고 명시되어 있네
 * 그러면 모든 탑들의 높이가 서로 다르다고 볼 수 있음.
 * 
 * 
 * 6 9 5 7 4
 * 
 * 그럼 처음에 start, end = array.size - 1이다.
 * 이때 end랑 비교했을 때, 현재 start높이보다 더 큰 탑을 찾아.
 * 그럼 start = 3, end = 4 에서 해당 조건이 맞게되고, answer 배열에 모두 0으로 초기화 되어 있을테니 해당 값을, start + 1로 바꿔줘
 * 	조건을 만족한 순간, 더 이상 end가 4를 가리킬 이유가 없으므로, end를 낮춰
 * 그럼 반대로 end가 조건을 만족하지 않으면 start를 계속 증가시키면 되겠지
 * 처음은 어디에서 쏴도 받을 수 있는 구간이 없기 때문에 end가 0보다 작아지게 되면 종료하게 하면되고
 * end가 0보다 큰 경우까지만 보면돼 그럼 0 다음 1까지만 보게 될거고 end가 0을 가리켰을때 수신을 받을 수 있다면 즉 조건을 만족한다면 변경하겠지
 * 그럼 start도 감소하게 되서 최종적으로 0,0이 되니까 end가  >0 클 때 가지만 하면 될거 같에
 * 
 * 
 * 그럼 만약 이렇게 탑이 되어 있다면?
 * 조건을 만족하지 않으니까, end는 계속 감소하게 될거야
 * 만약 이 순간에도 하나라도 end가 조건에 만족해서 더 큰 탑의 높이에 걸리게 된다면
 * 이런식으로 6에서 걸리게되겠지 그럼 뒤에 있는것들은 모두 이 탑에 걸리게 될거고
 * 1 2 3 4
 * 하지만 만약 이렇게 되면 end는 끝까지 가게 될거야, 조건에 모두 만족하지 않으니까 그렇다는건
 * 다른 탑들도 그 이후에 값들을 만족할 수 없게 도ㅔ
 * 왜냐면 기본적으로 서로 다른 값을 갖고 있으니까 같은 값이 나올 수 없어
 * 같은 값이 있다면 얘기가 달라지지만 같은 값이 없기 때문에 가능한 풀이인데
 * end가 끝에 도달할때까지, 전부 수신을 못받게 될 수 있는거지
 * 4 3 2 1 
 * 이렇게 내림차순으로 되어 있으면, 당연히 하나씩 걸리게 되니까
 * 문제가 정확하게 조건에 맞게 되고
 * 
 * 결국 내가 증명하고 싶은건 오름차순으로 정렬이 되어 있는경우는
 * 그 어떤 곳에서도 받을 수 없다는거야
 * 왜냐면 end가 가리키는 값 이전의 탑들은 모두 해당 탑의 높이보다 작기 때문에
 * 결국 투포인터풀이가 가능한 이유가 되는거지.
 * N이 50만ㄱ까지 주어지니까 StringBuilder를 쓰자.
 * 
 * 아 생각해보니까 투 포인터로 못푸네
 * 
 * 9
	10 6 5 4 3 2 7 5 9

	이런경우 끝가지 내려가지만, 오름차순을 내가 가정하고 생각했는데 이게 아니지 생각해보니가
	그래 이런경우 5는 7이 받을 수 있는데, 못받으니까
	end를 다시 초기화 해야하므로 two-pointer풀이가 안됨.

	모노톤스택이네, 하 이거 반례 알기가 쉽지가 않아
	모노톤스택풀이.

 * */

import java.util.*;
import java.io.*;

class 탑_Two_pointer_faile {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static StringBuilder sb = new StringBuilder();

	public static void run() throws IOException{
		int N = Integer.parseInt(br.readLine());
		int [] top = new int[N];
		int [] answer = new int[N]; // 50만 * 4byte = 200만바이트 = 2MB
		Arrays.fill(answer, 0);
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) top[i] = Integer.parseInt(st.nextToken());

		int start = N - 1; int end = N - 1;

		// 0까지는 봐야 하므로
		while (end > -1) {
			// end가 가리키는 탑의 높이가 start가 가리키는 탑의 높이보다 크다면
			if(top[end] > top[start]) {
				answer[start] = end + 1;
				start--;
			} else {
				// 같은경우는 없고 end가 작은 경우만 존재하므로
				end--;
			}
		}

		for (int i = 0; i < N; i++) {
			if(i != N - 1) {
				sb.append(answer[i]).append(" ");
			} else {
				sb.append(answer[i]);
			}
			
		}
		System.out.println(sb.toString());


	}
	public static void main(String[] args) throws IOException{
		run();
	}
}










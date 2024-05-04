import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashMap;



class 가희와키워드_HashMap {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static HashMap<String, Boolean> wordMap = new HashMap<>();

	public static void setWord(int N) throws IOException{

		for (int i=0; i < N; i++) {
			String word = br.readLine();
			if(!wordMap.containsKey(word)) {
				wordMap.put(word, true);
			}
		}

	}

	public static void writePost(int M) throws IOException{
		while(M-->0) {
			int count = wordMap.keySet().size();

			String[] words = br.readLine().split(",");
			for (String wd : words) {
				if(wordMap.containsKey(wd)) {
					wordMap.remove(wd);
					count--;
				}
			}
			System.out.println(count);
		}


	}


	public static void run() throws IOException{
		StringTokenizer sb = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(sb.nextToken());
		int M = Integer.parseInt(sb.nextToken());

		setWord(N);
		writePost(M);

	}
	public static void main(String[] args) throws IOException{
		run();
	}
}
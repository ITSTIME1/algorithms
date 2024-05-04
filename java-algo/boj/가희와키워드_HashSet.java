import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashSet;



class 가희와키워드_HashSet {
	public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static HashSet<String> wordSet = new HashSet<>();
    public static StringTokenizer st;
    public static StringBuilder sb = new StringBuilder();
	public static void setWord(int N) throws IOException{
        for (int i = 0; i < N; i++) {  

            wordSet.add(br.readLine());
        }
	}

	public static void writePost(int M) throws IOException{
		while(M-->0) {
            st = new StringTokenizer(br.readLine(), ",");

            // 단어가 남아 있을때까지
            while(st.hasMoreTokens()) {
                String key = st.nextToken();
                if(wordSet.contains(key)) {
                    wordSet.remove(key);
                }
            }
            
            sb.append(wordSet.size() + "\n");
            // sb를 초기화할 이유가 없이, count를 m만큼 sb에 만들어 놓고, 마지막에 출력하는게 더 효과적이긴하지.
		}
        System.out.println(sb.toString());


	}


	public static void run() throws IOException{
		st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		setWord(N);
		writePost(M);
	}

    
	public static void main(String[] args) throws IOException{
		run();
	}
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 풍선터트리기_Offset {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void run() throws IOException {
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 공간복잡도
        // boolean = 1byte * 1000 = 1000byte
        // int = 4byte * 1000 = 4000byte * 2 = 8000byte + 1000byte = 9000byte
        // 1메가도 안쓴다.
        boolean[] c_q = new boolean[N];
        int[] q = new int[N];


        for (int i = 0; i < N; i++) {
            q[i] = Integer.parseInt(st.nextToken());
        }

        int check = N;
        int index = 0;
        StringBuilder sb = new StringBuilder("");

        while (true) {
            // 풍선을 터뜨림

            c_q[index] = true;
            sb.append(index + 1 + " ");
            check--;
            if (check == 0) break;

            int move = q[index];
            // false라면 move도 감소시키지만, true라면 index만 옮기면되므로
            if (move > 0) {
                while(move > 0) {
                    index = (index + 1) % N;
                    if (!c_q[index]) move--;
                    
                    
                }
            } else if(move < 0) {
                while(move < 0) {
                    index = (index - 1 + N) % N;  
                    if(!c_q[index]) move++;
                    
                }
            }
        }
        
        System.out.println(sb.toString());
    
    }

    

    public static void main(String[] args) throws IOException {
        run();
    }
}

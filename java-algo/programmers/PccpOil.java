package programmers;
import java.util.*;

/**
 * PccpOil
 */
public class PccpOil {
    public static int solution(int[][] land) {
        int col = land.length;
        int row = land[0].length;

        boolean[][] visited = new boolean[col][row];
        int index = 2; // 시작 인덱스

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < col; i++) {
            for (int j = 0; j < row; j++) {
                if (land[i][j] == 1 && !visited[i][j]) {
                    int oilCount = bfs(i, j, land, visited, index);
                
                    if (!map.containsKey(index)) {
                        map.put(index, oilCount);
                    }
                    index++;
                }
            }
        }

        // 시추관, 땅과 
        HashMap<Integer, Set<Integer>> sichu = new HashMap<>();
        // 시추셋을 넣는다고, 그렇게 될 수가 있나
        for (int i = 0; i < row; i++) {
            Set<Integer> hashSet = new HashSet<>();
            for (int j = 0;  j < col; j++) {
                if(land[j][i] != 0) {
                    hashSet.add(land[j][i]);
                }
            }

            sichu.put(i, hashSet);
        }

        // Map.Entry로 출력해보자.
        int maxOil = 0;
        for (Map.Entry<Integer, Set<Integer>> entry : sichu.entrySet()) {
            Set<Integer> value = entry.getValue();
            int compareOil = 0;
            for (int s : value) {
                compareOil += map.get(s);
            }
            maxOil = maxOil < compareOil ? compareOil : maxOil;
        }

        return maxOil;
    }
    public static int bfs(int i, int j, int[][] land, boolean[][] visited, int index) {
        int col = land.length;
        int row = land[0].length;

        int[] dc = {-1, 1, 0, 0};
        int[] dr = {0, 0, -1, 1};

        Queue<int[]> q = new LinkedList<>();
        visited[i][j] = true;
        land[i][j] = index;
        q.add(new int[]{i, j});

        int oilCount = 0;
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int c = current[0];
            int r = current[1];

            for (int in = 0; in < 4; in++) {
                int newCol = c + dc[in];
                int newRow = r + dr[in];

                if (newCol >= 0 && newCol < col && newRow >= 0 && newRow < row) {
                    if (land[newCol][newRow] == 1 && !visited[newCol][newRow]) {
                        q.add(new int[]{newCol, newRow});
                        visited[newCol][newRow] = true;
                        oilCount++;
                        land[newCol][newRow] = index;
                    }
                }
            }
        }
        return oilCount + 1;
    }
    public static void main(String[] args) {
        int[][] land = {
            {0, 0, 0, 1, 1, 1, 0, 0},
            {0, 0, 0, 0, 1, 1, 0, 0},
            {1, 1, 0, 0, 0, 1, 1, 0},
            {1, 1, 1, 0, 0, 0, 0, 0},
            {1, 1, 1, 0, 0, 0, 1, 1}
        };
        // int[][] land = {
        //     {1, 0, 1, 0, 1, 1},
        //     {1, 0, 1, 0, 0, 0},
        //     {1, 0, 1, 0, 0, 1},
        //     {1, 0, 0, 1, 0, 0},
        //     {1, 0, 0, 1, 0, 1},
        //     {1, 0, 0, 0, 0, 0},
        //     {1, 1, 1, 1, 1, 1}
        // };
        solution(land);
        
        for (int i = 0; i < land.length; i++) {
            for (int j = 0; j < land[0].length; j++) {
                System.out.print(land[i][j] + " ");
            }
            System.out.println();
        }
        

    }
}


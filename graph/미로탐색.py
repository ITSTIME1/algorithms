<<<<<<< HEAD
# 문제분석

=======
# DFS 사용, 런타임 에러 발생
>>>>>>> 94dbbe1a8364640ea245c7170a3c16422dc021f1
import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline
<<<<<<< HEAD

=======
sys.setrecursionlimit(10**6)
>>>>>>> 94dbbe1a8364640ea245c7170a3c16422dc021f1

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

<<<<<<< HEAD

arr = [input().strip() for _ in range(n)]
=======
# 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

z = []
def dfs(x, y, graph):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            # 갈 수 있다면
            graph[nx][ny] = graph[x][y] + 1
            z.append((nx, ny))
            # 도착지저밍면 아웃
            if nx == n-1 and ny == m-1:
                return
            dfs(nx, ny, graph)
    return 
dfs(0,0, graph)
print(graph)
print(graph[n-1][m-1])
# 마지막에 3, 3 으로 오게 되어 있음 dfs 재귀 콜스택이 하나씩 종료되면서
# 그럼 마지막에 1이 남긴 곳으로 오게 되어 있으니 3, 3을 예상할 수 있따.
print(z)
# [[True, True, False, True, True, False], 
# [True, True, False, True, True, False], 
# [True, True, True, True, True, True], 
# [True, True, True, True, False, True]]

# 모든 경로를 다 찾기 떄문에 불가능한데
# [[3, 4, 0, 14, 15, 0], 
# [2, 5, 0, 13, 16, 0], 
# [7, 6, 11, 12, 17, 18], 
# [8, 9, 10, 13, 0, 19]]

# 2번 예제가 다익스트라를 사용하지 않는다면
# 절대로 최단 경로를 찾는건 불가능해
# 왜냐하면 한번 간 경로를 다시 최소경로를 다시 탐색하지 않기 떄문이지
# 결과적으로 dfs 로 풀게되면
# 최단경로를 찾지 못한다는거야 위 2번예제 같은경우
# 왜냐하면 함수가 종료되는 즉시 콜스택에서 제거하기 때문이지

# 그럼 결국엔 마지막 n,m까지 도달하게 되면 가지 못했던 곳들을 전부 다 가면서 콜스택을 하나씩 제거하게 될거야
# 물론 이미 한번 dfs를 돌릴떄 모든경로를 다 탐색했기 때문에
# matrix 구간은 벗어나지 않지만 1인 구간은 없기 때문에
# 다익스트라 처럼 따로 경로를 재갱신 시키지 않는 이상은 절대로 재갱신이 안된다는것
# 물론 그마저도 런타임이 뜰 수 있따.
# 재갱신을 시킨다는거 그만큼 더 많은 연산을 진행해야 하기 떄문에
# 입력대비 너무 오랜 시간이 걸린다.
# 아무튼 재갱신을 시키지 않는다면 결론적으로 n, m 에 도달하게 ㅗ디면 콜스택에서 이전 콜스택에서 도달하지 않았던 경로를 찾게 ㅗ디고 결구겡ㄴ 전부 콜스택에서 지워지게 된다느 ㄴ것이다.
# 때문에 예제2번은 절대로 9가 나올 수 없다. " 재갱신을 시키지 않는 이상은."
>>>>>>> 94dbbe1a8364640ea245c7170a3c16422dc021f1

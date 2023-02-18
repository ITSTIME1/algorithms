# DFS 사용, 런타임 에러 발생
import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

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
            if graph[nx][ny] == 1 or graph[nx][ny] > grade[x][y] + 1:

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
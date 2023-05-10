import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline
sys.setrecursionlimit(10**7)




T = int(input())




def dfs(matrix, i):
    matrix[i] = 1
    node = vertex[i]-1
    if matrix[node] != 1:
        dfs(matrix, node)


def bfs(matrix, i):
    queue = deque([])
    queue.append(i)

    # 방문할곳이 남아있으니까
    while queue:
        node = queue.popleft()
        matrix[node] = 1
        
        if matrix[vertex[node]-1] != 1:
            matrix[vertex[node]-1] = 1
            queue.append(vertex[node]-1)







for i in range(T):
    n = int(input())

    vertex = list(map(int, input().split()))
    matrix = [0] * n

    ans = 0
    for i in range(len(vertex)):
        if matrix[i] == 0:
            # dfs(matrix, i)
            bfs(matrix, i)
            ans += 1

    print(ans)
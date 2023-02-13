import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline


n = int(input())

e = int(input())


# 1번 컴퓨터가 바이러스에 걸린다고 했으니까
# 1번 노드부터 시작한다
# def bfs(graph, root):

#     visited = set()
#     queue = deque([root])
#     visited.add(root)

#     while queue:
#         vertex = queue.popleft()
#         for neighbour in graph[str(vertex)]:
#             if neighbour not in visited:
#             	visited.add(str(neighbour))
#             	queue.append(neighbour)
#     return visited

def dfs(graph, start, visited=None):
    # 처음엔 none 이니까 visited 를 생성 하고
    if visited is None:
        visited = set()
    visited.add(str(start))


    # for next in graph[start] - visited:
    #     dfs(graph, next, visited)
    # return visited

    # 2
    for i in graph[str(start)]:
        if str(i) not in visited:
            dfs(graph, str(i), visited)
    return visited





# 7 개의 컴퓨터가 존재하고 1~7번까지의 컴퓨터가 있다
# 6 쌍이 존재한다 각각의 컴퓨터는


# n = 7 이란건 정점의 개수가 7개라는건데
# e 라는건 간선의 개수를 의미하고
graph = {str(i): [] for i in range(1, n+1)}

for i in range(e):
	f, s = map(int, input().split())
	graph[str(f)].append(s)
	graph[str(s)].append(f)

a = dfs(graph, "1")
print(len(a)-1)
import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n = int(input())



tree = {str(i): [] for i in range(1, n+1)}


ans = {}

def dfs(graph, start, visited=None):
    # 처음엔 none 이니까 visited 를 생성 하고
    if visited is None:
        visited = set()

    visited.add(str(start))

    for i in graph[str(start)]:
        if str(i) not in visited:
            dfs(graph, str(i), visited)
        else:
        	ans[str(start)] = i
    return visited

for i in range(n-1):
	f, s = map(int, input().split())
	tree[str(f)].append(s)
	tree[str(s)].append(f)

dfs(tree, "1")


for i in range(2, n+1):
	print(ans[str(i)])	
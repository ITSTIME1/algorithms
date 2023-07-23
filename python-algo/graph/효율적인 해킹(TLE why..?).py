# 음.. 가장 많은 컴퓨터를 해킹하려면

# 한번의 해킹으로 가장 많이 해킹하려면
# 한번의 해킹을 하는 컴퓨터가 가장 많은 컴퓨터를 가지고 있으면 되는데
# 그럼 1, 2, 4번 컴퓨터는될 수 없어 왜
# 각각 3번의 컴퓨터만 연결되어 있으니까
# 하지만 3번의 컴퓨터는 1, 2, 4, 5랑 연결되어 있기 때문에
# 3번을 해킹함으로써 1, 2, 4, 5번 컴퓨터를 해킹 할 수 있다는거지.
import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 이게 왜 시간초과지 어렵지 않은거 같은데
# 뭐 때문에 왜 시간초과야
n, m = map(int, input().split())



graph = {str(i) : [] for i in range(1, n+1)}


def bfs(graph, root):
    visited = set()

    cnt = 0
    queue = deque([str(root)])
    visited.add(str(root))

    while queue:
        vertex = queue.popleft()
        for v in graph[str(vertex)]:
            if str(v) not in visited:
                visited.add(str(v))
                cnt += 1
                queue.append(str(v))
    return cnt


for i in range(m):
	a, b = map(int, input().split())
	graph[str(b)].append(a)

ans = []

pre = 0
for i in range(1, n+1):
	a = bfs(graph, str(i))
	if a >= pre:
		pre = a
		ans.append(i)
print(*ans) 	


# b를 해킹하면 a를 해킹할 수 있다
# 그럼 반대로 a를 해킹하면 b도 해킹할 수 있다
# 연결되어있다라는걸 가르키는거 같은데..

# 신뢰하는 관계니까 b를 해킹하면 a를 해킹할 수 있게끔 그래프를 구성해주고

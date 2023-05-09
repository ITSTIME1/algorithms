import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n, m, vertex = map(int, input().split())


dic = {}
for i in range(m):
	v, e = map(int, input().split())

	if v not in dic:
		dic[v] = [e]
	else:
		dic[v].append(e)

	if e not in dic:
		dic[e] = [v]
	else:
		dic[e].append(v)


# def dfs(graph, start_node):
# 	n, v = [], []

# 	n.append(start_node)

# 	while n:

# 		node = n.pop()

# 		# 이 노드가 방문하지 않았다면
# 		if node not in v:
# 			v.append(node)

# 			# 그 노드와 연결되어 있는 노드부터 탐색해야되기 떄문에
# 			# 해당 노드와 연결된 인접 노드를 연결
# 			n.extend(graph[node])

# 	# 탐색종료
# 	if len(n) == 0:
# 		return [n, v]


# deque
def dfs2(graph, start_node):
	v = []
	n = deque([])

	n.append(start_node)
	while n:	
		node = n.pop()
		if node not in v:
			v.append(node)

			d = graph[node]
			d.sort(reverse=True)
			n.extend(d)
		else: continue

	print(v)


# recursive dfs

# def recursive_dfs(graph, start, visited=deque()):
# 	visited.append(start)

# 	for node in graph[start]:
# 		if node not in visitied:
# 			recursive_dfs(graph, node, visited)

# 더 간결한거 같은데
# 

def bfs(dic, start):
	visit = []
	non_visit = deque([])


	non_visit.append(start)

	while non_visit:
		node = non_visit.popleft()
		if node not in visit:
			visit.append(node)


			# 이 코드는 해당 정점을 방문한게 있을 수도 있기 때문에
			# 그 인접한 곳은 미리 제외하고
			# 왜냐면 무방향 그래프라면
			# 방향그래프가 아니니까
			# 서로 연결되어 있을 수 있지
			# 그렇게 된다면
			# 중복해서 들어있을 수 있자나
			
			# queue += graph[n] - set(visited)
			d = dic[node]
			d.sort()
			non_visit.extend(d)

	print(visit)



dfs2(dic, vertex)
bfs(dic, vertex)



a = [1,2,3,4]
b = [2,3,3]
a 




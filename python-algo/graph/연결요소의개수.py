import sys
input = sys.stdin.readline
sys.setrecursionlimit(2500)

# 정점과, 간선의 개수를 받음
N, M = map(int, input().split())

# 정점들을 생성할건데
# 정점들을 방문했는지 안했는지를 탐색
vertex = [False] * N
# 그래프 생성
graph = [[0] * N for _ in range(N)]


for _ in range(M):
	# 연결된 정점
	u, v = map(int, input().split())
	# 0, 1
	graph[u-1][v-1] = 1
	graph[v-1][u-1] = 1

# # 그래프를 만들어준다.

def graph_search(root):
	global vertex
	vertex[root] = True

	for node in range(N):
		# graph[0][0.1.2.3.4]
		if graph[root][node] == 1 and not vertex[node]:
			graph[root][node] = 0
			graph[node][root] = 0
			graph_search(node)

	return







# 0~N-1
cnt = 0
for node in range(N):
	# 방문하지 않았다면
	if not vertex[node]:
		# root node 는 0~N-1까지 검사하면서
		# 가장 작은 값을 루트노드로 지정함
		graph_search(node)
		cnt += 1
print(cnt)






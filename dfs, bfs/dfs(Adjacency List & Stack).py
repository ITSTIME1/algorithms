n, m, v = map(int, input().split())

graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
	# 1, 4
	f, t = map(int, input().split())
	# graph[f] 비어있다면 graph[f] = [t]를 넣어주고
	# 만갸 grap[f] = [1] 이런 상태라면
	# 비어있지 않은 관계로graph[f].append(t)
	# 해주면 값이 하나 추가된다
	if graph[f] == []:
		graph[f] = [t]
	else:
		graph[f].append(t)
	if graph[t] == []:
		graph[t] = [f]
	else:
		graph[t].append(f)

def dfs_linked_list(graph, vertex, visited):
	stack = [vertex]
	# == 이건 비교연산자 인데
	# 그니까 visited[vertex] = 처음에 False 값으로 되어 있으니까
	# True 인제 아닌지 확인하고
	while stack:
		value = stack.pop()
		if not visited[value]:
			print(value, end = " ")
			# 이게 할당 연산자를 사용한건데
			# visited[value] = True 를 할당하겠다 이런 의미인데
			visited[value] = True
		# graph[value] 정점에 있는
		# 모든 인접정점을 가지고 와서
		for adj in graph[value]:
			# 그 해당 정점의 인접정점들이 true 가 아니라면
			# stack 에 추가해서 방문해야할 정점들로 쌓아준다
			# 그럼 뒤에서부터 하나씩 뽑게 된다
			if not visited[adj]:
				stack.append(adj)

# 이렇게 되면 인접한 후입 선출해서 나중에 들어온 정점이
# 가장 앞으로 오게 된다
# 문제에서 이걸 작은 번호부터 정렬해달라고 했으니
# sort() 를 ㅆ쓰던가 아니면 reverse() 쓰던가 아니면
# for 문을 한번더 쓰던가 하면 될거 같다.

for i in graph:
	i.reverse()
dfs_linked_list(graph, v, visited)


# 인접리스트 & 재귀


n, m, v = map(int, input().split())
graph = [[]] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  if graph[f] == []:
    graph[f] = [t]
  else:
    graph[f].append(t)
  if graph[t] == []:
    graph[t] = [f]
  else:
    graph[t].append(f)

def dfs(graph, vertex, visited):
  visited[vertex] = True
  print(vertex, end=' ')
  for adj in graph[vertex]:
    if not visited[adj]:
      dfs(graph, j, visited)

# 이것도 같은 값이 나온다
dfs(graph, v, visited)

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

from collections import deque

def bfs(graph, i, visited):
  queue= deque()
  queue.append(i)
  while queue:
    value = queue.popleft()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for j in graph[value]:
        queue.append(j)

bfs(graph, v, visited)

# 인접행렬과 재귀
# 인접행렬을 stack 으로 구현했던 것과 달리
# 재귀로 구현하게 되면 list [] 메모리 만큼을 불필요 하게 된다
# 재귀가 발견 되는 즉시 dfs(1) -> dfs(2) 로 가기 때문에
# 1번 행렬의 조건에 맞는 값을 선순위로 가지를 치고
# 그럼 그 재귀의 정점에 또 다른 가지를 치게되어
# 마지막 재귀서부터 서서히 프로세스가 종료되어 돌아온다.

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)


for _ in range(m):
  f, t = map(int, input().split())
  matrix[f][t] = matrix[t][f] = 1

def dfs(matrix, i, visited):
  visited[i] = True
  print(i, end=' ')
  for c in range(len(matrix[i])):
    if matrix[i][c] == 1 and not visited[c]:
      dfs(matrix, c, visited)
dfs(matrix, v, visited)

# dfs(1) -> dfs(2) -> dfs(4) -> dfs(3) = 마지막 dfs(3) 에서 더 이상 조건에 맞는
# 값이 없으며 dfs 가 종료되어 서서히 역으로 회귀 하게 된다
# 그렇게 된다면 순서대로 print(가 되었으니 값 자체는 1, 2, 4, 3)
# 순으로 나오게 된다
# dfs 나 bfs 이런건 뭔가 상상을 잘 할 수 있어야 하는것 같다

# 뭔가 재밌어..
# 코드량이 현저히 줄고 메모리도 덜 사용하는 재귀를 사용 하는게 훨씬 편리해보이는데


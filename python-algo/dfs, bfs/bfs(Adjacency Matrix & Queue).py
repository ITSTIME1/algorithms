n, m, v = map(int, input().split())

matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)


for _ in range(m):
	f, t = map(int, input().split())
	matrix[f][t] = matrix[t][f] = 1

# Queue 자료 구조를 이용할때
# deque 라이브러리를 사용하는게 좋다
# 큐라는건 먼저 들어온게 그대로 나가는 걸 말한다
# 물 호수를 생각하면 되는데
# 첫 물이 들어오고 나갈때 마지막 물이 나가는게 아닌
# 호수 끝을 통해 처음에 들어온 물이 바로 나가게 된다
# 큐는 그 구조라고 생각하면된다.
from collections import deque

print(matrix)
def bfs(matrix, vertex, visited):
	queue = deque()
	queue.append(vertex)

	while queue:
		# popleft() 함수가 stack 에서 pop()이랑 다른점은
		# pop() 가장 나중에 들어온 값을 뽑는 반면
		# popleft() 가장 처음에 들어온 값부터 뽑는다
		value  = queue.popleft()
		if not visited[value]:
			print(value, end = " ")
			visited[value] = True
			for adj in range(len(matrix[value])):
				# [2,3,4]
				
				# 2 부터
				# 3
				# 4 이런 식으로 나오게 된다 이유는 pop()을 사용하지 않고 popleft()를 사용했기 때문에
				# 가장 왼쪽에 있는 가장 먼저 들어온 2를 먼저 탐색하게 되고
				# 그다음 3을 탐색하고 그다음 4를 탐색하게 된다
				if matrix[value][c] == 1 and not visited[value]:
					queue.append(c)

# [[0, 0, 0, 0, 0],
#  [0, 0, 1, 1, 1],
#  [0, 1, 0, 0, 1],
#  [0, 1, 0, 0, 1],
#  [0, 1, 1, 1, 0]]


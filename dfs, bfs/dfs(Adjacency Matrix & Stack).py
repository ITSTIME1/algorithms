# 백준1260 기준


# 인접행렬과 리스트를 이용해서 dfs 를 구현하는게 목표.
# 문제에 주어진 조건에 따라 코드를 변형시키는 것 까지 목표.

# 우선 정점의 개수가 주어지고 (정점의 개수는 최대 1000까지 주어질 수 있고)
# 간선의 개수는 (최대 10000개까지 주어질 수 있다)
# 그리고 처음 시작할 정점의 숫자를 입력을 받는다
n, m, v = map(int, input().split())

# 정점이 여러개라는 말은 방문해야할 정점이 여러개라는 말을 의미하고
# 방문해야할 정점이 여러개이기 때문에 정점을 작은 순서대로 배열할 수 있는 것이다
# 일단 기본 코드를 작성해보고 그 코드를 좀 더 개선해보고 고쳐보자

# 1. 우선 인접행렬을 만들어주고
# 만약 예제에 인접행렬을 직접주어준다라면
matrix = [[0] * (n+1) for _ in range(m)]

for _ in range(m):
	f, s = map(int, input().split())
	matrix[f][s] = matrix[s][f] = 1

# 1을 체크해주는 이유는 서로 인접행렬이라는것을 표현하기 위함이다
# 만약 가중치 그래프 라면 1이아닌 입력받은 가중치로 입력을 해줘야 문제에 맞게
# 답을 구할 수 있을 것이다

# 그런다음 이제 문제에 요구에 맞게 dfs 를 써야할 곳을 생각해본다
# 우선 이 문제에서 요구하는건 방문 하는 곳을 작은 순서대로 나열해달라는 얘기가 된다
# 그럼 방문을 했다라는 걸 알기 위해서 boolean 변수를 하나 만들어준다

# 왜냐하면 방문한 것을 기억하지 않는다면
visited = [False] * (n+1)

# 우선 인접리스트로 표현을 해보자면
# 우선 stack 에다가 방문을 해야 하는 정점의 번호가 생기게 된다
# 처음엔 정점의 번호가 주어지기 때문에
# 그 정점의 번호가 스택에 저장되어 있게 되고
# 그 정점의 번호를 가지고 와서 해당 정점과 인접한 정점들을 확인해본다
result = []
def dfs(matrix, vertex, visited):
	stack = [vertex]

	while stack:
		value = stack.pop()
		# 방문하지 않았다면
		if not visited[value]:
			visited[value] = True
			# print(value, end = " ")
			result.append(value)

			# 방문하지 않은 정점과 연결된 인접한 정점들을 확인한다
			# 근데 문제의 조건에서 정점이 작은 순서대로 출력해달라고 원하니까
			# stack 의 pop 함수를 활용하면 뒤에서 부터 정점의 번호를 확인한다고 한다면
			# 가장 먼저 들어오는 정점의 번호는 가장 큰 정점의 번호가 될 것이고
			# 그럼 가장 나중에 들어오는 정점의 번호는 가장 빠른 정점의 번호가 될것이기에
			# 가장 빠른 정점의 번호부터 인접한 정점을 확인하게 될 것이다
			for i in range(len(matrix[value])-1, -1, -1):
				# 인접한 행렬이고 방문하지 않았다면 "이것부터 방문하도록 하게 한다"
				if matrix[value][i] == 1 and not visited[c]:
					stack.append(i)

dfs(matrix, v, visited)
print(result)

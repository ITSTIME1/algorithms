# 문제분석

# 순열 사이클의 개수를 구하는 프로그램인데

# 순열이 n개 주어지면 index 1~n 까지 와 주어진순열과 인접행렬을 만들 수 있다

T = int(input())

for _ in range(T):
	n = int(input())
	num = list(map(int, input().split()))
	matrix = [[] * (n+1) for _ in range(n+1)]
	print(matrix)


import itertools


N, M = map(int, input().split())

num = list(itertools.permutations([_ for _ in range(1, N+1)], M))

for i in num:
	print(*i, end = "\n")
	
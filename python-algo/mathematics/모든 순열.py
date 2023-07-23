import itertools

N = int(input())
num = [_ for _ in range(1, N+1)]
arr = list(itertools.permutations(num, N))
for i in arr:
	print(*i)

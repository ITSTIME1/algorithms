from itertools import combinations, permutations
T = int(input())

for _ in range(T):
	N, M = map(int, input().split())
	num = [_ for _ in range(M)]
	combi = list(combinations(num, N))
	print(len(combi))
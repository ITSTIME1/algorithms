import sys

N, K, L = map(int, sys.stdin.readline().rstrip().split())


com = []
count = 0
for _ in range(N):
	f, s, t = map(int, sys.stdin.readline().rstrip().split())
	check = []
	check.append([f, s, t])
	if f >= L and s >= L and t >= L:
		count+=1
		com.append([f, s, t])
	else:
		for i in range(len(check[0])):
			if check[0][i] < L:
				l_in = check[0].index(check[0][i])
				check[0].pop(l_in)	
				if sum(check[0]) >= K:
					count+=1
					com.append([f, s, t])
				else:
					break
			else:
				continue


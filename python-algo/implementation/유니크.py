import sys

N = int(sys.stdin.readline().strip())

pr = [[0 for _ in range(3)] for _ in range(N)]

game = [sys.stdin.readline().strip().split() for _ in range(N)]

# 이런 문제 어렵다...
for i in range(3):
	for j in range(N):
		first = game[j][i]
		cnt = 0 
		for k in range(N):
			if first == game[k][i]:
				cnt+=1 

		if cnt - 1 >= 1:
			pr[j][i] = 0
		elif cnt - 1 == 0:
			pr[j][i] += int(first)
for c in pr:
	print(sum(c), end = "\n")
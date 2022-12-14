import sys

N, D = map(int, sys.stdin.readline().split())
D = str(D)
cnt = 0
for _ in range(1, N+1):
	ch = list(str(_))
	if ch.count(D) >= 1:
		cnt += ch.count(D)


print(cnt) 

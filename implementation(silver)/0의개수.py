import sys
T = int(input())
for i in range(T):
	N, M = map(int, sys.stdin.readline().strip().split())
	zero = 0
	# n2으로하면 1조야 
	for j in range(N, M+1):
		c = list(str(j))
		zero += c.count("0")
	print(zero)


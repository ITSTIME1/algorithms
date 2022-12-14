import sys
for _ in range(int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	num = list(map(int, sys.stdin.readline().split()))
	print(min(num), max(num))
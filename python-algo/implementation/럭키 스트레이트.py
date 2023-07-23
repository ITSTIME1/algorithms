import sys

N = list(map(int, sys.stdin.readline().rstrip()))
div = len(N) // 2

if sum(N[:div]) == sum(N[div:]):
	print("LUCKY")
else:
	print("READY")
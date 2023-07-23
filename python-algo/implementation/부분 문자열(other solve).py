import sys


# 100만 이면 O(nlogn)
S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()


if P in S:
	print(1)
else:
	print(0)



s, p = (input().rstrip() for _ in range(2))
print([0, 1][s.__contains__(p)])
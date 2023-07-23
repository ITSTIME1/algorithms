# set 자료형이 hash table 보다 훨씬 빠르게 동작한다
import sys
n, m = map(int, sys.stdin.readline().strip().split())

dic = {}
nl, ml = set(), set()

for i in range(n+m):
	if i+1 <= n:
		nl.add(sys.stdin.readline().strip())
	else:
		ml.add(sys.stdin.readline().strip())

# 교집합이용
re = sorted(list(nl&ml))
print(len(re))
print(*re, sep="\n")
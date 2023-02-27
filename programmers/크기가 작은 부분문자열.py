import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


t = "10203"

p = "15"
ans = []
for i in range(len(t)):
	a = t[i:i+len(p)]
	if len(a) == len(p):
		ans.append(a)


cnt = 0
for i in ans:
	if int(i) <= int(p):
		cnt += 1

print(cnt)
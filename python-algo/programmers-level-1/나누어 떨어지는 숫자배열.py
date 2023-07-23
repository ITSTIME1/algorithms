import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


arr = [3, 2, 6]
divisor = 10

ans = []
for i in arr:
	if i % divisor == 0:
		ans.append(i)

if len(ans) == 0:
	ans = [-1]
	print(ans)
else:
	ans.sort()
	print(ans)

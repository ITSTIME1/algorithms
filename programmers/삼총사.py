import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



number = [-1, 1, -1, 1]


cnt = 0
for i in combinations(number, 3):
	if sum(i) == 0:
		cnt += 1

print(cnt)
import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


arr = [4, 4, 4, 3, 3]

answer = []
for i in arr:
	if len(answer) == 0:
		answer.append(i)
	else:
		if answer[-1] != i:
			answer.append(i)


print(answer)
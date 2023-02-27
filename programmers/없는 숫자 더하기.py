import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



numbers = [5, 8, 4, 0, 6, 7, 9]
answer = []
for i in range(0, 10):
	if i not in numbers:
		answer.append(i)


print(sum(answer))


import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


left = 24
right = 27


def sol(left):
	total = 0
	for i in range(1, left+1):
		if left % i == 0:
			total += 1
	return total


arr = []
for i in range(left, right+1):
	
	a = sol(i)
	if a % 2 == 0:
		arr.append(i)
	else:
		arr.append(-i)
print(sum(arr))
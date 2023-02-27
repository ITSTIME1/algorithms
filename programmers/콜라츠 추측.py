import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = 626331

index = 0
while n != 1:
	if index >= 500:
		if n != 1:
			index = -1
			break

	if n % 2 == 0:
		n //= 2
		index += 1
	elif n % 2 == 1:
		n = n*3+1
		index += 1

print(index)

import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n, l = map(int, input().split())

fruit = list(map(int, input().split()))

fruit.sort()

deque_list = deque(fruit)





while len(deque_list) != 0:
	c = deque_list.popleft()
	if c <= l:
		l+=1

	elif c > l:
		break


print(l)

import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = 4
a = "수"
b = "박"

answer = ""
if n % 2 == 1:
	for i in range(n):
		if i % 2 == 0:
			answer += a
		else:
			answer += b
else:
	for i in range(n):
		if i % 2 == 0:
			answer += a
		else:
			answer += b
print(answer)
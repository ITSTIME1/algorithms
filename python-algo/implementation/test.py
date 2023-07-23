import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 디펜스게임?

s = [(0, 5), (2, 4), (1, 4), (4, 3), (3, 3), (5, 2), (6, 1)]

for i in s:
	if s.count(i[1]) >= 2:
		print("True")
	else:
		print("False")


pre = 0
for i in s:
	if i[1] != pre:
		k-= 1
	else:
		continue
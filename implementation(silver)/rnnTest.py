import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


arr = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(arr)):
	for j in range(i+1, (i+1)+1):
		print(i, j)  
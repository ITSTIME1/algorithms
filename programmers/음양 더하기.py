import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# true = 참
# false = 거짓

arr = [10]

c = arr.index(min(arr))

del arr[c]

if len(arr) == 0:
	arr = [-1]
else:
	return arr 
import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


arr = deque([1, 2, 3, 4, 5])

arr.popleft()
print(arr)
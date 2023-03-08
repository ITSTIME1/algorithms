import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = 30


arr = [i for i in range(1, n//2+1) if n % i == 0]
arr.append(n)
print(arr)
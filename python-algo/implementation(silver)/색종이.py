import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())

arr = [[0 for i in range(100)] for _ in range(100)]

	
for i in range(n):
	x, y = map(int, input().split())

	for row in range(x-1, (x-1)+10):
		for col in range(y-1, (y-1)+10):
			arr[row][col] = 1

result = 0
for i in arr:
	result += i.count(1)

print(result)
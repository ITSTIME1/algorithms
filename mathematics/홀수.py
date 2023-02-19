# 문제분석
import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


arr = []
for i in range(7):
	num = int(input())
	# 홀수의 합을 결정하고
	if num % 2 != 0:
		arr.append(num)

if arr == 0:
	print(-1)
else:
	print(sum(arr))
	print(min(arr))
	
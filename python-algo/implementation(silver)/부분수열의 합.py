import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 이 문제는 순서를 상관하지 않고
# 조합문제다

n, s = map(int, input().split())

arr = list(map(int, input().split()))


index = n
cnt = 0
while index >= 1:
	for i in combinations(arr, index):
		if sum(list(i)) == s:
			cnt += 1
	index -= 1

print(cnt)
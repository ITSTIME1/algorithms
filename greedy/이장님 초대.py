import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n = int(input())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

for i in range(1, len(arr)+1):
	arr[i-1] = arr[i-1] + i

print(max(arr) + 1)
# 가장 큰숫자 + 1 + 중복된숫자

# 통찰력이있어야

# (4+1) + 2 = 7
# (39+1) + 2 = 42

# 심는일수 + 묘목다 자라는 일수

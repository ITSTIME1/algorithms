import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 그럼 최대한 K에 맞춰서 먹는게 중요하네

# 그럼 p인 사람의 위치에서
# k만큼 뺀 위치가 햄버거라면 먹을 수 있는거니까 cnt += 1
# 만약 k만큼 뺀 위치가 햄버거가 아니라 사람이라면 k+2만큼 더한 곳이 햄버거라면 그걸먹는다

# 음 그럼  2만번..0.5초되나?


# 7 + 1 = 8
# 5 + 2 = 7

# HP 의 개수 + k


n, k = map(int, input().split())

arr = list(map(str, input()))

ans = 0
for i in range(n):
	if arr[i] == "P":
		for j in range(i-k, i+k+1):
			if arr[j] == "H":
				arr[j] = "X"
				ans += 1
				break

print(ans)

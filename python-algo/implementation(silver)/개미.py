import sys
import heapq
import math
import copy
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n1, n2 = map(int, input().split())


one = list(input().strip())
two = list(input().strip())

t = int(input())


one.reverse()

first_set = copy.deepcopy(one)
second_set = copy.deepcopy(two)

# 1. one의 마지막과 두번재에 첫번째가 서로 다른방향이면
# 2. 먼저 바꿔주고 각각 탐색해서 첫번째는 마지막 전까지 두번재는 첫번째 전까지 탐색해서 다른 방향이면 바꿔줌

# O(N*T)
while t > 0:
	if one[len(one)-1] not in second_set and two[0] not in first_set:
		one[len(one)-1], two[0] = two[0], one[len(one)-1]

		for i in range(len(one)-2):
			if one[i] in first_set and one[i+1] not in first_set:
				one[i], one[i+1] = one[i+1], one[i]

		for j in range(len(two)-1, 1, -1):	
			if two[j] in second_set and two[j-1] not in second_set:
				two[j], two[j-1] = two[j-1], two[j]
	else:
		for i in range(len(one)-1):
			if one[i] in first_set and one[i+1] not in first_set:
				one[i], one[i+1] = one[i+1], one[i]

		for j in range(len(two)-1, 0, -1):
			if two[j] in second_set and two[j-1] not in second_set:
				two[j], two[j-1] = two[j-1], two[j]


	t-=1

print("".join(one+two))
import sys
import heapq
from collections import deque
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline


# 참가자 중에 동명이인이 있다

n = int(input())

dic = {}

for i in range(n):
	part = input().strip()
	if part in dic:
		dic[part] += 1
	else:
		dic[part] = 1

for i in range(n-1):
	string = input().strip()
	dic[string] -= 1

ans = ""
for k, v in dic.items():
	if v == 1:
		ans = k
		print(ans)
		break

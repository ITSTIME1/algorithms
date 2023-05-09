import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n, m, vertex = map(int, input().split())

dic = {}


for _ in range(m):
	v, e = map(int, input().split())
	
	if v not in dic:
		dic[v] = [e]
	else:	
		dic[v].append(e)
		
	if e not in dic:
		dic[e] = [v]
	else:
		dic[e].append(v)

print(dic)


def dfsff(dic, start):
	visited = []
	non_visit = deque()

	non_visit.append(start)
	# 방문해야될 필요가 있는 정점이 있다면
	while non_visit:
		node = non_visit.pop()
		if node not in visited:
			print(node, end=" ")
			visited.append(node)
			d = dic[node]
			d.sort(reverse=True)
			non_visit.extend(d)
		else: continue





dfsff(dic, vertex)

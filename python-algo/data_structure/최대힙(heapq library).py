# 문제분석

import heapq
import sys

n = int(sys.stdin.readline().strip())


heap_list = []
for i in range(n):
	x = int(sys.stdin.readline().strip())
	if x == 0:
		# 힙 리스트가 존재한다면
		# 최대값 출력
		# 만약 힙리스트가 없다면 0
		if heap_list:
			print(heapq.heappop(heap_list)[1])
		else:
			print(0)
	else:
		heapq.heappush(heap_list, (-x, x))



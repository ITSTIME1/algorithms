import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 숫자를 중복해서 사용할 수 이쏙
# 숫자를 한개 이상 사용해야되기 때문에
# 1개 보다 작아지면
# 중단

# 뽑는 개수가 1개보다 작아진다면 break




T = int(input())

arr = [1, 2, 3]

ans = []
for i in range(T):
	n = int(input())
	index = n

	cnt = 0
	while index >= 1:
		# 3도 충분히 1을 반복해서 사용할 수 있음
		for i in product(arr, repeat = index):
			if sum(list(i)) == n:	
		
				cnt += 1

		index -= 1
	print(cnt)
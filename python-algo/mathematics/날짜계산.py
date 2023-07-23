import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

e, s, m = map(int, input().split())


init = [1,1,1]

cnt = 1

while True:
	if init[0] == e and init[1] == s and init[2] == m:
		break
		
	init[0] += 1
	init[1] += 1
	init[2] += 1

	if init[0] > 15:
		init[0] = 1
	
	if init[1] > 28:
		init[1] = 1

	if init[2] > 19:
		init[2] = 1

	cnt += 1


	

print(cnt)
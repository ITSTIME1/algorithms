import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


price = 3
money = 20
count = 4

arr = []

for i in range(1, count+1):
	ans = price * i
	
	arr.append(ans)

ans = max(sum(arr), money) - min(sum(arr), money)

if ans == 0:
	answer = 0
else:
	answer = ans

return answer
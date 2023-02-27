import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


array = [1, 5, 2, 6, 3, 7, 4]

commands = [[2,5,3],[4,4,1],[1,7,3]]


answer = []
for i in commands:
	c = i

	i = c[0]
	j = c[1]
	k = c[2]

	re = array[i-1:(j+1)-1]
	re.sort()
	l = re[k-1]
	a.append(l)	
print(a)




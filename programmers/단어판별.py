import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 단어 별로 짝수번째 있는 문자는 upper로 만든다

s = "try hello world"

arr = list(map(str, s.split(" ")))


total = ""
for i in range(len(arr)):
	c = list(arr[i])
	for j in range(len(c)):
		if j % 2 == 0:
			c[j] = c[j].upper()

	if i == len(arr)-1:
		total += "".join(c)
	else:
		total += "".join(c) + " "
print(total)




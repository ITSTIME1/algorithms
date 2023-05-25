
import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


string = list(input())


dic = {}

for i in range(len(string)):
	if string[i] not in dic:
		dic[string[i]] = [i]
	else:
		dic[string[i]].append(i)



ans = 0
for i in string:
	for j in string:
		if dic[i][0] < dic[j][0] and dic[j][0] < dic[i][1] and dic[i][1] < dic[j][1]:
			ans += 1
		else:
			continue

print(ans)
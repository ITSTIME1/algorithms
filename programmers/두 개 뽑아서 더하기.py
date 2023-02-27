import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


numbers = [2,1,3,4,1]


answer = set()
for i in combinations(numbers, 2):
	answer.add(sum(i))


answer_list = list(answer)

answer_list.sort()




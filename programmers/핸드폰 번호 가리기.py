import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


phone_number = "01033334444"

l = len(phone_number)-4

li = list(phone_number)

for i in range(len(phone_number)):
	if i <= l-1:
		li[i] = "*"

print("".join(li))



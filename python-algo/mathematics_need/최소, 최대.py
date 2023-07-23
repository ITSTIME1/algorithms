import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


def gcd(x, y):
	while y:
		x, y = y, x % y
	return x


def lcm(x, y):
	return x*y // gcd(x, y)

print(lcm(1071, 2029))

while True:
	arr.append(lcm(arr.pop(), arr.pop()))
	if len(arr) == 1:
		return arr[0]
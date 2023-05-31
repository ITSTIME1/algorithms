import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

x, y, w, h = map(int, input().split())

one = max(w, x) - min(w, x)
two = y - 0
three = x - 0
four = max(h, y) - min(h, y)

print(min(one, two, three, four))



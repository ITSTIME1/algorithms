# 문제분석

import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n, m = map(int, input().split())


arr = [input().strip() for _ in range(n)]

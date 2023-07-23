import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 길이가 n으로 주어졌을때 얼마만큼의 수박을 출력해야되냐
# n = 2 수박
# n.= 1 수
# n = 3 수박수

n = 1
str = "수박"*n
print(str[:n])
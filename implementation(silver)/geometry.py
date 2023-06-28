import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


box = [[0 for _ in range(10)] for _ in range(10)]

arBox = [[1 for _ in range(4)] for _ in range(4)]
x, y = len(box) // 2, len(box) // 2



curX, curY = len(arBox) / 2, len(arBox)/ 2


resultX = x - curX

resultY = y + curY - 1


a  = 0
def sum(x, y):
	global a
	a = x % 2 ==0 ? x + 2 : y-2


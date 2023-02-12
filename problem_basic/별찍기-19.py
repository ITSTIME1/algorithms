# 문제분석

import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline

def Star(x, y, num):
    if num == 1:
        mat[x][y] = '*'
        return

    div = num // 3

    for i in range (3):
        for j in range (3):
            if i == 1 and j == 1:
                continue
            Star(x + (i * div), y + (j * div), div)

mat = [[" "] * 6561 for i in range(6561)]
N = int(input())

Star(0, 0, N)

for i in range(N):
    Str = []
    for j in range(N):
        Str.append(mat[i][j])
    print("".join(Str))
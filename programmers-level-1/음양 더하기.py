import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


def solution(absolutes, signs):
    total = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            total += absolutes[i]
        else:
            total += -absolutes[i]
    return total
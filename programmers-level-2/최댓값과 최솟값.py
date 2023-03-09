import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

def solution(s):
    s_list = list(map(int, s.split(" ")))
    answer = str(min(s_list)) + " " + str(max(s_list))
    return answer
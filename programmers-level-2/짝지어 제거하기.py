import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

def solution(s):
    answer = -1

    ans = []
    for i in list(s):
        if len(ans) == 0:
            ans.append(i)
            continue
        if len(ans) != 0 and ans[-1] == i:
            ans.pop()
        else:
            ans.append(i)
    if len(ans) != 0:
        answer = 0
    else:
        answer = 1

    return answer
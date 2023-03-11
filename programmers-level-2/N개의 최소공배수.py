import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return x*y // gcd(x, y)


def solution(arr):
    answer = 0

    while len(arr) != 1:
        arr.append(lcm(arr.pop(), arr.pop()))
    
    answer = arr[0]
    
    
    return answer
    
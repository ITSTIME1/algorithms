import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

def solution(A,B):
    answer = 0
    
    # A에서 가장 작은 수 , B에서 가장 큰 수 를뽑으면 가능한거같은데
    
    A.sort(), B.sort(reverse=True)
    
    a_list, b_list = deque(A), deque(B)
    
    while len(a_list) != 0 and len(b_list) != 0:
        minVal, maxVal = a_list.popleft(), b_list.popleft()
        answer += minVal * maxVal        
        
    return answer
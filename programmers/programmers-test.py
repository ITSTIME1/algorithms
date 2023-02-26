import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


def solution(a, b):
    answer = 0
    
    a = []
    if a <= b:
        for i in range(a, b+1):
        	answer += i
    else:
        for i in range(a, b+1):
            answer += i
    
    return answer


a = solution(5, 3)
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.

def soulution(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b+1))



import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

def solution(k, m, score):
    # 최대 점수 최대점수를 어디 다쓰지
    answer = 0
    # 사과를 담을 개수보다 작다면 이익이 발생하지 않지
    if len(score) < m:
        return 0
    # 최대로 먼저 정렬을 해주고
    score.sort(reverse=True)
    # 음 del 자체가 문제였구만
    # for i in range(0, len(score), m):
    #     c = score[i:i+m]
    #     if len(c) >= m:
    #         answer += min(c) * m

    # while len(score) >= m:
    #     c = score[0:m]
    #     answer += c[-1] * len(c)
    # 아 del 이 O(n) 의 시간복잡도를 가지는구나
    #     del score[0:m]
    #     if len(score) < m:
    #         break
   	index = 0
    while True:
    	c = score[index:m]
    	if len(c) >= m:
    		answer += c[-1] * len(c)
    		index+=m
    	else:
    		break
        
    return answer
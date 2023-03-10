import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 아니 너무 어려운데?
# 그리디 너무 안풀다보니까 어떻게 풀어야 할지 아이디어가 자꾸 틀리네;;

def solution(people, limit):
    answer = 0
    # 무게가 초과하면 2개의 보트를 주는것보다
    # 다른 사람을 무게가 더 작은 사람을 태우는게 좋지않을까
    # 50 40 이런 경우는 그냥 1나의 보트에 태워가는거고
    # 50 80 이런 경우는 1명만 태운다면?
    # 큰 사람만 태워보내는거지
#     50 80 +1
#     50 70 +1
#     50 50 +1
    
#     50 70 80
#     50 80 +1
#     50 70 +1
#     50 +1 <- # 모두 태워야하니까
    people.sort()
    p_list = deque(people)
    
    while len(p_list) > 1:
        if p_list[0] + p_list[-1] <= limit:
            answer += 1
            p_list.popleft()
            p_list.pop()
        else:
            p_list.pop()
            answer += 1
    if len(p_list) != 0:
        answer += len(p_list)
    
    
    return answer
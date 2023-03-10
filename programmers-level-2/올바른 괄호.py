import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # 이건 많이 풀어본 문제인데
    # 괄호가 맞으면 그 문자열이 true, false 인지 구하는거니까 어려운건 아닌데.
    ans = []
    for i in list(s):
        if len(ans) == 0 and i == ")":
            answer = False
            break
        
        if i == "(":
            ans.append(i)
        
        else:
            if ans[-1] == "(":
                ans.pop()
    
    if len(ans) != 0:
        answer = False
        
    return answer
        
        
#         if i == "(":
#             ans.append(i)
#         elif i == ")":
#             if len(ans) != 0 and ans[-1] == "(":
#                 ans.pop()
#             elif len(ans) == 0:
#                 answer = False
#                 break
#             else:
#                 answer = False
#                 break
    
    
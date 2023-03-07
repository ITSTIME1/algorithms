import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


def solution(babbling):
    answer = 0
    dic = {"aya": 0, "ye": 0, "woo": 0, "ma": 0}
    
    for i in babbling:
        word = list(i)
        check = []
        pre = ""
        for j in word:
            check.append(j)
            re = "".join(check)
            if re in dic:
                if pre != re:
                    pre = re
                    dic[re] += 1
                    check.clear()
                else:
                    break
        if len(check) != 0:
            continue
        answer += 1
                
        
    
    return answer
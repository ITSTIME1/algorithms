import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


def solution(n, words):
    answer = []
    
    dic = {str(i) : [] for i in range(1, n+1)}
    # 한글자 x
    # 같은 단어 x
    # 이전의 마지막 문자로 시작되지 않으면 x
    
    check_word, index = [], 1
    for i in words:
        if len(i) == 1:
            dic[str(index)].append(i)
            answer = [index, len(dic[str(index)])]
            break
        
        if len(check_word) == 0:
            check_word.append(i)
            dic[str(index)].append(i)
            index += 1
            continue
        else:
            # 중복체크 통과 그리고 끝문자 같다면
            if i not in check_word and check_word[-1][-1] == i[0]:
                check_word.append(i)
                dic[str(index)].append(i)
                index += 1
            elif i not in check_word and check_word[-1][-1] != i[0]:
                dic[str(index)].append(i)
                
                answer = [index, len(dic[str(index)])]
                break
            elif i in check_word:
                dic[str(index)].append(i)
                answer = [index, len(dic[str(index)])]
                break
            
            if index > n:
                index = 1
    if len(check_word) == len(words):
        answer = [0,0]
    return answer
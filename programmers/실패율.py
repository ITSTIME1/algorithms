import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



def solution(N, stages):
    p = len(stages)
    
    # 문제 설명
    # 1. 사람수를 체크할 p를 선언
    # 2. n번까지의 스테이지를 돌면서 현재 i번째 스테이지의 머물고 있는 사람수를 count()함수로 체크
    # 3. c 가 곧 해당 스테이지의 머물고 있는 사람 수기 때문에 그 사람수가 0명이라면 도달한 사람이 없기에 위 제한사항대로 실패율은 0 으로 처리
    # 4. 만약 도달한 사람이 0 명이 아니라면 도달한 사람이 있는 것이기 때문에
    # 실패율을 구하고 이때 해당 스테이지의 도달하게 되면 p는 이전 스테이지의 있는 사람을 제외한 나머지가 되기 때문에 p-=c 연산을 진행 여기서 막혔었는데
    # 만약 1번 스테이지의 머물고 있는 사람이 있다면 2번스테이지에서는 2번스테이지를 머물렀던 사람 + 2번 스테이지의 머물고 있는 사람이기 때문에
    # 1번 스테이지의 머물고 있는 사람은 아직 2번 스테이지를 못왔다
    # 고로 2번스테이지로 넘어 왔을때 1번 스테이지의 사람수 만큼은 제외 해야하기 때문에
    # 이전 스테이지의 머물고 있는 사람들의 수는 제외하게 되면
    # 현재 머물고 있는 사람 수 + 이미 클리어하고 간 사람들 수 가 된다.
    # 그럼 그게 곧 스테이지의 도달한 사람의 수가 되게 된다.
    
    # 마찬가지로 3스테이지로 넘어가게 되면 2번스테이지의 있는 사람은 제외해야 하기 때문에
    # 2번스테이지의 인원수 만큼은 제외하고 3번 스테이지의 도달한 사람수 + 이미 넘어간 사람 수를 하게 된다.
    
    # 5. 그리고 람다로 저장해두어 내림차순으로 정렬을 수행하게 되면서
    # answer = [] 답을 int형으로 저장하고 return 하게 되면서 로직을 종료한다.
    
    
    
    ans = {}
    for i in range(1, N+1):
        c = stages.count(i)
        if c == 0:
            ans[str(i)] = 0
        else:            
            f = c / p
            p-=c
            ans[str(i)] = f
            
    ans_list = sorted(ans.items(), key = lambda x : -x[1])

    answer = []
    for i in ans_list:
	    answer.append(int(i[0]))
        
    return answer
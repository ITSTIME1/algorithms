# import sys
# import heapq
# import math
# from collections import deque
# from itertools import permutations, combinations, product, combinations_with_replacement
# input = sys.stdin.readline


# # 먼저 개발되어야 하는 기능을 나열한건데
# # ㄱ첫번째 기능 같은 경우 93퍼센트 진행했다
# # ㄱ두번째 기능 같은 경우 30퍼센트 진행했다
# # ㄱ세번째 기능 같은 경우 55퍼센트 진행했다

# # 95%가 2일뒤에 배포가가능했듯이
# # 계산을 좀 해보면

# # 첫날에 배포될 수 있는건 존재하지 않아 94, 60, 60
# # 둘째날에 배포될 수 있는것도 존재하지 않아 95, 90, 65
# # 셋째날에 배포될 수 있는것도 존재하지 않아 96, 120, 70 <- 왜냐하면 앞에 기능이 배포될때 같이 배포되기 떄문이지
# # 넷째날에 배포될 수 있는것도 존재하지 않아 97, 120, 75
# # 다섯째날에 배포될 수 있는것도 존재하지 않아 98, 120, 80
# # 여섯째날에 배포될 수 있는것도 존재하지 않아 99, 120, 85
# # 일곱째날에 배포될 수 있는건 존재해 100, 120, 85니까
# # 앞에것이 100퍼센트가 되었기 때문에
# # 100, 120은 배포가 가능 지워주고
# # count += 지워지는 개수
# # 일곱째 2, 1개가 되겠네

# # a:(95, 1)    b:(90, 1)    c:(99, 1)    d    e    f
# # 95,  90,  99,  99,  80,  99
# # 1, 1, 1, 1, 1, 1

# # 1 : 96, 91, 100, 100, 81, 100
# # 2 : 97, 92, 100, 100, 82, 100
# # 3 : 98, 93, 100, 100, 83, 100
# # 4 : 99, 93, 100, 100, 84, 100
# # 5 : 100, 94, 100, 100, 85, 100 <- 다섯째날에 1개 가능
# # 6 : 95, 100, 100, 86, 100
# # 7: 96, 100, 100, 87, 100
# # 8: 97, 100, 100, 88, 100
# # 9: 98, 100, 100, 89, 100
# # 10: 99, 100, 100, 90, 100
# # 11: 100, 100, 100, 91, 100 <- 11번째날에 3개 가능
# # 12: 92, 100
# # 13: 93, 94 95 96 97 98 99 100 <- 2개 

# # 맞네 결국 각 자리에 해당하는 스피드를 고유하게 가지고 있어야하고
# # 리스트에서 제거는 해주되
# # 전부 개발된거는 제거하지 말고 앞에게 제거가 되었다면 제거가 되는 형식으로 구현이 되어야하네

# # 그럼 각각의 고유한 스피드는 dic형태로 지니고 이쏙
# # 키값은 어덯게 괸리할까
# # 음..
# # 저런 상태로 리스트를 만들어둔다면
# [[95, 1], [90, 1]]

# 그럼 while문으로 계속 돌리면서
# 맨 앞에 있는 기능이 100퍼센트가 되었다면
# 그 것으로부터 100인것들까지의 범위를 전부 지워버리고
# 어짜피 리스트에 자기 스피드가 지정이 되어 있으니까
# 지워버리게 되면 그 개수만큼 count만 진행하면 되기 때문에
# 리스트가 전부 사라지기 전까지 전부 돌린다면 가능하겠네

# # 1. [기능, 스피드] 만들어서 check=[]리스트에 삽입
# # 2. while문으로 반복해서 돌면서 자기 스피드를 계속 더함
# # 3. 만약 자기 스피드가 100이상이라면 더 이상 더하지 않고
# # 4. 100 미만인 값들만 자기 스피드를 더함
# # 5. 만약 첫번째 기능의 개발이 100이 되었을때
# # 6. 모든 값에서 100인 기능을 찾음 만약 하나라도 그 다음게 100이 아니라면 그 전까지만 삭제함
# # 7. 그렇게 check에 값이 없을때 까지 반복

import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



def solution(progresses, speeds):
    answer = []
    pro = deque([])
    
    for i in range(len(progresses)):
        pro.append([progresses[i], speeds[i]])
    
    index = 0
    while len(pro) != 0:
        for i in range(len(pro)):
            if pro[i][0] < 100:
                pro[i][0] += pro[i][1]
                
            else: continue
        
        cnt = 0
        if pro[0][0] >= 100:
            for i in range(len(pro)):
                if pro[i][0] >= 100:
                    cnt += 1
                else:
                    break
            
            for i in range(cnt):
                pro.popleft()
            
            if cnt != 0:
                answer.append(cnt)
    
    return answer


pro = list(map(int, input().split(',')))
spd = list(map(int, input().split(',')))

a = solution(pro, spd)



print(*a, sep=",")
import sys
import heapq
from collections import deque
from datetime import datetime
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline




# 1일을 뺐는데 0이 안된다면 그대로 두는거고
# 월수가 12월이 넘어가면 넘어간 수 - 12 뺸 수가 = Month year+=1


# 그럼 해당 날짜가 작은지는 datetime으로 해야겠따


# 이게 런타임이 나는 이유가 뭘까..


def solution(today, terms, privacies):
    # ["2022", "05", "19"]
    # int로 바꿔주어야 계산이 편함
    answer = []
    stand = list(map(int, today.split(".")))
    
    # 달 수 저장
    terms_dic = {}
    for i in terms:
        t = i.split(" ")
        terms_dic[t[0]] = int(t[1])


    for i in range(len(privacies)):
        t = privacies[i].split(" ")
        # [2021, 05, 02]
        date = list(map(int, t[0].split(".")))
        terms_num = t[1]


        year = date[0]
        month = date[1] + terms_dic[terms_num]
        day = date[2]

        # 달수가 12월이 넘어간다면
        # 아 유효기간의 기간이 1이상 100 이하기 때문에 12를 빼더라도
        # 12보다 클 수 있구나 결국엔 12 보다 작을때까지 빼야된다는거네
        # 만약 1월인데 기간이 100달이야
        # 2020.101.01
        # 101이되니까
        # 101-12 = 89 2021
        # 89 - 12 = 77 2022
        # 77-12 = 65 2023
        # 65-12 = 53 2024
        # 53-12 = 41 2025
        # 41-12 = 29 2026
        # 29-12 = 17 2027
        # 17-12 = 5  2028

        # 2028.05.01
        # 12월보다 크다면 13은 1년을 넘어간거고
        # 25는 2년이 된거니까
        # 12달을 뺐는데 아직도 12월보다 크다면 그 만큼 년도도 증가된 상태겠지.

        # 이걸 고려를 못했었네 제한사항 잘읽자;;.
        while month > 12:
            month-=12
            year += 1
        
        day -= 1
        

        if day == 0 and month == 1:
            month = 12
            day = 28
            year -= 1
            continue
            
        elif day == 0 and month != 1:
            month -= 1
            day = 28
            
        # print(year, month, day)


        # 그럼이제 최종본이 나왔으니까
        # 이 유효기간의 날짜가 오늘날짜보다 작은것 들은 보관하면 안돼
        cur_date = datetime(year, month, day)
        stand_date = datetime(stand[0], stand[1], stand[2])

        # 유효기간이 < 오늘날짜보다 작다면 폐기
        if cur_date < stand_date:
            answer.append(i+1)

    return answer

today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]


a = solution(today, terms, privacies)
print(a)
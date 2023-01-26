# 문제분석
# 뭔가 어딘가에 막혀서 잘 아노딘다..

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes = {}
    
    n = int(input())
    for _ in range(n):
        v, k = input().split()
        # 의류 종류가 dict에 없다면 새로 넣어주고, 아니면 원래 있던 의류 종류 키에 대해,
        # set 밸류에 v 추가해주기
        # 아 get 함수로 의상종류가 key값이기 때문에
        # 의상 종류가 없다면 None을 반환하는구나
        # 하지만 이것도 key 를 찾는거라 in 메서드랑 worst case 시간복잡도는 똑같다
        # 하지만 이문제는 dic의 범위가 작기 때문에 in 메서드를 사용해도 큰 문제가 없다
        if clothes.get(k) == None:
            clothes[k] = set()
        clothes[k].add(v)
      
    count = 1
    for key in clothes.keys():
    	count *= len(clothes[key]) + 1
    print(count-1



# 이 문제는 특정 옷을 분류하는데 까지는 성공했는데
# 그 다음 필터링 처리하는 방법을 생각하지 못했다
# 이 코드를 보니 공식화 시켜둔거 같은데
# 이 공식이 어떻게 나온거지 ..
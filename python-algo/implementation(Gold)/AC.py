import sys
from collections import deque
input = sys.stdin.readline

T = int(input())


# 음 배워갈 부분은 있으나
# 빈배열을 출력해야 된다는 부분에서 글쎄..
# 어떻게 유추할 수 있는 부분이 없는거 같은데
# n이 주어지지 않았을때도 error를 출력하고 있고
# n이 주어졌을때 D를 수행했을때도 erorr를 가지고 있기 때문에
# 빈배열이 주어졌다면 = []다? 무슨말이지이게..
# 음 그러면 수가 주어졌는데 빈배열이 주어질 수 있나?
# 그럴 수 없음 배열에 들어 있는 수의 개수라고 했기 때문에
# 배열에 들어있는 수들의 개수를 준거임
# 따라서 0이라는건 배열에 수가 없다라는걸 알 수 있지

for _ in range(T):
    p = input().strip()
    n = int(input())
    # 입력 받는 부분이 이해가 잘 안가는데
    # 왜42를 4, 2로 나눠서 받았을까    
    # 아무리봐도 42를 그렇게 보는건 말이 안되는데
    arr = input().strip()
    arr_list = []
    number = ""
    for i in arr:
        if i == "[" or i == "]":
            continue
        if i.isdigit():
            number += i
        else:
            arr_list.append(int(number))
            number = ""
    
    if number != "":
        arr_list.append(int(number))
        number = ""
    
    
    r_cnt = 0
    arr_list = deque(arr_list)
    answer = "error"
    isActive = True
    for i in p:
        if i == "R":
            r_cnt += 1
        
        else:
            # 수가 있는지 없는지부터 조사좀 해보고
            if len(arr_list) >= 1:
                if r_cnt % 2 == 0:
                    arr_list.popleft()
                else:
                    arr_list.pop()
            else:
                isActive = False
                break
    
    
    # 여기서 에러가 발생한다는 경우는
    # 배열에 수가 존재하지 않는데 D를 수행할 경우 이때가 error가 발생
    # n = 0이라는건 애초에 배열에 들어있는 수 자체가 존재하지 않는다.
    # 배열에 수가 존재하고 D를 수행하려고 하는데 없다면 ERROR
    # 배열에 수가 존재하지 않고 D를 수행하려고 한다면? 
    if r_cnt % 2 == 1:
        # 홀수라면 무조건 처음이랑은 다른 배열상태기 때문에
        arr_list.reverse()
        print(f'[{",".join(list(map(str, arr_list)))}]')
    else:
        print(f'[{",".join(list(map(str, arr_list)))}]')
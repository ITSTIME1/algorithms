from collections import deque
def solution(picks, minerals):
    answer = 0
    
    # 곡갱이에 따라 가중치를 저장해놓고
    dic = {0 : [1, 1, 1], 
           1 : [5, 1, 1], 
           2 : [25, 5, 1]}

    
    # minerals = deque(minerals)
    
    # 광물을 캘 범위는 모든 picks의 합 * 5까지
    # 그게 곡괭이를 가지고 캘 수 있는 끝범위니까
    # 곡괭이가 총 6개가 있다면 광물의 길이가 8이라면
    # 8 // 5 = 1..3
    arr = []
    cnt = sum(picks)
    for i in range(0, len(minerals), 5):
        if cnt == 0:
            break
        arr.append(minerals[i:i+5])
        cnt -= 1

    
    result = []
    for i in arr:
        # 다이아로 전부 캤을때, 철로 전부 캤을대, 돌로 전부 캤을때
        r = [0, 0, 0]
        
        s = i
        for j in s:
            if j == "diamond":
                r[0] += dic[0][0]
                r[1] += dic[1][0]
                r[2] += dic[2][0]
            elif j == "iron":
                r[0] += dic[0][1]
                r[1] += dic[1][1]
                r[2] += dic[2][1]
            else:
                r[0] += dic[0][2]
                r[1] += dic[1][2]
                r[2] += dic[2][2]
                
                
        result.append(r)
        
    # 여기까지 했다는건 돌로 캤을때 비율이 가장 높은순서 돌의 비율이 같다면 철의 비율이 높은순서로
    result.sort(key=lambda x: (-x[2], -x[1], -x[0]))
    result = deque(result)
    
    
    idx = 0
    while True:
        # 광물을 모두 캔 상황이거나 or 괭이가 없어서 캐지 못하는 상황이라면 작업종료
        if not result or picks.count(0) == len(picks):
            break

        if picks[idx] > 0:
            m = result.popleft()

            if idx == 0:
                answer += m[0]
            elif idx == 1:
                answer += m[1]
            else:
                answer += m[2]
            picks[idx] -= 1
        else:
            idx += 1    
        
        

    return answer
                        
                    
            

            

    

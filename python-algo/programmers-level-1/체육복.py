from collections import Counter
def solution(n, lost, reserve):

    dic = Counter(range(1, n+1))
    
    
    # 체육복을 잃어버린 사람
    lost.sort()
    for who in lost:
        dic[who] -= 1
        
        
    # 체육복이 하나더 있는 사람
    for who in reserve:
        dic[who] += 1
        
    
    # 이런 경우는 reserve가 공급해주는 사람인데 공급해주는 사람이 정렬되어 있는 상태로 주어야지
    reserve.sort()
    for i in reserve:
        # 만약 내가 두벌 이상 있고 + 내가 잃어버린 사람이 아니면서 + 내 앞에 사람이 잃어버린 사람이면서 그 사람이 아직 공급받지 못했다면 준다.
        # 그리고 그 사람이 공급해주는 사람이 
        
        # 만약 내가 두벌 이상 있고 내가 잃어버린 사람이라면
        if dic[i] >= 2 and i in lost:
            dic[i]-= 1
            continue
            
        elif dic[i] >= 2 and i - 1 in lost and dic[i-1] == 0 and i not in lost and i-1 not in reserve:
            dic[i-1] += 1
            dic[i] -= 1
            continue
        # 만약 내가 두벌 이상 있고 +  내 뒤에 사람이 잃어버린 사람이면서 + 내가 잃어버리지 않은 사람이면 준다. + 그리고 그 사람이 공급해주는 사람이 아니라면
        elif dic[i] >= 2 and i + 1 in lost and dic[i+1] == 0 and i not in lost and i + 1 not in reserve:
            dic[i+1] += 1
            dic[i] -= 1
            continue     
        
        

    return len([k for k ,v in dic.items() if v >= 1])
    
    


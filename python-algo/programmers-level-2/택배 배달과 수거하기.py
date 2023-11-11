

def solution(cap, n, deliveries, pickups):
    distance = 0
    isActive = False
 
    while isActive == False:

        # 1. 배달해야할 마지막 지점 찾기
        last = n-1
        
        while True:
            if deliveries[last] == 0 and pickups[last] == 0:
                last -= 1
            else:
                distance += (last+1) * 2
                break
        
        # 2. 마지막 지점부터 필요한 박스 찾기
        visited = [False] * n
        needBox = 0
        for i in range(last, -1, -1):
            # 그 지점이 배달해야할 박스가 없지 않고, 그 박스를 더했을때 최대로 실어야 될 것보다 작거나 같다면
            if deliveries[i] != 0 and needBox + deliveries[i] <= cap:
                needBox += deliveries[i]
                visited[i] = True
            else:
                break
                
        # 3. 마지막 지점부터 하나씩 까기
        findHouse = [i for i in range(len(visited)) if visited[i]]
        findHouse.sort(reverse=True)
        for i in findHouse:
            while deliveries[i] != 0:
                deliveries[i] -= 1
                needBox -= 1
        # 수거할 택배
        fullBox = 0
        while fullBox != cap:
            if pickups[last] != 0 and fullBox + pickups[last] <= cap:
                fullBox += pickups[last]
                pickups[last] = 0
                last -= 1
            else:
                if pickups[last] == 0:
                    last -= 1
                    continue
                # 실고 있던 택배에 추가하면 커지는 경우라면
                # 실을 수 있는 만큼만 실자.
                if fullBox + pickups[last] > cap:
                    # 1 , 3 2개까지 실을 수 있자나
                    # 만약 1개고 2개까지 실을 수 있다면 최대 한개까지만 실을 수 있으니까
                    pickups[last] -= (cap - fullBox)
                    fullBox += cap-fullBox
                    last -= 1
        cnt = 0
        for i in range(len(deliveries)):
            if deliveries[i] != 0 and pickups[i] != 0:
                cnt += 1
        
        if cnt == len(deliveries):
            isActive = True 
    return distance
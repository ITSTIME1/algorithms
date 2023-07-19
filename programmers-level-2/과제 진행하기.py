# 41.7점

def solution(plans):
    answer = []
    
    # 생각해보니까
    # 아 과제를 끝낸 시점에 13:30분에는 이전과제만 있기 때문에 이전과제만 진행한다.
    # 그렇기 때문에 현재 가지고온 14시에 시작하는 과제는 잠시 대기항목에 넣어놓는다.
    
    # 이후 computer 과제를 진행하게 되니까
    # 만약 다음 과제를 가지고 왔을때
    # computer과제가 끝나는 시간에
    
    
    for idx, value in enumerate(plans):
        h = int(value[1].split(":")[0])
        m = int(value[1].split(":")[1])
        plans[idx][1] = (h * 60) + m
        plans[idx][2] = int(value[2])
    
    # 시간이 빠른 순서대로 정렬
    plans.sort(key=lambda x : -x[1])
    
    # 진행해야될 과제가 있을때까지
    current = None
    start = 0
    end = 0
    wait = []
    new = []
    while plans:
        p = plans.pop()
        
        # 진행중인 과제가 아직 없다면 현재 가지고 온 과제를 진행시킨다.
        if current is None:
            current  = p
            start = p[1]
            end = start + p[2]
            continue
        
        # 일단 고려해야되는거는
        # 현재 진행하는 과제가 끝나는 시간 전에 진행해야될 과제라면 현재 진행하고 있는 과제는 잠시 멈춰둔다.
        if p[1] < end:
            com = abs(start-p[1])
            current[2] -= com
            wait.append(current)
            current = p
            start = p[1]
            end = start + p[2]
            continue
        
        # 현재 진행하는 과제가 끝나는 시간이거나 또는 이후에 진행될과제라면
        # 즉 진행중이던 과제가 끝났다라는건 end시간이라는거고
        # 근데 새로 가져온 과제가 엔드시간 이후 시간이거나 엔드시간일 수 있자나
        else:
            # 잠시 멈춰둔 과제가 있다면 멈춰둔 과제를 진행하는데
            answer.append(current[0])
            if p[1] > end:
                current = wait.pop()
                start = end
                end = start + current[2]
                # 만약 현재 가지고온 시간이 이전 과제를 끝내기 전에 하게 된다면
                # 그럼 만약에 이전과제를 끝내는 시간안에 새로운 과제를 하는시간이 되면 이렇게 계산하면 되겠지만
                # 이전 과제를 끝내는 시간 밖이라면
                # 생각해보니까 미리 꺼내지 않아도 되자나
                # 그냥 만약에 sc- >com 넘어가는것처럼
                # 만약 end 보다 넘어간다면 가져오지 않고 이전거 하면되고
                # 그다음에 가져왔을때 이렇게 하면 되겠네
                if p[1] < end:
                    current[2] -= abs(p[1] - start)
                    wait.append(current)
                    current = p
                    start = p[1]
                    end = start + p[2]
                    continue
                
            elif p[1] == end:
                # 이런경우 끝나는 시각이 되었을때 wait도 있다면
                if wait:
                    current = p
                    start = p[1]
                    end = start + p[2]
                    continue
                    
                else:
                    # 만약에 wait이 없으면 대기중인 과제가 없다는거니까 새로 시작하는 과제를 하면되자나
                    current = p
                    start = p[1]
                    end = start + p[2]
                    continue
                    
    
    # 그럼 마지막에 current현재 진행중인 과제가 종료 될거니까
    if current is not None:
        wait.append(current)
        for idx in range(len(wait)-1, -1, -1):
            answer.append(wait[idx][0])
    # if current is not None:
    return answer








# 66.7점
def solution(plans):
    answer = []
    
    # 생각해보니까
    # 아 과제를 끝낸 시점에 13:30분에는 이전과제만 있기 때문에 이전과제만 진행한다.
    # 그렇기 때문에 현재 가지고온 14시에 시작하는 과제는 잠시 대기항목에 넣어놓는다.
    
    # 이후 computer 과제를 진행하게 되니까
    # 만약 다음 과제를 가지고 왔을때
    # computer과제가 끝나는 시간에
    
    
    for idx, value in enumerate(plans):
        h = int(value[1].split(":")[0])
        m = int(value[1].split(":")[1])
        plans[idx][1] = (h * 60) + m
        plans[idx][2] = int(value[2])
    
    # 시간이 빠른 순서대로 정렬
    plans.sort(key=lambda x : -x[1])
    
    # 진행해야될 과제가 있을때까지
    current = None
    start = 0
    end = 0
    wait = []
    # 일단 처음부터 가져오지 않고 정렬되어 있는것부터 가져오면 되는거지
    while plans:
        p = plans[-1]
        
        # 현재 진행중인 과제가 없으면 진행한다.
        if current is None:
            plans.pop()
            current = p
            start = current[1]
            end = start + p[2]
            continue
            
        # 현재 진행중인 과제가 있다면
        # 진행중인 과제를 가지고 왔을때 현재 진행중인 과제가 끝나는 시간 안에 있어 새로운 과제를 진행해야 될때
        if p[1] < end:
            plans.pop()
            com = abs(start - p[1])
            current[2] -= com
            wait.append(current)
            current = p
            start = p[1]
            end = start + p[2]
            continue
        else:
            # 이건 p[1] >= end 인 상황이니까
            # p[1] == end
            # p[1] > end
            # 즉 과제가 끝냈을때 멈춘 과제가 있다면
            # 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 있다면 새로 시작하는 과제부터 진행한다.
            answer.append(current[0])
            if p[1] == end:
                if wait:
                    plans.pop()
                    current = p
                    start = p[1]
                    end = start + p[2]
                    continue
                # 대기 목록이 없으면 현재과제를 진행하면된다.
                else:
                    plans.pop()
                    current = p
                    start = p[1]
                    end = start + p[2]
                    continue
                    
            else:
                # 이건 과제는 끝났지만 다음 과제가 시작시간이 아닐때
                # 멈춰둔 과제를 이어서 진행한다.
                current = wait.pop()
                start = end
                end = start + current[2]
                continue
    
    if current is not None:
        wait.append(current)
        for idx in range(len(wait)-1, -1, -1):
            answer.append(wait[idx][0])
    
    return answer
        
    
    
    
    


# 100점
def solution(plans):
    answer = []
    
    # 생각해보니까
    # 아 과제를 끝낸 시점에 13:30분에는 이전과제만 있기 때문에 이전과제만 진행한다.
    # 그렇기 때문에 현재 가지고온 14시에 시작하는 과제는 잠시 대기항목에 넣어놓는다.
    
    # 이후 computer 과제를 진행하게 되니까
    # 만약 다음 과제를 가지고 왔을때
    # computer과제가 끝나는 시간에
    
    
    for idx, value in enumerate(plans):
        h = int(value[1].split(":")[0])
        m = int(value[1].split(":")[1])
        plans[idx][1] = (h * 60) + m
        plans[idx][2] = int(value[2])
    
    # 시간이 빠른 순서대로 정렬
    plans.sort(key=lambda x : -x[1])
    
    # 진행해야될 과제가 있을때까지
    current = None
    start = 0
    end = 0
    wait = []
    # 일단 처음부터 가져오지 않고 정렬되어 있는것부터 가져오면 되는거지
    while plans:
        p = plans[-1]
        
        # 현재 진행중인 과제가 없으면 진행한다.
        if current is None:
            plans.pop()
            current = p
            start = current[1]
            end = start + p[2]
            continue
            
        # 현재 진행중인 과제가 있다면
        # 진행중인 과제를 가지고 왔을때 현재 진행중인 과제가 끝나는 시간 안에 있어 새로운 과제를 진행해야 될때
        if p[1] < end:
            plans.pop()
            com = abs(start - p[1])
            current[2] -= com
            wait.append(current)
            current = p
            start = p[1]
            end = start + p[2]
            continue
        else:
            answer.append(current[0])
            # 만약
            # 진행중이던 과제를 끝냈을때 잠시 멈춘 과제가 있다면
            # 멈춰둔 과제를 진행한다.
            if p[1] == end:
                
                if wait:
                    current = plans.pop()
                    start = current[1]
                    end = start + current[2]
                    continue
                # 만약에 과제를 끝낸 시각에 새로 시작해야 되는과제만 있고
                # 진행중인 과제가 없다면 새로 시작해야되는 과제를 하면되는거지
                else:
                    current = plans.pop()
                    start = current[1]
                    end = start + current[2]
                    continue
                    
            else:

                # 만약에 과제를 끝냈을때 잠시 멈춘 과제가 있다면 멈춰둔 과제를 이어서 진행한다.
                if wait:
                    current = wait.pop()
                    start = end
                    end = start + current[2]
                    continue
                # 만약에 과제를 끝냈을때 잠시 멈춘 과제가 없다면 현재 과제로 진행한다.
                else:
                    current = plans.pop()
                    start = current[1]
                    end = start + current[2]
                    continue
            
                    
    
    if current is not None:
        wait.append(current)
        for idx in range(len(wait)-1, -1, -1):
            answer.append(wait[idx][0])
    
    return answer
        
    
from collections import deque
def solution(book_time):
    answer = 0

    for idx, value in enumerate(book_time):
        start, end = value[0], value[1]
            
        # 분으로 전부 통일해서 변경 해준다.
        book_time[idx][0] = (int(start.split(":")[0]) * 60) + int(start.split(":")[1])
        book_time[idx][1] = (int(end.split(":")[0]) * 60) + int(end.split(":")[1])
        
        
    book_time.sort(key=lambda x : x[0])
    book_time = deque(book_time)
    
    table = {}
    idx = 0
    
    while book_time:
        re = book_time.popleft()
        
        if len(table) == 0:
            table[idx] = [re]
            idx += 1
            continue
            
        for key, value in table.items():
            time = value[-1]
            # 근데 들어갈 수 없는 조건을 어떻게 판딴할까
            # 만약 종료시간보다 작다면 못들어가는거지 종료를 안했으니까
            # 이러면 들어갈 수 있찌
            if re[0] >= time[1] + 10:            
                table[key].append(re)
            else:
                table[idx] = [re]
                idx += 1
    print(table)

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])
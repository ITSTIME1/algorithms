import math
    
def solution(fees, records):
    answer = []
    
    master_time = (23 * 60) + 59
    
    for i in range(len(records)):
        sep = records[i].split(" ")

        h, m = sep[0].split(":")[0], sep[0].split(":")[1]
        time = (int(h) * 60) + int(m)
        sep[0] = time
        records[i] = sep

        
    records.sort(key=lambda x : x[1])
    
    
    table = {}

    for car in records:
        if car[1] not in table:
            # 입차시간, 퇴차시간, 차량상태, 누적시간 

            table[car[1]] = [car[0], 0, car[2], 0]
        else:

            if table[car[1]][2] == "OUT":
                table[car[1]][2] = "IN"
                table[car[1]][0] = car[0]
                
            # 이경우는 두번째에 들어왔을때 IN이라면 출차를 한것이므로
            elif table[car[1]][2] == "IN":
                table[car[1]][1] = car[0]
                table[car[1]][2] = "OUT"
            
                table[car[1]][3] += abs(int(table[car[1]][1]) - int(table[car[1]][0]))


    for key, value in table.items():
        # 아직까지도 차량이 존재한다면
        if value[2] == "IN":
            remain = master_time - value[0]
            value[3] += remain
        

        if value[3] > fees[0]:
            if (value[3] - fees[0]) / fees[2] != 0:
                ce = (value[3] - fees[0]) / fees[2]
                cal = fees[1] + math.ceil(ce) * fees[3]
                answer.append(cal)
            else:
                cal = fees[1] + ((value[3] - fees[0]) / fees[2]) * fees[3]
                answer.append(cal)
        else:
            answer.append(fees[1])
    
    return answer
            
        
    
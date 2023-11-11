def solution(data, col, row_begin, row_end):
    
    # 오케이 무슨소리인지는 알겠어
    
    # 1. col번째 칼람을 기주능로 정렬하자
    sorted_col = sorted(data, key=lambda x:(x[col-1], -x[0]))
    
    # 2. 정렬된 데이터에서 i번째 값들을 i로 나눈 나머지로 바꾼다.
    bit_list = []
    for i in range(len(sorted_col)):
        s_i = 0
        for j in range(len(sorted_col[0])):
            s_i += sorted_col[i][j] % (i+1)
            
        bit_list.append(s_i)

    # 3. bitwise
    answer = bit_list[0]
    for i in range(row_begin-1, row_end):
        answer = answer ^ bit_list[i]
    
    return answer
                
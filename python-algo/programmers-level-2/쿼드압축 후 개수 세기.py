def recursive(arr, x, y, p, answer):
    
    # 그럼 일단 모두 같다는건 현재 숫자오 ㅏ모두 같다는거지
    # 현재 숫자와 모두 같으면 압축 할 수 있다는거니까
    check = arr[x][y]
    for r in range(x, x+p):
        for c in range(y, y+p):
            # 일단 숫자가 하나라도 다르다면
            if arr[r][c] != check:
                # 또 분할해야되니까
                p//=2
                recursive(arr, x, y, p, answer)
                recursive(arr, x+p, y, p, answer)
                recursive(arr, x, y+p, p, answer)
                recursive(arr, x+p, y+p, p, answer)
                # 갖아 작은 부분까지 내려 왔다면
                # 끄 작은 부분들을 전부다 각각의 값에서 올려준다음에
                # return 
                return
            
    # 압축이 되낟면 그 처음 값을 하나 올릴거고
    # 하나로 전부다 쪼개졌을때도
    # x, y가 해당 좌표가 될테니까
    # 그 좌표의 값을 하나씩 증가시켜주고
    answer[check] += 1



def solution(arr):
    # zero, one
    answer = [0, 0]
    p = len(arr)
    x, y = 0, 0 

    recursive(arr, x, y, p, answer)
    
    return answer
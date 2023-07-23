def simul(board, i, j, n):
    dx = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for idx in range(8):
        nx = dx[idx][0] + i
        ny = dx[idx][1] + j
        
        # 범위를 넘어가거나 또는 이미 x처리 된 부분이 있다면 넘어간다.
        # x는 지뢰에 인접한 지역이기 때문에 따로 처리해서 두번 방문하지 않도록
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == "X" or board[nx][ny] == 1:
            continue
        
        board[nx][ny] = "X"
    
    board[i][j] = "X"
    return board
    

def solution(board):
    n = len(board)

    for i in range(n):
        for j in range(n):
            # 지뢰가 매설된 지역
            if board[i][j] == 1:
                board = simul(board, i, j, n)
            
    
    return sum([1 for i in range(n) for j in range(n) if board[i][j] == 0])


# [[0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0], 
#  [0, ㅌ, ㅌ, ㅌ, ㅌ], 
#  [0, ㅌ, ㅌ, ㅌ, ㅌ], 
#  [0, ㅌ, ㅌ, ㅌ, ㅌ]]

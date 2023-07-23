N, M = map(int, input().split())

board = [list(map(str, input())) for _ in range(N)]


for i in range(N-7):
    for j in range(M-7):
        white, black = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                # 짝수이면서 first 값이 B인거
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        black+=1
                    elif board[a][b] != "W":
                        white+=1
                else:
                    if board[a][b] != "B":
                        black+=1
                    elif board[a][b] != "W":
                        white+=1

        print(white, black)






                
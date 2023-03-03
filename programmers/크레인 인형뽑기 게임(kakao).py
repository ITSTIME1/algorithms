from collections import deque


def game(number, board):
    # 음 정사각 격자라고 하네
    m = len(board)
    isActive = True
    
    # number = 5
    ans = 0
    for i in range(1):
        for j in range(m):
            if board[j][number-1] != 0:
                # 뽑았다고 가정하고
                ans = board[j][number-1]
                board[j][number-1] = 0
                isActive = False
                break
        if isActive == False:
            break
    
    return [ans, board]
    


def solution(board, moves):
    answer = 0
    bd = board
    md = deque(moves)
    stack = []
    while len(md) != 0:
        num = md.popleft()
        # game에서 리턴한걸
        c = game(num, bd)
        # board 판을 업데이트해주고
        bd = c[1]
        
        # 빈칸이면 패스
        if c[0] == 0:
            bd = c[1]
            continue
        
        # 그 값을 stack에 넣어줄거야
        # 뽑을게 없을땐 0이 들어오니까
        # 그럼 아무상태도 아닌데 0을 넣을 순 없자나
        if len(stack) == 0 and c[0] != 0:
            stack.append(c[0])
            continue
        # 같은 인형이라면
        elif stack[-1] == c[0]:
            stack.pop()
            answer += 2
        else:
            stack.append(c[0])
        
    return answer
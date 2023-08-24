def solution(n):
    answer = []
    # 원반의 개수 , 시작 , 목표, 보조
    # 처음엔 n개에다가, 1, 3, 2
    def hanoi(n, start, goal, middel):
        # 원반의 개수가 한개면 바로 도착지점으로 보내고
        if n == 1: 
            answer.append([start+1, goal+1])
            return
            
        # 원반의 개수가 한개가 아니라면 재귀를 타서 
        # 2, 0 1 2
        # 1, 0 2 1 시작 0에서 목표 2로 이동 함수종료
        # 그다음에 거 이동시키면 시작에서 0 목표지점 1로 이동
        hanoi(n-1, start, middel, goal)
        answer.append([start+1, goal+1])
        hanoi(n-1, middel, goal, start)
            
    hanoi(n, 0, 2, 1)
    return answer
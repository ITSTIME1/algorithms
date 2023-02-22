import sys

N = int(input())
candidates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
def earn(day, money):
    global answer
    answer = max(answer, money)
    if day >= N: return

    if day + candidates[day][0] <= N:
        earn(day + candidates[day][0], money + candidates[day][1])
        earn(day + 1, money)
    else:
        earn(day + 1, money)
    return

earn(0, 0)
print(answer)

# 이 알고리즘의 동작방식


# 우선 재귀로 시작한다
# 우선 한날짜부터 시작해서
# 탐색을 진행하는데
# 처음날짜부터 탐색을 진행하고
# 만약 그 해당날짜가 탐색이 진행이 된다면 해당날짜 + 상담이 걸리는 날짜로 넘어간다
# 그랬을때 그 상담날짜도 또한 상담이가능하다면 계속해서 상담이 가능한 상태로 넘어가고
# 넘어가는 상태에서 계속해서 money 를 최대값으로 업데이트해준다
# 여기서 중요한건 만약 해당날짜에 수업이 불가능하다면 해당날짜 + 1를 해서
# 가능한 날짜를 찾는 작업이 필요하고
# 만약 상담할 수 있는 날짜가 N+1일은 퇴사라 못하니 N까지는 상담이 가능하다는얘기
# 그럼 현재 날짜 + 상담에 걸리는 날짜 <= N 보다 작을떄까지는 상담이 가능하다는 얘기니까
# 해당 날짜 까지는 상담을 진행해주고
# 해당 날짜가 넘어 간다면 퇴사일이라 상담을 진행하지 못하므로 기저조건에 return을 걸어준다
# 그리고 상담을 하다가 + 1일씩 증가하면서 가능한 날짜를 찾는데 더 이상 가능한 날짜가 없으면 return 하게 한다
# 상담을

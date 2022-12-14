# 정방형 2차원 배열을 가정하고 한다.
# 90도 회전
# 회전후의 행은 증가하는 모습을 볼 수 있고 그 증가폭은 바깥 배열이 한번 돌때
# 열 부분이 N 만큼 도는 크기와 같다.
# 회전후의 열은 모두 같은 숫자로 통일 되어 있는데 그것은
# N-1 만큼과 같지만 

# 오른쪽으로 즉 시계 방향으로 회전하는 배열
# 왼쪽으로 회전하는 배열을 만들어보자
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

test = [[1,2,3], [4,5,6], [7,8,9]]
print(rotate_90(test))

# 180도 회전
def rotate_180(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[N-1-r][N-1-c] = m[r][c]
    return ret
print(rotate_180(test))

def rotate_270(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[N-1-c][r] = m[r][c]

    return ret
print(rotate_270(test))

# 360도 = 원배열과 같은 배열이기 때문에
# 할 필요가 없다 만약 360도 까지 한 횟수를 카운트 하라고 하면
# 90 180 270 총 세번의 카운트와 360도를 했다는 즉 원배열까지 도달했다는 cnt += 1을 하게 되면
# 360도까지 총 몇번의 회전을 했냐라는 질문에 답할 수 있게 된다.


# 이 함수는 원배열을 입력받고 몇 도 회전할 건지 입력받아 배열을 돌리는 방식이다
# 위의 모든 함수가 따 짜여져 있는 것이다.
# ㅇㅇ
def rotate(m, d):
    """2차원 배열을 90도 단위로 회전해 반환한다.
       이때 원 배열은 유지되며, 새로운 배열이 탄생한다. 이는 회전이 360도 단위일 때도 해당한다.
       2차원 배열은 행과 열의 수가 같은 정방형 배열이어야 한다.

       :input:
       m: 회전하고자 하는 2차원 배열. 입력이 정방형 행렬이라고 가정한다.
       d: 90도씩의 회전 단위. -1: -90도, 1: 90도, 2: 180도, ...
    """
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][N-1-r] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    # 사실상 이 경우는 그냥 0 인 경우 원배열인 경우기 때문에
    # 바로 그냥 원 배열을 리턴해주는 것도 하나의 방법일 것 같다 
    else:
        for r in range(N):
            for c in range(N):
                ret[r][c] = m[r][c]
    return ret
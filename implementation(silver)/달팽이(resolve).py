# 이 문제는 2차원 리스트를 탐색하면서 가는 문제다.

# 원소index: (x, y)
# 상 index: (x-1, y)
# 하 index: (x+1, y)
# 좌 index: (x, y-1)
# 우 index: (x, y+1)
arr = [[1,2,3], [4,5,6], [7,8,9]]

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return retr
print(rotate_90(arr))
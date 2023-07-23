import sys

for _ in range(int(input())):
    m, n = map(int, sys.stdin.readline().strip().split())
    arr = [sys.stdin.readline().strip().split() for _ in range(m)]
    cnt = 0
    last_box = m-1
    for i in range(n):
        # 거꾸로 탐색시작 하고
        not_box_count = 0
        for k in range(m-1, -1, -1):
            # 박스가 있다면
            if arr[k][i] == "1":
                cnt += not_box_count
            # 박스가 없다면
            else:
                not_box_count += 1
    print(cnt)

# 5 4
# 1 0 0 0
# 0 0 1 0
# 1 0 0 1
# 0 1 0 0
# 1 0 1 0
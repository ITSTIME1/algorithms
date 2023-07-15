import sys
input = sys.stdin.readline


# 0, 소프트웨어
# 1, 임베디드
# 2, 인공지능
score = [0] * 3


# 2학년 학생들만 구하면되는거자나
# 1학년 학생들은 따로 구하고
p = int(input())

arr = [list(map(int, input().split())) for _ in range(p)]



for i in arr:
    s = i
    # 2학년만 선별
    if s[0] != 1:
        # 소프트웨어
        if s[1] == 1 or s[1] == 2:
            score[0] += 1
        
        # 임베드디
        elif s[1] == 3:
        
            score[1] += 1
        # 인공지능
        else:
            score[2] += 1


score.append(p-sum(score))

for i in score:
    print(i)
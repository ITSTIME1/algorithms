# 1 1
# 2 2 3
# 3 4 5 6
# 4 7 8 9 10
# 5 11 12 13 14 15
# 6 16 17 18 19 20 21


# 1 1
# 2 2 3
# 3 4 5 6 7
# 4 8 9 10 11 12 13 14 15
# 5 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31

T = int(input())
p1 = [500, 300, 200, 50, 30, 10]
p2 = [512, 256, 128, 64, 32]

def firstFestival(a):
    
    # 분배된 인원수
    s1 = [1, 2, 3, 4, 5, 6]
    pr = 0
    result = 0
    f = sum(s1)
    if f < a or a == 0:
        pr = '0'
    else:
        for j in range(len(s1)):
            result += s1[j]
            if a <= result:
                pr = s1[j]
                break
        # 포함되어 있는 범위를 반환
        return pr
    return pr

def secondFestival(b):
    # 19
    s2 = [1, 2, 4, 8, 16]
    pr2 = 0
    result2 = 0
    f1 = sum(s2)
    if f1 < b or b == 0:
        pr2 = '0'
    else:
        for k in range(len(s2)):
            result2 += s2[k]
            if b <= result2:
                pr2 = k+1
                break
        # 포함되어 있는 범위를 반환
        return pr2
    return pr2

for _ in range(T):
    a, b = map(int, input().split())
    c = firstFestival(a)
    d = secondFestival(b)
    if c == '0' and d != '0':
        print(p2[d-1]*10000)
    elif c != '0' and d == '0':
        print(p1[c-1]*10000)
    elif c == '0' and d == '0':
        print(0)
    else:
        print((p1[c-1]+p2[d-1])*10000)

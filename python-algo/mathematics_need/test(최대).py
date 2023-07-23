# def gcd(a, b):
#     for i in range(min(a, b), 0, -1):
#         print(i)
#         if a % i == 0 and b % i == 0:
#             return i
# print(gcd(8, 16))

def gcd1(a, b):
    if a < b:
        min = a
    else:
        min = b
    res = 0
    # min+1 이나 min 이나 최대 공약수는 가장 큰 수 부터 -1씩 감소 시키면서
    # 가기 때문에 상관없다
    for i in range(min+1, 1, -1):
        if a % i == 0 and b % i == 0:
            res = i
            break
    return res
print(gcd1(8, 16))
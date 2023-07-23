
# import sys
# input = sys.stdin.readline

# n = int(input())
# ans = 1

# start = ["1"]


# dic = {}
# result = ['1']
# while ans <= n:
#     for i in start:
#         a = list(i)
#         for j in a:
#             if j not in dic:
#                 dic[j] = 1     
#             else:
#                 dic[j] += 1
    
#     start.clear()
    
#     answer = ""
#     for k, v in dic.items():
#         answer += str(k) + str(v)
    
#     result.append(answer)
    
    
#     start.append(answer)
#     ans += 1       
#     dic = {}

# answer = []

# start = list(map(str, result))
# cha = list(map(int, start[n-1]))

# print(cha)

# print(max(cha))

# a = ["11"]

# s = []
# for i in a:
#     print(list(i))

def ant_sequence(n):
    if n == 1:
        return 1

    sequence = "1"
    for _ in range(n - 1):
        count = 1
        next_sequence = ""
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
            else:
                next_sequence += str(count) + sequence[i - 1]
                count = 1
        next_sequence += str(count) + sequence[-1]
        print(next_sequence)
        sequence = next_sequence

    max_digit = max(sequence)
    return int(max_digit)

# 입력 받기
n = int(input())

# 개미 수열의 N번째 항의 자릿수 중 가장 큰 수 계산
result = ant_sequence(n)

# 결과 출력
print(result)
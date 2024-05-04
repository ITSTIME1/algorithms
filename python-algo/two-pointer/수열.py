import sys
input = sys.stdin.readline

# n개의 수열, k일
n, k = map(int, input().split())
num = list(map(int, input().split()))
# n은 최대 10만
# 1 < k < 10만
# max_number = 0
# for i in range(n - k + 1):
#     s = num[i:i+k] # O(k)
#     max_number = max(sum(s), max_number) O(n)
# print(max_number)

start, end = 0, 0
# a = 0
# a = []
# number = 0
# while start < n - k + 1:   
#     # k가 되지 않았다면, number에 k를 계속 더해나간다.
#     if end - start + 1 != k:
#         number += num[end]
#         end += 1
#     else:
#         number+=num[end]
#         a.append(number)
#         number -= num[start]
#         start += 1
#         end += 1
        
        
        
# print(max(a))
    

a = []        
number = 0
# 조금더 최적화를 해보면
# max_number가 0으로 두면 안되는거 같은데
# 만약에 전부다 작은 값들이 다 음수라고 한다면, 이게 반례가 될 수 있네
# 그러면 0이 큰 값이 되기 때문에, 문제가 되는거지.
# 그러면 최소 -100부터 시작해야겠네
# 합쳤을때 -100 아래로 내려갈 수 있으니까
# 가장 작은 값을 무엇으로 설정해야 할까.
# -100으로만 구성되어 있으면 가장 작은게 되므로
# -100이 몇개가 있을때 가장 작을까?
# 그럼 날짜의 길이가 가장 킬면서 -100으로만 채워졌을때, 가장 작게 될테니까
# -100 * k 음
# 맞지.
max_number = -100 * k
while end < n:
    number += num[end]
    
    if end - start + 1 == k:
        max_number = max(max_number, number)
        number -= num[start]
        start += 1
    end += 1
    
print(max_number)
# 수들이 -100 ~ 100 사이로 주어진다고 했는데
# 음수 + 음수 = 음수
# 음수 + 양수 = 음수 -12, 3
# 양수 + 음수 = 양수 3, -12
# 양수 + 양수 = 양수


input_list = list(map(int, input().split()))

H = int(input_list[0])
M = int(input_list[1])

time = int(input()) # 80

H += time // 60 # 몫
M += time % 60 # 나머지


# 시간은 60 이상이면 시간을 더해주고
# 분에서 - 60을 빼준다.
if(M >= 60):
  H += 1
  M -= 60

if(H >= 24):
  H -= 24

print(H, M)
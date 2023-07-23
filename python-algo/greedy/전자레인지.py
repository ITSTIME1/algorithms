# Time = 1000 이라고 했을때
# A, B, C = 5분, 1분, 10분

# Time = 100
# 

# 초단위 100초
# 분 => 초 300초, 60초, 10초
Time = int(input())
time_list = [300, 60, 10]
result = 0
result_list = []

for i in time_list:
  result = Time // int(i)
  result_list.append(result)
  Time = Time%int(i)



if(Time % 10 != 0 ):
  print("-1")
else:
  print(*result_list)
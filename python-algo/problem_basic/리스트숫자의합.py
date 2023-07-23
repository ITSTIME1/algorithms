number_value = int(input())
# 쪼개서 받기
list_value = list(input())
result = 0

def solution(number_value, list_value):
  global result
  for i in range(number_value):
    result += int(list_value[i])



solution(number_value, list_value)
print(result)

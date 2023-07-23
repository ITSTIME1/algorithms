

people = int(input())
people_time = list(map(int, input().split()))
result = 0
result_list = []
answer_list = []

# Solution 2
# for i in range(people):
#   people_time.sort()
#   result += people_time[i]
#   result_list.append(result)
#   if(len(result_list) <= people):
#     answer_list = sum(result_list)
# print(answer_list)

# Solution 1 runTimeError 나긴 하지만 맞는 답
def solution(people, people_time):
  global result;
  global result_list;
  global answer_list;
  for i in range(people):
    people_time.sort()
    result += people_time[i]
    result_list.append(result)
    if(len(result_list) <= people):
      answer_list = sum(result_list)
  print(answer_list)

solution(people, people_time)

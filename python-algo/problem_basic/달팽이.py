# 낮에 올라가는 a
# 밤에 미끄러지는게 b
# 막대의 길이가 v

# 달팽이가 하루동안 올라간 길이 = 낮에 올라가는 길이 (a) - 밤에 미끄러지는 길이 (b)

# 달팽이가 하루 (1) 올라가기 시작했을때
# 아침에 (2) 밤에(1) = 1 = 그 날의 올라간 길이
# 그 날의 길이가 v와 같아지는 시점이 바로 다 올라간 길이

# 막대 6 아침에 5 밤에 1
# 0 4 
# 1 4
# result <= v
import sys
import math

a, b, v = map(int,sys.stdin.readline().split())


def solution(a,b,v):
  answer = math.ceil((v-b)/(a-b))

  print(answer)

solution(a,b,v)
  
  
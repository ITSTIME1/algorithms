# 반올림 함수 직접 만들기
# round 함수는 보통 실수형 자료형이 아닌
# 정수형을 반올림 할 때 오사오입 법칙을 따르는데
# 이건 우리가 기존에 알고 있던 반올림과
# 거리가 먼 것을 알 수 있다
# 때문에 반올림 할 때는 함수를 직접 만들어서
# 사용한다.

# i = 0 이라는건 소수점 첫째자리 라는 뜻
num = -0.6
def fun_round(num, i=0):
  # 5.5 = 5.5 * 10**(0)
  # 10.5 = 10.5
  num = num * 10**(i)
  if num >= 0:
    # 5.5 를 int 화 시키면
    # 5 소수점이 없고 5가 되는거지
    # 그럼 5+1 하니까 6이되는거고
    # num_f = 11
    # 10.5 - 11
    # 0.05
    num_f = int(num) + 1
    if num-int(num) >= 0.5:
      return num_f / (10**i)
    else:
      return int(num) / (10**i)
  else:
    # 0.2 = int(num) = 0 - 1= -1
    # 0.2 - 1 = 0.8
    num_f = int(num) - 1
    # 0 - 1 = -1

    # -0.6 - 0 = -0.6
    if num-int(num) <= -0.5:
      return num_f / (10**i)
    else:
      return int(num) / (10**i)

print(fun_round(num))
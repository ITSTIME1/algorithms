
# 정석 풀이법
num1, num2 = map(int, input().split())


gcd = 0
lcm = 0
for i in range(min(num1, num2), 0, -1):
  if num1 % i == 0 and num2 % i == 0:
    gcd = i
    break
    for k in range(max(num1, num2), (num1*num2)+1):
      if k % num1 == 0 and k % num2 == 0:
        lcm = k
        break



print(gcd, lcm, sep="\n")

# 라이브러리 이용
import math

a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))


def GCD(x, y):
  # y 가 0이 아닐때까지
  while y:
    x, y = y, x%y
    # 2 % 0 일경우 y가 참이 아니기 때문에
    # x 값을 반화해주면 그게 바로 GCD 가 되는것임.
  return x
print(GCD(10, 12))

# LCM 은 x*y 를 곱한값에서 GCD 값으로 나눈 몫이 
# 최소공배수가 나온다.
def LCM(x, y):
  result = (x*y) // GCD(x,y)
  return result
  
  
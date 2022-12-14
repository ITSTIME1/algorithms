import sys


# 테스트 케이스가 주어지지 않았기에 시도하고
# 에러에 대한 부분은 break 로 나온다
# ex(1, 2,3 ㄱ)
while True:
  try:
    a, b = map(int,   sys.stdin.readline().split())
    print(a+b)
  except:
    break



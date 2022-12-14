T = int(input())

def solution(T):
  for i in range(T):
    H, W, N = map(int, input().split())
    floor = N % H
    number = N // H+1
    if(floor == 0):
      floor = H
      number = N // H
    print(floor*100+number)
solution(T)

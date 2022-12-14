a, b, c = map(int, input().split())

def solution(a, b, c):
  if b >= c:
    print(-1)
  else:
    print(a // (c-b) + 1)

solution(a, b, c)
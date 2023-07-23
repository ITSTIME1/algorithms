N, M, K = map(int, input().split())
result = 0
while N >= 2 and M >= 1 and N+M-3 >=K:
  N-=2
  M-=1
  result+=1
  if(N<1 and M<0):
    break

print(result)
  
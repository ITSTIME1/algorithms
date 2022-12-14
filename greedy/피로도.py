a, b, c, m = map(int, input().split())


piro = 0
work = 0
for i in range(1, 25):
  if piro + a <= m:
    piro += a
    work += b
  else:
    if piro-c >= 0:
      piro-=c
    else:
      piro = 0


print(work)
    


# 두번째 풀이
    

A, B, C, M = map(int, input().split())

i = 1;
piro = 0;
piroResult = 0;
work = 0
# i = 1 시간 일하면 piro = +=a
while i <= 23:
  i+=1
  piroResult = piro + A;
  if  piroResult <= M:
    piro += A;
    work += B;
  else:
    if piro - C < 0:
      work = 0
    else:
      piro-=C
  if(i > 23):
    break;

print(work)
# 시작 시간 - 끝나는 시간
# 공백 없어야 되고

# 1, 4 = 5, 7, 7 = 


N = int(input())

array = []
replace = []

for i in range(N):
  s, e = map(int, input().split())
  array.append([s, e])

replace = sorted(array, key=lambda x: x[0])
replace = sorted(array, key=lambda x: x[1])

last = 0
count = 0

for s, e in replace:
  if s >= last:
    count += 1
    last = e
print(count)

import sys

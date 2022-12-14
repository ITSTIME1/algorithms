# 5
# Mickey 1 10 1991
# Alice 30 12 1990
# Tom 15 8 1993
# Jerry 18 9 1990
# Garfield 20 9 1990

# 가장 나이가 많은 사람 = 연도가 가장 낮고, 월, 일 가장 낮은 사람
# 가장 나이가 적은 사람 = 연도가 가장 높고, 월, 일 가장 높은 사람


N = int(input())

arr = []
for i in range(N):
  n, d, m, y = input().split()
  d = int(d)
  m = int(m)
  y = int(y)
  arr.append((n, d, m, y))

arr.sort(key = lambda x : (x[3], x[2], x[1]))
max_c = arr[0][0]
min_c = arr[len(arr)-1][0]
print(min_c, max_c , sep = "\n")

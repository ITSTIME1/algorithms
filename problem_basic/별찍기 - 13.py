N = int(input())

for i in range(N):
  print("*" * (i+1))

# 2 = 0, 1
for j in range(N-1):
  print("*" * (N-j-1))
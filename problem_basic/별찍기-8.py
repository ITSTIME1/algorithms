N = int(input())

for i in range(N):
  for j in range(N-i-1):
    print(" ", end = "")

  for j in range((2*i+1)):
    print("*", end = "")
  print()


# 4, 3, 2, 1
for r in range((N-1), 0, -1):
  for k in range(N-r):
    print(" ", end="")
  for k in range(2*r-1):
    print("*", end="")
  print()
N = int(input())
# 4 = 0, 1, 2, 3

for i in range(N):
  if(i == 0):
    print(" " * (N-i-1) + "*")
  elif (i<N-1):
    print(" " * (N-i-1) + "*" + " " * (2*(i+1)-3) + "*")
  elif(i == N-1):
    print(" " * (N-i-1) + "*" + "*" * (2*(i+1)-3) + "*")
    
    
# 1. 공백은 - 1씩
# 2. 별은 1개씩
# 3. 별의 입력 개수에서 ex) 3 0, 1, 2 2 이상부터는 별을 출력

#  * * *
# * * * *


N = int(input())

for i in range(N):
  if(i == 0):
    print(" " * (N-i-1) + "*")
  elif(i ==  1):
    print(" " * (N-i-1) + "*" + " " * i + "*")
  elif (i >= 2): 
    print(" " * (N-i-1) + "*" + " *" * i)
    
  
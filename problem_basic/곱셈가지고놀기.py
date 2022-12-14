i = 1
while i < 9:
  i+=1
  if(i % 2 == 0):
    for j in range(1, 10):
      print(i, "*", j, "=", i*j, end=' ')
    print("============================")
    print()
  elif(i % 2 == 1):
    for k in range(1, 10):
      print(i, "*", k, "=", i*k, end=' ')
    print("============================")

  if(i>9):
    break
    
sugar_number = int(input())
count = 0
while sugar_number >= 0:
  if sugar_number % 5 == 0:
    count += sugar_number // 5
    print(count)
    break
  else:
    sugar_number-=3
    count+=1 
else:
  print(-1)
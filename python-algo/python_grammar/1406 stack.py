string = list(input().lower())
command = int(input())

# 4
# 0, 4 = 0, 1, 2, 3
move_check = len(string)
print(move_check)
for i in range(1, command+1):
  order = list(input().split())
  order_command = order[0].upper()
  if(order_command == "P"):
    # 마지막 값이라면
    if(move_check == len(string)):
      string.append(order[1])
      move_check = len(string)
      # 첫번째 값이라면
    elif(move_check == 0):
      string.insert(move_check, order[1])
    else:
      string.insert(move_check, order[1])
      move_check = len(string)
              
  elif(order_command == "L"):
    if(move_check == 0):
      pass
    else:
      move_check -= 1
  elif(order_command == "D"):
    if(move_check == len(string)-1):
      pass
    else:
      move_check += 1
  elif(order_command == "B"):
    if(move_check == 0):
      string.pop()
      pass
    else:
      # L = 2
      
      string.pop()
  
    
    
      
    
      
    
    
  print(string)
  print(move_check)
print("".join(string))
      
    
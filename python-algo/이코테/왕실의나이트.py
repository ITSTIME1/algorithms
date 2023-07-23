
import time
# a1
start = time.time()
input_data = input()


# 가로 row 
row = input_data[1]
column = (int(ord(input_data[0])) - int(ord('a'))) + 1

# x, y = 1, 1 = (row, column)

# 이동 경로가 8가지고 나옴 조건의 따라서
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]


count = 0
for check_step in steps:
  # 8가지의 경우의 수를 다 보면서
  n_row = int(row) + int(check_step[0])
  n_column = int(column) + int(check_step[1])


  if n_row >= 1 and n_row <= 8 and n_column >=1 and n_column <= 8:
    count+=1
  x, y = n_row, n_column

print(count)
print(time.time() - start)

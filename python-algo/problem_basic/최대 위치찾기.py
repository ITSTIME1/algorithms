int_counter = 9

numbers = []

for i in range(0, int_counter):
  n = int(input())
  numbers.append(n)

print(max(numbers))
# 인덱스에서 요구하는 값이 몇번째인지 잘 확인해야됨
# 인덱스가 0부터 시작하므로 +1 더해주어야함
print(numbers.index(max(numbers))+1)
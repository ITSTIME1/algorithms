test_case = int(input())

for i in range(1, test_case+1):
  a, b = map(int, input().split())
  print(f'Case #{i}: {a+b}')
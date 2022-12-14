test_case = int(input())



def case_function(test_case):
  for i in range(1, test_case+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')


case_function(test_case)
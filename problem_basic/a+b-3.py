test_number = int(input())


def plus_function (test_number):
  for i in range(test_number):
    a, b = map(int, input().split())
    print(a+b)



plus_function(test_number)
  
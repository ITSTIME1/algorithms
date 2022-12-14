value = int(input())

def multipliation(value):
  for i in range(1, 10):
    result = value * i
    print(value, '*', i, '=', result)

multipliation(value)
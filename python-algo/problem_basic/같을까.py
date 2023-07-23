a, b, c = map(int, input().split())

def algorithms_result(a, b, c):
  one = (a+b)%c
  two = ((a%c)+(b%c))%c
  three = (a*b)%c 
  four = ((a%c)*(b%c))%c

  print(one, two, three, four, sep='\n')

algorithms_result(a, b, c)

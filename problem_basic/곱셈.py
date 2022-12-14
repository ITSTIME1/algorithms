a = int(input())
b = input()

def multiplication(a, b):
  three = a * int(b[2]) 
  four = a * int(b[1])
  five = a * int(b[0])
  six = a * int(b)
  print(three, four, five, six, sep='\n')


multiplication(a, b)

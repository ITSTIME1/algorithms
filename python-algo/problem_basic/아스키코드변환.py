input_value = input()

def solution(input_value):
  if type(input_value) is str:
    print(ord(input_value))
  elif type(input_value) is int:
    print(chr(input_value))

  

solution(input_value)

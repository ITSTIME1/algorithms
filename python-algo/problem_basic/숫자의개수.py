a = int(input())
b = int(input())
c = int(input())

def solution_answer(a, b, c):
  result_list = a*b*c
  answer_list = list(str(result_list))

  for i in range(0, 10):
    print(answer_list.count(str(i)))


solution_answer(a, b, c)
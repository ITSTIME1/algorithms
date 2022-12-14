class StackClass():
  # 생성자
  def __init__(self):
    self.data = []

  # 사이즈 반환
  def size(self):
    return len(self.data)

  def pop(self):
    # 정수가 없는 경우 
    pop_object = None
    if(len(self.data) == 0):
      print("-1")
    else:
      pop_object = self.data.pop(-1)
      return print(pop_object)

      
  def empty(self):
    if(len(self.data) == 0):
      return print("1")
    else:
      return print("0")

  def top(self):
    if(len(self.data) == 0):
      return print("-1")
    else:
      return self.data[-1]
      

  def push(self, num):
    object_int = self.data.append(num)
    return object_int
    


a = StackClass()
N = int(input())
for i in range(N):
  order = list(input().split())
  if order[0] == "push":
    a.push(int(order[1]))
  elif order[0] == "pop":
    b = a.pop()
  elif order[0] == "size":
    print(a.size())
  elif order[0] == "empty":
    a.empty()
  elif order[0] == "top":
    print(a.top())

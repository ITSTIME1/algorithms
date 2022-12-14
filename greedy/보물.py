N = int(input())
a_number = list(map(int, input().split()))
b_number = list(map(int, input().split()))

a_number.sort(reverse=True)
# [6,1,1,1,0]
# [1,2,3,7,8]
# 정렬을 안하면 b_number 값이 s의 최소값이 되지 못하게 하기 때문에.
b_number.sort() # 문제에서는 배열 바꾸지 말라했지만 사실상 상관 없는 문제. 말라했음.
result = 0

for i in range(N):
  result += a_number[i] * b_number[i]

  if(i > N):
    break
print(result)
    

# Solution 2

N = int(input())

a_number = list(map(int, input().split()))
b_number = list(map(int, input().split()))
result = 0

# for i in range(N):
#   a_number.sort()
#   b_max_index = b_number.pop(b_number.index(max(b_number)))

#   result += a_number[i] * b_max_index
# print(result)

def solution(N):
  global result
  global a_number
  global b_number
  
  for i in range(N):
    a_number.sort()
    b_max_index = b_number.pop(b_number.index(max(b_number)))
    result += a_number[i] * b_max_index

solution(N)
print(result)
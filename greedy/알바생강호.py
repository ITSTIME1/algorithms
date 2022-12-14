import sys
N = int(input())
array = []

# 총 N 번 만큼
for i in range(N): 
    array.append(int(sys.stdin.readline().strip()))


array.sort(reverse=True)
# 3, 1, 2 총 3번
for i in range(N):
  result = array[i]-((i+1)-1)
  if(result < 0):
    array[i] = 0
  else:
    array[i] = result
print(sum(array))
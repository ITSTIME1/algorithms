from collections import deque
N = int(input())
# arr = deque(i for i in range(1, N+1))
arr = deque(range(1, N+1))
result = []
# O(N)
while len(arr) != 1:
	result.append(arr.popleft())
	arr.append(arr.popleft())

result.append(arr[0])
print(*result)




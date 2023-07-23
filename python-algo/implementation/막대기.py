import sys

N = int(sys.stdin.readline().rstrip())

arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

last = arr[-1]
count = 1
for i in reversed(range(N)):
	if arr[i] > last:
		count+=1
		last = arr[i]
	else:
		pass
print(count)

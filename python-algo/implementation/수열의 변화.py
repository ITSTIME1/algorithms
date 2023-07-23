import sys
N, K = map(int, sys.stdin.readline().strip().split())

arr = list(map(int, sys.stdin.readline().strip().split(",")))


i = 1
while i <= K:
	for j in range(len(arr)-1):
		arr[j] = arr[j+1] - arr[j]
	i+=1

for i in range(K):
	arr.pop()
print(*arr, sep=",")
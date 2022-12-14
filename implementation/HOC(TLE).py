import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.sort()

# sort() = O(nlogn) + O(N)
# O(N ) 이 더 크기 때문에 시간복잡도는 O(n)
cnt = 0 
for i in range(1, len(arr)+1):
	# 1, 2, 3, 4, 5
	if arr[i-1] != i:
		cnt+=1
		print(i)
		break
if cnt == 0:
	print(len(arr)+1)

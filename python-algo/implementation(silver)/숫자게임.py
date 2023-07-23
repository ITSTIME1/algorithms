N = int(input())
total = []
cnt = 0
for i in range(N):
	arr = list(map(int, input().split()))
	result = []
	for j in range(len(arr)-2):
		for k in range(j+1, len(arr)-1):
			for n in range(k+1, len(arr)):
				re = list(str(arr[j]+arr[k]+arr[n])) 
				result.append(re[len(re)-1])
	c = list(map(int, set(result)))
	total.append((i+1, max(c)))

total.sort(key = lambda x : (-x[1]))
max_num = total[0][1]
re = [j[0] for j in total if max_num == j[1]]
print(max(re) if len(re) > 1 else re[0])

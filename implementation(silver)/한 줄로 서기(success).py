n = int(input())
arr = list(map(int, input().split()))


dic = {}
for i in range(len(arr)):
	dic[i+1] = arr[i]

ran = list(range(1, n+1))

total = []
while True:
	if len(total) == n:
		print(*total, end = " ")
		break	
	for i in ran:
		cnt = 0
		for j in total:
			if i < j:
				cnt += 1
		if cnt == dic[i]:
			total.append(i)
			del ran[ran.index(i)]
			break







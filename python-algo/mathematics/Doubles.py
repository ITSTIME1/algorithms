
# -1 입력을 받기 전까지
while True:
	arr = list(map(int, input().split()))
	# -1을 받았다면 반복문 종료
	if arr[0] == -1:
		break
	# print(arr[:len(arr)-1])
	cnt = 0	
	for i in range(len(arr[:len(arr)-1])):
		div = arr[i] // 2
		# 나머지가 0
		# div 가 arr 안에 있다면 cnt += 1
		if arr[i] % 2 == 0:
			if div in arr:
				cnt+=1

	print(cnt)
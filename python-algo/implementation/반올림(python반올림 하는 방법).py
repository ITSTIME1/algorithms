N = int(input())


# 재귀 함수
def recursive(num):
	# int -> str 바꾸고 map 객체를 통해서 list 로 만들어서

	num_len = list(map(int, str(num)))
	# [1, 2, 3]
	if len(num_len) < 2:
		return print(*num_len, sep = "")
		
	else:
		# 1의자리 반올림
		for i in range(len(num_len)-1, 0, -1):
			if num_len[i] >= 5:
				num_len[i] = 0
				num_len[i-1] = num_len[i-1]+1
			else:
				num_len[i] = 0
		
	return print(*num_len, sep = "")


for i in range(N):
	num = int(input())
	recursive(num)

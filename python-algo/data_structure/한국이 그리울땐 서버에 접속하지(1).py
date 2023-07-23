
n = int(input())

pattern = list(map(str, input().split("*")))

left = pattern[0]
right = pattern[1]

ans = []
for i in range(n):
	string = input()
	# 왼쪽, 오른쪽 문자열 매칭이 잘 맞았나 확인.
	if string[:len(left)] == left and string[-len(right):] == right:
		
	else:
		# 애초부터 맞지 않는건 NE
		print("NE")
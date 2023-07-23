N = int(input())
grade = list(map(int, input().split()))


result = []
for i in range(len(grade)):
	check = grade[i]
	
	# 점수가 비어있다면 첫 값이기 때문에
	# 첫 값은 숫자를 그대로 대입
	if(len(result) == 0):
		result.append(check)

	# 점수가 비어있지 않고 값이 있다면
	# 1. 이번에 가지고 온 값이 0 이라면
	# 그대로 result에 넣어주고
	# 2. 이번에 가지고 온 값이 1 이고 이전에 가지고 온 값이
	# 0이라면 result 1로 들어가고
	# 3. 이번에 가지고 온 값이 1이고 이전에 가지고 온 값이
	# 1이라면 
	else:
		# 이전 값
		pre = result[len(result)-1]
		if check == 0:
			result.append(0)
			#[ 1, 0 ]
		elif check == 1 and pre == 0:
			result.append(1)
		elif check == 1 and pre >= 1:
			result.append(pre+check)
print(sum(result))
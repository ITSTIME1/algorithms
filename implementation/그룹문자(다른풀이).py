N = int(input())

array = [input() for _ in range(N)]


good = 0 
for i in range(len(array)):
	position = 0
	wrong_string = 0
	check_string = [_ for _ in array[i]]
	for k in range(len(check_string)-1):
		# 연속 되어 있지 않다면
		if check_string[k] != check_string[k+1]:
			position = k
			checking = check_string.pop(k)
			if checking in check_string:
				wrong_string += 1
		
		check_string.insert(position, checking)
	
	# 한 문자를 다 검사하고 
	# 봤는데 틀린 문자라고 판단되었다면?
	# 그 문자열은 틀린문자열
	if wrong_string == 0:
		good += 1 

print(good)

# runtime error



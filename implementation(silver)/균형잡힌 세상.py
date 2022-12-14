# 다시 해보자
# 풀었으
# 시행 착오 끝에 낙이온다
while True:
	string = input()
	if string == ".":
		break
	word, x = [], 0
	for i in range(len(string)):
		if string[i] == "(" or string[i] == "[":
			word.append(string[i])
		elif string[i] == "]" or string[i] == ")":
			if len(word) != 0:
				if string[i] == "]" and word[-1] == "[":
					word.pop()
					continue
				if string[i] == ")" and word[-1] == "(":
					word.pop()
					continue
				else:
					word.append(string[i])
			else:
				x = 1
				break

	if x == 1:
		print("no")
	else:
		if len(word) == 0:
			print("yes")
		else:
			print("no")

# ((])).
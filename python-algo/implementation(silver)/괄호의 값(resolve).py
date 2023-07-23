string = list(input())
dic = {"()": 0, "[]": 0}
two = 2
three = 3
total = []
stack = []
# ]()
# # 
# ((((())))(()))
def clear(dic):
	for i in dic:
		dic[i] = 0	
	return dic	
def check_string(string):
	x = 0
	stack = []
	for i in range(len(string)):
		if string[i] == "(" or string[i] == "[":
			stack.append(string[i])
		elif string[i] == ")" or string[i] == "]":
			if len(stack) == 0:
				x = 1
				continue
			check = stack[-1]
			if (check == "(" and string[i] == ")") or (check == "[" and string[i] == "]"):
				stack.pop()
			else:
				stack.append(string[i])
	if len(stack) == 0 and x == 1:
		return False
	elif len(stack) == 0 and x == 0:
		return True
		
if check_string(string):
	for i in range(len(string)):
		if string[i] == "(" or string[i] == "[":
			stack.append(string[i])
		elif string[i] == ")" or string[i] == "]":
			check = stack[-1]
			# 마지막값으로 값들이 남았을때
			if (len(stack) == 1 and stack[-1] == "(") or (len(stack) == 1 and stack[-1] == "["):

				if check+string[i] == "()":
					# 1 + 3
					if two**dic[check+string[i]] == 1:
						result = three**dic["[]"]
						total.append(two*result)
						clear(dic)
						continue
					else:
						result = two**dic[check+string[i]] + three**dic["[]"]
						total.append(two*result)
						clear(dic)
						stack.pop()
				elif check+string[i] == "[]":
					if three**dic[check+string[i]] == 1:
						result = two**dic["()"]
						total.append(three*result)
						clear(dic)
						continue
					else:
						result = three**dic[check+string[i]] + two**dic["()"]
						total.append(three*result)
						clear(dic)
						stack.pop()
			else:
				dic[check+string[i]] += 1
				stack.pop()
	else:
		print(sum(total))
else:
	print(0)
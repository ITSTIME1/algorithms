import sys

string = list(sys.stdin.readline().strip())
check = False
# <open>tag<close>
# <int><max>2147483647<long long><max>9223372036854775807
total = []
tag = []
word = []

# <ab cd>ef gh<ij kl>
for i in range(len(string)):
	# 열린 태그 일때
	if string[i] == "<":
		check = True
		if len(word) != 0:
			total.append("".join(word[::-1]))
			word.clear()
		if len(tag) != 0:
			total.append("".join(tag))
			tag.clear()
		tag.append(string[i])
	elif string[i] == ">":
		check = False
		tag.append(string[i])

	else:
		if check == False:
			if len(tag) != 0:
				total.append("".join(tag))
				tag.clear()
			if string[i] == " ":
				total.append("".join(word[::-1]))
				total.append(string[i])
				word.clear()
				continue
			word.append(string[i])
			continue
		else:
			tag.append(string[i])



if len(word) != 0:
	total.append("".join(word[::-1]))
if len(tag) != 0:
	total.append("".join(tag))

result = "".join(total)
print(result)
# if result.find("<") and result.find(">"):
# 	# 찾는 문자가 없을땐
# 	c = list(result.split()[::-1])
# 	print(*c, end = " ")
# else:
# 	print(result)

# if ["<", ">"] in result:
# 	print("".join(result))
# else:
# 	print(list(result.split()[::-1]))
# # # output
# <int><max>7463847412<long long><max>7085774586302733229

# # answer 
# <int><max>7463847412<long long><max>7085774586302733229

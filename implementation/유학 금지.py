
det = "CAMBRIDGE"
string = list(map(str, input()))

result = []
for i in range(len(string)):
	if string[i] not in det:
		result.append(string[i])


print("".join(result))		
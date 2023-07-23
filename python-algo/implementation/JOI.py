string = list(input())
result = []
joi = 0
ioi = 0
for i in range(len(string)):
	result.append(string[i])
	if "".join(result) == "JOI":
		joi += 1
		del result[:2]
	elif "".join(result) == "IOI":
		ioi += 1
		del result[:2]
	else:
		if len(result) >= 3:
			if "".join(result) == "JOI":
				join+=1
				del result[:2]
			elif "".join(result) == "IOI":
				ioi += 1
				del result[:2]
			else:
				del result[0]
		else:
			continue
print(joi, ioi)


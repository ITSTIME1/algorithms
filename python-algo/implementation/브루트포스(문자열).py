target = "ABC"
text = "ABCABC"

# 3 0 1 2
cnt = 0
print(len(text))
print(len(target))
for i in range(len(text) - len(target)):
	print(str(i) + "for 첫")
	# 0 1 2 
	for j in range(len(target)):
		print(str(i) + "for 둘")
		if text[i+j] == target[j]:
			cnt += 1
		else:
			break



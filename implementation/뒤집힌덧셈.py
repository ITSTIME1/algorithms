from collections import deque
grade = list(map(int, input().split()))

result = []
for i in range(len(grade)):
	num = str(grade[i])

	change = deque()
	for k in num:
		change.appendleft(k)
	
	list_word = "".join(change)
	result.append(list_word)


result = list(map(int, result))
total = sum(result)

new_number = deque()
for n in str(total):
	new_number.appendleft(n)

total_number = ''.join(new_number)
print(int(total_number))
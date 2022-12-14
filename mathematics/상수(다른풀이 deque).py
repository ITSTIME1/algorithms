from collections import deque
arr = list(map(str, input().split()))

result = deque()
for i in arr:
	check = i
	# 734
	make = deque()
	for ch in check:
		make.appendleft(ch)
	result.append(make)


first = "".join(list(result[0]))
second = "".join(list(result[1]))
if first > second:
	print(first)
else:
	print(second)
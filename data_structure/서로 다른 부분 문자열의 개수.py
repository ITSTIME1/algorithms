# 문제분석

# TLE.
# string = list(input())

# length = 1
# dic = {}
# while length <= len(string):
# 	for i in range(0, len(string)):
# 		if "".join(string[i:i+length]) not in dic:
# 			dic["".join(string[i:i+length])] = 1
# 	length += 1

# print(len(dic))

string = input()
length = 1

cnt = 0
arr = set()
while length <= len(string):
	for i in range(0, len(string)):
		arr.add(string[i:i+length])
	# 서로 다른 문자열이고
	length += 1

# set table 을 썼어야 하는 문제이구만
print(len(arr))


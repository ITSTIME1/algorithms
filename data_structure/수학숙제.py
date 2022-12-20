import re 
# 정규식 문제라고 하는데
# python 정규식 모듈인 re = regex
# 정수만 출력하고 싶을때 이런 정규식 모듈을 사용하면 쉽게 찾을 수 있다

ans = []
for _ in range(int(input())):
	numbers = re.findall("\d+", input())
	ans.extend(list(map(int, numbers)))

print(ans)


# 정규식을 안쓰고 푼다면?


n = int(input())
num = []
for _ in range(n):
	string = input()
	temp = ""
	for i in string:
		if i.isdigit():
			temp+=str(i)
		if i.isalpha():
			if temp == "":
				continue
			else:
				num.append(int(temp))
				temp = ""
	if temp != "":
		num.append(int(temp))

num.sort()
for i in num:
	print(i, end = "\n")
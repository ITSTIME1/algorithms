# 음 각 문자를 아스키코드 값으로 바꿔서
# 맵핑 되어진 아스키코드 값에다가 넣어주면 되겠는데
# 아니면 리스트를 하나 만들어서
# 어짜피 모음이라는건 aeiou 이 다섯가지 밖에 없으니까
# 해당 문자들을 넣어서
# print(ord("e") % 97)
import sys
a = [ord("a") % 97, ord("A") % 97, ord("e") % 97, ord("E") % 97, ord("i") % 97, ord("I") % 97, ord("o") % 97, ord("O") % 97, ord("u") % 97, ord("U") % 97]

total = 0

while True:
	s = input().strip()
	if s == "#":
		break
	for i in s:
		if ord(i) % 97 in a:
			total += 1

	print(total)
	total = 0


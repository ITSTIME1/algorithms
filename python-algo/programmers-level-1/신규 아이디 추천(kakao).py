import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 끝나면 True로 바꾸면 되니까

def one(id):
	one_id = ""
	for i in id:
		if i.isupper() == True:
			l = i.lower()
			one_id += l
			continue
		else:
			one_id += i
	return one_id

def two(id):
	two_id = ""
	# 알파벳 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한
	# 모든 문자를 제거
	stack = list(id)
	for i in stack:
		if i.islower() == True or i.isdigit() == True or i == "-" or i == "_" or i == ".":
			two_id += i
		else:
			continue

	return two_id


def three(id):
	three_id = ""
	stack = deque(list(id))
	word = []
	while len(stack) != 0:
		w = stack.popleft()
		
		if len(word) == 0:
			word.append(w)
			continue
		elif w == "." and word[-1] == ".":
			continue

		else:
			word.append(w)
	
	three_id = "".join(word)
	return three_id


def four(id):
	four_id = ""
	stack = deque(list(id))
	if stack[0] == ".":
		stack.popleft()
	elif stack[-1] == ".":
		stack.pop()

	four_id = "".join(stack)
	return four_id


def five(id):
	stack = list(id)
	if len(stack) == 0:
		stack.append("a")
	
	five_word = "".join(stack)
	return five_word


def six(id):
	stack = list(id)
	six_word = ""
	if len(stack) >= 16:
		six_word = "".join(stack[0:15])
	else:
		six_word = "".join(stack)

	if six_word[-1] == ".":
		s = list(six_word)
		s.pop()
		six_word = "".join(s)

	return six_word


def seven(id):
	stack = list(id)
	n = len(stack)
	last = stack[-1]
	if len(stack) <= 2:
		for i in range(3-n):
			stack.append(last)

	seven_id = "".join(stack)
	return seven_id



answer = ""
new_id = "abcdefghijklmn.p"
isActive = True
while isActive != False:
	# 단어가 규칙에 맞지 않는다면!
	one_id = one(new_id)
	two_id = two(one_id)
	three_id = three(two_id)
	four_id = four(three_id)
	
	five_id = five(four_id)
	
	six_id = six(five_id)
	
	seven_id = seven(six_id)

	answer = seven_id
	isActive = False

print(answer)




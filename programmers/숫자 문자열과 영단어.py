import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



number = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}


strings = "123"

result = []
answer = ""
for i in strings:
	if i.isdigit() == False:
		r = "".join(result)
		if r in number:
			answer += number[r]
			result = []

		result.append(i)

	else:
		r = "".join(result)
		if r in number:
			answer += number[r]
			answer += i
			result = []
		else:
			answer += i

if len(result) != 0:
	r = "".join(result)
	if r in number:
		answer += number[r]
print(answer)



# replace 함수를 사용하면
# key 에 해당하는 걸 값으로 바꿔주는 역할을 하는 함수
# 이걸하면 진짜 빠르네
# 그럼 s에 있는 문자열을 value에 해당하는 값으로 바꿔준다면
# 되는거네..

answer = s

    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

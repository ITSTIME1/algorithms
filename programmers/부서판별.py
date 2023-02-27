import sys
import heapq
from collections import deque
from string import ascii_lowercase, ascii_uppercase
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

alphabet_list = list(ascii_lowercase)
alphabet_list_upper = list(ascii_uppercase)



s = "AB"
n = 1

# 생각해보니까 z일대를 생각안해도 알파벳문자길이로나누어주면
# z가 넘어도 찾을 수 있음.

answer = ""
for i in s:
	# 만약 문자열에서 가지고온 문자가 대문자라면
	if i.isupper() == True:
		a = alphabet_list_upper.index(i)
		# z같은 마지막 문자라면
		answer += alphabet_list_upper[(a+n) % len(alphabet_list_upper)]
		
	# 만약 가지고온 문자가 소문자라고 한다면
	elif i.islower() == True:
		a = alphabet_list.index(i)

		answer += alphabet_list[(a+n) % len(alphabet_list)]

	# 만약에 공백이 들어온다면
	elif i == " ":
		answer += " "
print(answer)

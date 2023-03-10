import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

s = "3people unFollowed  me"
s_list = list(s.split(" "))


# 공백이 있어서 그렇구나 그러면 하나씩 읽어와야 될거 같은데 =
# 하나씩 읽어와서 첫글자만 보고 판단하면 될거 같은데 

def solution(s):
	s_list = list(s.split(" "))
	print(s_list)

	ans = ""
	for i in range(len(s_list)):
		if s_list[i] == "":
			ans += " "
			continue
		if s_list[i][0].isdigit() == True:
			ans += s_list[i].lower() + " "
		
		else:
            # ans += s_list[i].title() + " "
			ans += s_list[i].capitalize() + " "
	return ans[:len(ans)-1]


# title() 과 capitalize() 의 차이라고 한다면
# 둘다 첫 글자를 대문자로 변경해준다는건 동일하지만
# title() 같은 경우 알파벳 외의 문자로 나누어져 있는 영단어들의 첫 글자를 모두 대문자로 바꾸어준다.

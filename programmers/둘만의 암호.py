import sys
import heapq
from collections import deque
from string import ascii_lowercase
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline



# 문자열 s, skip
# 자연수 index
# 주어진다고하는
# 규칙에 따라서 문자열을 만든다고 한다.

# 문자열 s의 각 알파벳을 index 만큼 뒤의 알파벳으로 바꿔준다는건데

# 그럼 z를 넘어가면 z를 처음넘어가는 시점부터 a, b, c,.. 이런식으로
# 그럼 이렇게 해볼까ord가 아

# 왜 틀리지? 아스키코드를 쓴것도 아니고 string을 썻는데도?
# 아 내가 착각했으 넘겨지는걸 착각햇으
# 포함해서 없애는게 아니라
# 그냥 skip_list에 포함되는건 애초부터 넘기고 카운트 세지 않아야 하는것임.



alpha = list(ascii_lowercase)

# 26
# print(len(alpha))
s = "aukks"
skip = "wbqd"
index = 5

s_list = list(s)
skip_list = list(skip)


answer = ""
idd = index
for i in range(len(s_list)):
	stack = []
	j = 1
	# a = (alpha.index(s_list[i]) + index) % len(alpha)
	while idd != 0:
		a = (alpha.index(s_list[i]) + j) % len(alpha)
		if alpha[a] in skip_list:
			j+=1
			continue
		else:
			idd-=1
			j+=1
			stack.append(alpha[a])

	answer += stack[-1]
	idd = index

print(answer)



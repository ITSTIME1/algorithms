import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 이건 스택을 이용한 문제같은데

# 문자열별로 hash를 만들자
# 그리고 각각의 인덱스 값을 저장하고



# 우선 전부다 0 으로 만들어두고

# 문자를 하나씩 가지고 왔을때
# 처음가지고 왔다면 0 으로 되어 있기 때문에
# -1 을 추가하고
# 해당 인덱스로 바꿔준다 
# b = 0 -1
# a = 1 -1
# n = 2 -1
# a = 3-1 = 2
# n = 4-2 = 2 
# a = 5-3 = 2

# 맞네 문제 이해가 맞는데 아마 아까 0 때문에 틀렸을거 같다

s = "foobar"
dic = {}

for i in s:
	if i not in dic:
		dic[i] = [False]

s_l = list(s)
answer = []
for i in range(len(s_l)):
	# 처음 들어왔다면
	if dic[s_l[i]][0] == False:
		dic[s_l[i]].append(i)
		dic[s_l[i]][0] = True
		answer.append(-1)
	# 처음 들어온게 아니라면
	else:
		a = i - dic[s_l[i]][-1]
		answer.append(a)
		dic[s_l[i]].append(i)
print(answer)



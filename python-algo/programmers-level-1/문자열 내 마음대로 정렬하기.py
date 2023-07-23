import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 정한 순서대로 문자를 배치한 뒤 return
# 만약 n의 인덱스 문자열을 가지고 왔을때
# 그 문자를 가진 문자가 두개 이상이라면
# 그 문자를 정렬했을때 사전순으로 빠른걸 넣어준다

# 각각 의문자들을 일단 가지고 온다면

strings = ["sun", "bed", "car"]
n = 1

a = {}
for i in strings:
	word = list(i)
	c = word[n]
	if c not in a:
		a[c] = [i]
	else:
		a[c].append(i)

a_list = sorted(a.items(), key = lambda x: x[0])

answer = []
for i in a_list:
	if len(i[1]) >= 2:
		i[1].sort()

for i in a_list:
	answer.extend(i[1])
print(answer)
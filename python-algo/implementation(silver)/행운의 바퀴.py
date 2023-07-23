import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 글자가 바뀌는 횟수랑
# 몇번째 돌렸는지랑 관계가 있나?

# 음 어떻게 풀지는 대충 알겠네
# 일단 디큐를 안쓰고 리스트로 구현도 가능할거 같다

n, k = map(int, input().split())


board = ['?'] * n

idx = 0
check = True
for i in range(k):
	num, cha = input().split()
	# 그 다음 인덱스를 찾기 위해서
	idx = (idx + int(num)) % n

	if board[-idx] == '?':
		board[-idx] = cha
		continue

	elif board[-idx] == cha:
		continue
	# 다른 문자일 경우니까
	# 같은 자리에 다른 문자가 있는 경우
	elif board[-idx] != cha and board[-idx] != '?':
		check = False

	

for i in range(n):
	# 물음표는 상관 없으니까
	if board[i] == "?":
		continue

	for j in range(i+1, n):
		# 같은 문자가 중복해서 존재할때
		# 같은 문자가 같은 곳에 있는건 위에서 필터링 거쳤는데
		# 다른 위치에 중복된 값이 있는건 검사를 안했기 때문에 검사를 해주어야 함.
		if board[i] == board[j]:
			check = False

if check:
	for i in range(-idx, n+(-idx)):
		print(board[i], end="")		
else:
	print("!")
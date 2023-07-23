# 부분 문자열이면 1
# 그렇지 않으면 0

# 우선 P의 첫 문자를 기준으로
# 받은 문자열에서 첫 문자와 같은 걸 찾고
# P  의 문자열의 길이 만큼 새로운 리스트에 담아준다음
# 그 P 의 문자열의 길이만큼 다 담았다면
# 문자열을 P 부분 문자열인지 검사하여
# 그 문자가 맞다면 1 아니라면 0 출력


# 만약 S 의 문자열 시작 길이부터 추가하는데
# P 의 길이가 더 길다면 0 

# "aek", "joo", "ekj"

# "aek"
# "baekjoon"

import sys


# 100만 이면 O(nlogn)
S = list(map(str, sys.stdin.readline().rstrip()))
P = list(map(str, sys.stdin.readline().rstrip()))

arr = []
cnt = 1
p_cnt = len(P)

for i in range(len(S)):
	if S[i] == P[0]:
		if p_cnt > len(S[i:p_cnt + len(S[:i])]):
			cnt = 0
			break
		else:
			arr.append(S[i:p_cnt + len(S[:i])])

a_j = "".join(arr[0])
p_j = "".join(P)

if cnt != 0: 
	if a_j == p_j: 
		print(1) 
	else: 
		print(0)
else:
	print(0)


# KMP 알고리즘 공부 ( 문자열 공부 )
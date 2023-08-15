import sys
from collections import Counter
input = sys.stdin.readline



n = int(input())

word = [input().strip() for _ in range(n)]
m = int(input())

string = [input().strip() for _ in range(m)]


if n == 1:
	print(string[0])
else:
	answer = ""
	for i in range(len(word)):
		if (i == 0 or i == len(word)-1) and word[i] == "?":
			next = ""
			if i == 0:
				next = word[i+1][0]
				for j in string:
					if j[-1] == next and j not in word:
						answer = j
			else:
				next = word[i-1][-1]
				for j in string:
					if j[0] == next and j not in word:
						answer = j
				
	
		else:
			if word[i] == "?":
				back = word[i-1][-1]
				next = word[i+1][0]
				for j in string:
					if j[0] == back and j[-1] == next and j not in word:
						answer = j


	print(answer)
# 1
# ?
# 1
# asdaada

# # 이런경우는 존재하지 않음 이유는 ? 하나이면서 후보문자열이 여러개니까 단서가없음.
# 1
# ?
# 2
# awfe
# awfe

# # 이런 경우는 앞에 처음이랑 끝 분기에 걸리게 됨.
# 2
# ?
# awfe
# 1
# awer





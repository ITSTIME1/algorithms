import sys
from string import ascii_lowercase
input = sys.stdin.readline

string = input().strip()

word = {}


for i in range(len(string)):
	if string[i] not in word:
		word[string[i]] = i

	else:
		# 가장 처음 나오는 인덱스를 원하고 있으니까
		# 가장 처음 나오는것이라면 두번째보단 첫번째가 더 인덱스로써 가깝고
		# 더 먼저 나왔기 때문에 문제 조건에 부합한다.
		# 가장 작은 인덱스만 가지고 있게 하고
		if word[string[i]] > i:
			word[string[i]] = i


alpha = list(ascii_lowercase)
# 인덱스를 찾아도 되겠구나 그럼 index()함수를 사용해서 가장 처음 문자가 나타난 위치를 찾게 될테니까
for i in range(len(alpha)):
	if alpha[i] in word: 
		print(word[alpha[i]], end = " ")

	else:
		print(-1, end = " ")


# alpha='abcdefghijklmnopqrstuvwxyz'
# for i in alpha:
#     if i in letter:
#         print(letter.index(i),end=' ')
#     else:
#         print(-1, end=' ')

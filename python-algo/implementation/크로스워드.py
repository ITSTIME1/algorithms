import sys
import copy
input = sys.stdin.readline


# copy를 사용하는게 더 오래걸리네
r, c = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]

ori = [[0] * c for _ in range(r)]

def width():
	# 방문여부
	visited = copy.deepcopy(ori)

	word_list = []
	for i in range(r):
		make_word = ""
		for j in range(c):
			if board[i][j] != "#" and visited[i][j] == 0:
				visited[i][j] = 1
				make_word += board[i][j]
			elif board[i][j] == "#" and len(make_word) > 1:
				word_list.append(make_word)
				make_word = ""
			elif board[i][j] == "#" and len(make_word) == 1:
				make_word = ""


		if make_word != "" and len(make_word)!=1:
			word_list.append(make_word)

	return word_list


def height():
	visited = copy.deepcopy(ori)

	word_list = []
	for i in range(c):
		make_word = ""
		for j in range(r):
			if board[j][i] != "#" and visited[j][i] == 0:
				visited[j][i] = 1
				make_word += board[j][i]
			elif board[j][i] == "#" and len(make_word) > 1:
				word_list.append(make_word)
				make_word = ""
			elif board[j][i] == "#" and len(make_word) == 1:
				make_word = ""

		if make_word != "" and len(make_word)!=1:
			word_list.append(make_word)
	return word_list
# 5 5
# good#
# an##b
# messy
# e##it
# #late
print(sorted(width() + height())[0])
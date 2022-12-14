# .F.F...F
# F...F.F.
# ...F.F.F
# F.F...F.
# .F...F..
# F...F.F.
# .F.F.F.F
# ..FF..F.


# # index 짝수일때 짝수번째가 흰
# # index 홀수일때 홀수번째가 흰
# w,b,w,b,w,b,w,b
# b,w,b,w,b,w,b,w

N = 8

board = [list(input()) for _ in range(N)]
# print(board)
h = 0
for i in range(N):
	for j in range(N):
		# 짝수라면
		# 홀라면
		# 0, 2, 4, 6
		if i % 2 == 0:
			if j % 2 == 0 and board[i][j] == "F":
				h+=1
		else:
			if j % 2 == 1 and board[i][j] == "F":
				h+=1
print(h)
	
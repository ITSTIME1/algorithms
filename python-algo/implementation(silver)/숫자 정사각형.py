N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
if min(N, M) == N:
	N1 = N
	M1 = M-(M-N)
elif min(N, M) == M:
	N1 = N-(N-M)
	M1 = M
elif N == M:
	N1 = N
	M1 = M

# 디테일 = 처음 발견 되는 넓이는 최대 넓이이니 == 처음 발견 되었을때 result에 저장하지 않고
# 바로 print(해준다면 더 효율적인 코드가 된다.)

# 2100ms -> 860ms..
while True:
	if N1 == 1 and M1 == 1:
		print(1)
		break
	for i in range(N-N1+1):
		for j in range(M-M1+1):
			check = []
			for k in range(i, i+N1):
				for c in range(j, j+M1):
					check.append(board[k][c])
					# k == 3 c == 3
			if (check[0] == check[N1-1]) and (check[0] == check[(N1*N1)-N1]) and (check[0] == check[(N1*N1)-1]):
				print(N1*M1)
				exit()
	N1-=1
	M1-=1




# 2172ms...
# N, M = map(int, input().split())

# board = [list(map(int, input())) for _ in range(N)]

# if min(N, M) == N:
# 	N1 = N
# 	M1 = M-(M-N)
# elif min(N, M) == M:
# 	N1 = N-(N-M)
# 	M1 = M
# elif N == M:
# 	N1 = N
# 	M1 = M
# result = []
# while True:
# 	if N1 == 1 and M1 == 1:
# 		result.append(1)
# 		break
# 	for i in range(N-N1+1):
# 		for j in range(M-M1+1):
# 			check = []
# 			for k in range(i, i+N1):
# 				for c in range(j, j+M1):
# 					check.append(board[k][c])
# 			if check[0] == check[N1-1] == check[(N1*N1)-N1] == check[(N1*N1)-1]:
# 				result.append(N1*M1)

# 	N1-=1
# 	M1-=1
# print(max(result))
# # 5 3
# # 422
# # 222
# # 111
# # 000
# # 101


# # This Case (fail)
# # 3 3
# # 122
# # 221
# # 112
# 일단 내가 생각한 알고리즘은
# 대각선 2개
# 가로, 세로
# 이렇게 총 3개를 탐색하는거다
# 일단 선생님이 부를숫자가 빙고판에 대응되기 때문에
# 빙고판 숫자를 하나 받아서
# 그 숫자를 일단 다 받은뒤
# 그 숫자를 찾아서 0으로 만들어준다
# 그리고 나서 리스트의 있는 숫자를 전부 0으로 만들어줬다면
# 이제 위의 세가지 알고리즘을 탐색하면서
# 빙고가 되나 확인한다
# 각각 줄이 완성되면 한개씩 반환하고
# 각가의 줄이 3개가 된다면 빙고니까
# 그때의 마지막 값을?


def bingo(board):
	arr = board
	n = len(board)
	r_bingo, l_bingo, bingo = 0, 0, 0
	# 가로
	for i in range(n):
		r_cnt =  0
		for j in range(n):
			if arr[i][j] == 0:
				r_cnt += 1
		if r_cnt == 5:
			r_bingo += 1
	# 세로
	for j in range(n):
		v_cnt = 0
		for k in range(n):
			if arr[k][j] == 0:
				v_cnt += 1
		if v_cnt == 5:
			l_bingo += 1

	bingo = r_bingo + l_bingo
	return bingo

def cross(board):

	arr = board
	n = len(board)
	r,l = 0, 0
	r_bingo, l_bingo, bingo = 0, 0, 0
	# 각각의 대각선을 확인해준다음에
	# 그 대각선이 5개라면 원빙고
	# 만약 10 개라면 투빙ㄱ
	for i in range(n):
		if arr[i][n-1-i] == 0:
			r_bingo += 1
		if arr[i][i] == 0:
			l_bingo += 1
	# 둘중에 하나만 빙고일 경우
	if r_bingo == 5:
		r += 1
	else:
		pass
	if l_bingo == 5:
		l += 1
	else:
		pass
	
	bingo = r + l
	return bingo 


dp = [[0 for _ in range(5)] for _ in range(5)]

n = 5
board = [list(map(int, input().split())) for _ in range(n)]
num = [list(map(int, input().split())) for _ in range(n)]

result = 0
for i in range(n):
	ar = num[i]
	# 5 10 7 16 2
	for j in range(n):
		# 5 10 7 16 2
		n_1 = ar[j]
		result += 1
		for k in range(n):
			for c in range(n):
				if board[k][c] == n_1:
					board[k][c] = 0
					if bingo(board) + cross(board) >= 3:
						print(result)
						exit()

# 드디어 맞았따



# 반례
# 14 12 5 11 13 
# 9 4 3 8 25 
# 18 15 19 24 20 
# 1 6 7 23 17 
# 22 16 10 2 21 
# 17 11 9 24 6 
# 23 1 2 15 12 
# 8 14 21 10 16 
# 3 22 18 13 25 
# 4 5 19 7 20
# 통과
# 18
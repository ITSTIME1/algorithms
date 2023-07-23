N, M, R = map(int, input().split())


dp = [[0 for _ in range(M)] for _ in range(N)]
dp_rotate = [[0 for _ in range(N)] for _ in range(M)]
graph = [input().split() for _ in range(N)]

# # 상하 반전시키기.
# # N = 0, 1, 2, 3, 4, 5
# for i in range(N):
# 	# M = 0, 1, 2, 3, 4, 5, 6, 7
# 	for j in range(M):
# 		dp[i][j] = graph[N-i-1][j] 
# print(dp)


# [['4', '5', '1', '9', '8', '2', '1', '3'], 
# ['1', '3', '2', '8', '7', '9', '2', '1'],
# ['2', '1', '3', '8', '6', '3', '9', '2'],
# ['5', '9', '2', '1', '9', '6', '1', '8'], 
# ['9', '7', '8', '2', '1', '4', '5', '3'], 
# ['3', '2', '6', '3', '1', '2', '9', '7']]

# 상하 바꾸는 연산 함수.
def dimensional_change_position_bottom_to_up(dp, graph):
	for i in range(N):
		for j in range(M):
			dp[i][j] = graph[N-i-1][j]
	return dp
print(dimensional_change_position_bottom_to_up(dp, graph))


# # 좌우 반전 시키는 연산 함수. 
def dimensional_change_position_left_to_right(dp, graph):
	for i in range(N):
		for j in range(M):
			dp[i][j] = graph[i][M-j-1]
	return dp

print(dimensional_change_position_left_to_right(dp, graph))

# [['7', '9', '2', '1', '3', '6', '2', '3'], 
# ['3', '5', '4', '1', '2', '8', '7', '9'], 
# ['8', '1', '6', '9', '1', '2', '9', '5'], 
# ['2', '9', '3', '6', '8', '3', '1', '2'], 
# ['1', '2', '9', '7', '8', '2', '3', '1'], 
# ['3', '1', '2', '8', '9', '1', '5', '4']]


# 오른쪽으로 rotate 하는 함수.
def diemensional_change_position_rotate_90_to_right(dp, graph):
	arr = []
	for i in range(M):
		tmp = []
		for j in range(N):
			tmp.append(graph[N-j-1][i])
		arr.append(tmp)

	# 만약 graph 에다가 변경해서 하고 싶다면
	# dp_rotate 하나를 다시 만들어서 부여한다.
	# rotate 하게 되면 N이 열이 되고 M 이 행이 되기 때문에
	# 범위를 주위한다.
	for i in range(M):
		for j in range(N):
			dp_rotate[i][j] = arr[i][j]
	return dp_rotate
print(diemensional_change_position_rotate_90_to_right(dp, graph))


# 왼쪽으로 rotate 하는 함수.
def diemensional_change_position_rotate_90_to_left(dp, graph):
	arr = []
	for i in range(M):
		tmp = []
		for j in range(N):
			# 7 0 1 2 3 4 5
			# grpah[7]
			tmp.append(graph[j][M-i-1])
		arr.append(tmp)

	for i in range(M):
		for j in range(N):
			dp_rotate[i][j] = arr[i][j]

	return dp_rotate
print(diemensional_change_position_rotate_90_to_left(dp, graph))

# 1/4 을 오른쪽 회전 시계방향 회전하는 함수.
def dimensional_change_position_rotate_90_to_right_1_4(dp,graph):
	div_N = N // 2 # 3
	div_M = M // 2 # 4
	for i in range(div_N):
		for j in range(div_M):
			# 1번 블록이 완성되고
			dp[i][j] = graph[div_N+i][j]
			# 2번 블록
			dp[i][div_M+j] = graph[i][j]
			# 3번 블록
			dp[div_N+i][div_M+j] = graph[i][div_M+j]
			# 4번 블록
			dp[div_N+i][j] = graph[div_N+i][div_M+j]
	return dp
print(dimensional_change_position_rotate_90_to_right_1_4(dp, graph))

# [['2', '1', '3', '8', '3', '2', '6', '3'],
#  ['1', '3', '2', '8', '9', '7', '8', '2'],
#  ['4', '5', '1', '9', '5', '9', '2', '1'],
#  ['6', '3', '9', '2', '1', '2', '9', '7'],
#  ['7', '9', '2', '1', '1', '4', '5', '3'],
#  ['8', '2', '1', '3', '9', '6', '1', '8']]

def dimensional_change_position_rotate_90_to_left_1_4(dp, graph):
	div_N = N // 2 # 3
	div_M = M // 2 # 4

	for i in range(div_N):
		for j in range(div_M):
			dp[i][j] = graph[i][div_M+j]
			dp[i][div_M+j] = graph[div_N+i][div_M+j]
			dp[div_N+i][div_M+j] = graph[div_N+i][j]
			dp[div_N+i][j] = graph[i][j]
	return dp
print(dimensional_change_position_rotate_90_to_left_1_4(dp,graph))

# [['1', '2', '9', '7', '6', '3', '9', '2'],
#  ['1', '4', '5', '3', '7', '9', '2', '1'],
#  ['9', '6', '1', '8', '8', '2', '1', '3'],
#  ['3', '2', '6', '3', '2', '1', '3', '8'],
#  ['9', '7', '8', '2', '1', '3', '2', '8'],
#  ['5', '9', '2', '1', '4', '5', '1', '9']]

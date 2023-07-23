# 사탕게임
# 문제분석
# 완전탐색인데

# 색이 다른 인접한 칸을 골라서
# 해당 위치를 스와프 한다음에\
# 같은 색이 있는 위치를 width height 각각 검사해서
# 색이 가장 큰 값을 리턴한다
# CCP
# CCP
# PPC
# 이런경우에 cp 를 한번씩 바꾸면서
# 가로 세로 색상이 같은 가장 큰 행 또는 열 을 찾아서
# 같은 색이 몇인지 리턴하면 된다
# 1. 1행에 cp 를 서로 자리를 바꾸면
# cpc
# ccp
# ppc
# 가 되는데 이때 가로의 최대는 2 세로의 최대 도 2이다
# 그 다음 행으로 넘어가서 pc를 만들면 세로의 값으로 3 이 된다.

# 이 예제를 보니까
# 문자열을 바꾼 다음에
# 그 인접한 곳을 교환후
# 완전탐색을 진행하는데 
# 그 완전탐색을 진행하면서
# 이어져있는 색상중 가장 큰 값을 리턴한다면
# 이걸 다시 돌려놔야 되나?

# 예제 에서 찾을 수 있다
# 힌트를 준 이유는 만약
# 힌트의 행 4번을 바꾸게 되면
# c를 4개를 먹을 수 있다고 한다
# 출력값 또한 4개로 나온걸 볼 수 있고
# 최대로 많이 먹은 사탕을 뜻한다
# 자 여기서 유추 해볼 수 있는건
# 먼저 4행을 바꿨을때 최대로 먹을 수 있다는 것이다
# 근데 만약 위에서 우리가 그럼 이전의 바꿔 놓았던 문자들은 다시 돌려야 하나 ?
# 이 문제가 해결이 된다
# 왜냐하면 만약 2행의 CY가 다르기 때문에 서로 스와핑을 했다고 가정한다
# 그렇게 되면 힌트에서 처럼 4행을 바꿨을때 처럼 c를 4개를 먹을 수 없다
# 왜냐 YC가 바뀐 상태가 되어있기 때문에 불가능하다
# 따라서 인접한 것을 바꿀때마다 검사를 한뒤 
# 다시 문자열을 바꿔놓아야 된다는 걸 의미한다 = 이 말은 곧 4행을 바꿨을 때 c를 최대로 먹을 수 있다는걸 뜻하기 때문이다.
# YCPZY
# CYZZP
# CCPPP
# YCYZC
# CPPZZ
N = int(input())
color = [list(input()) for _ in range(N)]

total = 0
# 연속된 숫자는 계속 더해주는거
# 만약 연속되지 않은 숫자가 되었을때
# 연속된 숫자가 누적이 되면 안되기 때문에
# 초기화시켜준다
# 연속된 시점에 몇개의 숫자가 연속되었는지를 그때 리턴해주면 그 행의 연속된 숫자가 된다.
def width(color, n):
	global total
	arr = color
	for i in range(n):
		c = 1
		for j in range(n-1):
			if arr[i][j] == arr[i][j+1]:
				c+=1
				total = max(c, total)
			# 이걸 생각을 못했네
			# 누적이 되지 않도록 다르다면 초기화 시켜준다.
			# 다른게 누적이 되어야 하니까
			# 왜냐하면 ccczadddd 라고 환다면 ccc 까지 총 3개가 total로 들어가고
			# cz 일 경우 이미 연속이 끊겼기 때문에
			# 다시 초기화 시켜준다 하지만 total 값은 변화가 없고 그 이후에 dddd 값일 경우
			# total 값보다 c값이 더 커지므로
			# total 값으로 들어가게 된다.
			else:
				c=1

def height(color, n):
	global total
	arr = color
	for i in range(n):
		c = 1
		for j in range(n-1):
			if arr[j][i] == arr[j+1][i]:
				c+=1
				total = max(c, total)
			else:
				c=1

for i in range(N):
	# 한칸씩 비교할거기 때문에
	h_count, v_count = 0, 0
	for j in range(N-1):
		# 만약에 인접한 부분이 같지않다면
		# 완전탐색 시전
		if color[i][j] != color[i][j+1]:
			# 스와핑
			color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
			width(color, N)
			height(color, N)
			# 사탕의 최대값
			# 원상복귀 시켜주고
			color[i][j], color[i][j+1] = color[i][j+1], color[i][j]
		# 열의 원소는 생각을 안했네
		if color[j][i] != color[j+1][i]:
			# 스와핑
			color[j][i], color[j+1][i] = color[j+1][i], color[j][i]
			width(color, N)
			height(color, N)
			# 사탕의 최대값
			# 원상복귀 시켜주고
			color[j][i], color[j+1][i] = color[j+1][i], color[j][i]
print(total)

# 누적되는걸 왜 찾지 못했을까..
# 분명 누적이 될텐데..

# 6
# CCYYCC
# YYCCYY
# CCYYCC
# YYCCYY
# CCYYCC
# YYCCYY

# 답->3

# 5
# CPZCC
# ZYCPZ
# CYYPZ
# ZPZCC
# CCPYY

# 답->3


# 6
# CCYYCC
# YYCCYY
# CCYYCC
# YYCCYY
# CCYYCC
# YYCCYY
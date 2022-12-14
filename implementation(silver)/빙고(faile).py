# 이 문제는 일단
# 몇번째의 빙고를 외치게 되냐 이다
# 즉 점이 3개 이상인 시점에 그 수를 저장하고 break 하면 된다
# 즉 최악의 경우 행렬 전체를 거의다 돌겠지만
# 예제1번과 같이 행렬의 수를 다 쓰지 않고도 빙고가 가능하다.




# 사회자가 부른 수를 가지고 오면서
# 그 수의 해당하는 위치를 0 으로 바꿔 줄것이다
# 그리고 3개의 포문을 돌건데
# 1. 대각선 포문 대각선을 검사 했을 때 모두가 다 0 이라면 cnt + =1 올려주면서 하나의 선이 완성 되엇고
# 2. 다음은 가로 포문 가로 포문을 검사했을때 한줄당 0이 총 개수만큼 나온다면 cnt += 1
# 3. 세로 포문또한 배열을 검사하면서 0 5개가 된다면 cnt + =1

# 이렇게 한번 숫자를 부를때마다 탐색을 시전하고 3개의 포문이 종료되고 난 후
# cnt 개수가 3보다 크다면 해당 수를 불렀을때 몇번재 인덱스엿는지
# result 값의 넣어놓고
# break 를 통해서
# 프로그램을 종료한


# 대각선
def cross(bingo):
	arr = bingo
	N = len(bingo)
	rcnt, lcnt = 0,0 
	for i in range(N):
		if bingo[i][N-1-i] == 0:
			rcnt += 1
		if bingo[i][i] == 0:
			lcnt += 1
	if rcnt == 5 or lcnt == 5:
		return 1
	else:
		return 0 
# 수직
def vertical(bingo):
	arr = bingo
	N = len(bingo)
	total = 0
	for i in range(N):
		cnt = 0
		for j in range(N):
			if bingo[j][i] == 0:
				cnt += 1
		if cnt == 5:
			total+=1
			break
	if total == 1:
		return 1
	else:
		return 0
# 수평
def horizontal(bingo):
	arr = bingo
	N = len(bingo)
	total = 0
	for i in range(N):
		cnt = 0
		for j in range(N):
			if bingo[i][j] == 0:
				cnt += 1
		if cnt == 5:
			total+=1
			break
	if total == 1:
		return 1
	else:
		return 0
N = 5
bingo = [list(map(int, input().split())) for _ in range(N)]
teacher = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
	for j in range(N):
		# 선생님의 숫자를 하나 씩 가지고 와서
		# 그 숫자의 인덱스를 찾아서 빙고판을 바꿔준다
		num = teacher[i][j]
		cnt+=1
		for k in range(N):
			for c in range(N):
				# 빙고를 다 돌았을때 해당 값이 있다면 그 해당 값의 빙고판을 바꿔주고
				# 각각 대각선 수직 수평을 다 검사한다음에
				# 대각선이라면 대각선 0의 개수가 5개가 되었다면 return 1을 보내준다
				# 수직을 검사했을때 0의 개수가 5개라면 cnt 를 보내준다
				# 수평도 마찬가지로 이런식으로 cnt 를 보내주면서
				# 만약 cnt가 모여 3이 되는 순간
				# 프로그램을 종료하고 num의 값을 리턴한다
				# 후에 그 값이 인덱스 몇인지 확인한 후 출력
				if bingo[k][c] == num:
					bingo[k][c] = 0
					c = cross(bingo)
					v = vertical(bingo)
					h = horizontal(bingo)
					if c == 1 and v == 1 and h == 1:
						print(cnt)
						exit()
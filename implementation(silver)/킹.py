# 문제분석

# 8*8 의 체스판이 있고
# 킹의 현재 위치가 주어짐
# 알파벳과, 숫자로 2차원 배열을 표시하는데
# 알파벳 = 열
# 숫자 = 행

# 열은 가장 왼쪽 a
# 행은 가장 아래가 1 가장 위가 8(사실상 1~8까지라ㅗㄱ 생각하기 쉬운데)
# 이건 행의숫자가 반대
# 움직이는 횟수가 끝났을때 돌의 위치랑 킹의 위치를 출력하면되고

# 킹이 돌의 위치로 이동할때
# 킹이 움직인 방향과 같은 방향으로 돌을 이동시킴
# 만약 킹이 왼쪽으로 이동해야 돌의 위치로 갈 수 있다면
# 돌또한 한칸 왼쪽으로 움직여줌

# 만약 킹이 한칸 위쪽으로 움직여야 한다면
# 돌 또한 한칸 위쪽으로 움직여줌


# 킹과 돌의 마지막 위치를 구하는 프로그램을 작성
# 움직임이 총 8가지
# 북, 남, 동, 서
# 기본 4가지에 + 4가지를 더한 방향

ch = 8
# 알파벳을 매칭시켜주고
alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
# 2차원 배열을 만든다음
matrix = [[0 for _ in range(ch)] for _ in range(ch)]
# 킹, 돌, 횟수
# 돌과 킹의 위치 둘다 2차원 배열에 표시해주고
# A1 = A, 1
king, dol, n = input().split()
# 방향
dirt = [input() for i in range(int(n))]
# 방향벡터
# R, L, B ,T , RT, LT, RB, LB
# 각각의 방향벡터로 정하면 될거 같은데
# 이거 좌표 벡터가 반대로 되어야 될거 같은데

dx = {"R": 0, "L": 0, "B": 1, "T": -1, "RT": -1, "LT": -1, "RB": 1, "LB": 1}
dy = {"R": 1, "L": -1, "B": 0, "T": 0, "RT": 1, "LT": -1, "RB": 1, "LB": -1}


# 체스판 밖으로 나간다면 그 이동은 건너 뛰고
# 즉 해당 이동은 하지 않는다
# 킹이 있었던 위치가 이동한다면 킹은 :1 돌: 2로 정했으니까
# 킹, 돌이 이 움직였던 자리는 다시 0
# 킹이 새로 움직인 자리는 1 돌이 새로 움직인 자리는 2
#

# 킹의 위치를 열 과 행으로 받아서 각각 더해야 하니까



# 현재 킹과 돌의 위치
kingX, kingY = ch-int(king[1]), alphabet[king[0]] 
dolX, dolY = ch-int(dol[1]), alphabet[dol[0]] 
for i in dirt:
	# 방향을 갖고 오면 우선
	# 해당 k_z, d_z 에 해당 방향만큼 더해봐서
	# 그 더한 값들이 체스판을 넘긴다면
	# break 하고
	# 그렇지 않다면 이동을 시도
	while True:
		# 킹의 방향
		nx = kingX + dx[i]
		ny = kingY + dy[i]

		# 만약 범위를 넘어간다면 break 하고
		if nx < 0 or nx > ch-1 or ny < 0 or ny > ch-1:
			break
		# 만약 현재 설정된 범위에서 킹의 값이 = 돌의값의 위치랑 같다면
		# 돌도 dx[i], dy[i] 만큼 이동하고 킹도 좌표업데이트
		# 만약 킹의 값이 ! = 돌의 값이 아니라면 킹의 값만 업데이트
		if nx == dolX and ny == dolY:
			ndolX = dolX + dx[i]
			ndolY = dolY + dy[i]
			# 돌 업데이트 해주고 킹도 같이 업데이트
			if ndolX < 0 or ndolX > ch-1 or ndolY < 0 or ndolY > ch-1:
				break
			else:
				kingX, kingY = nx, ny
				dolX, dolY = ndolX, ndolY
				break
		else:
			kingX, kingY = nx, ny
			break
# 7, 0 = a1
# 6, 0 = a2
# 리버스

# 예제 5, 6 case faile

reversed_alphabet = dict(map(reversed, alphabet.items()))
print(reversed_alphabet[kingY] + str(ch-kingX))
print(reversed_alphabet[dolY] + str(ch-dolX))
# [[0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0]]


 # 이런 체스판에서 행이 가장 아래쪽부터 1이 시작한다고 했고
 # 열은 1열부터 a 2열 b 3열 c

 # 그럼 일단 2차원 배열로 움직이고
 # 만약 킹의 위치가 c,2 가 실제 위치라면
 # 6,2 a,b,c,d 를 숫자와 매칭시켜서 맞는 숫자로 바꿔주면
 # 2 = c가 되고
 # 행은 6이니까 전체행 - 나온행(6) = 2
 # 2,c 그럼 이걸 알파벳순서대로 바꾸주면 c2
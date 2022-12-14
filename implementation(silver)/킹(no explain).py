
ch = 8

alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

# 필요없음.
# matrix = [[0 for _ in range(ch)] for _ in range(ch)]


king, dol, n = input().split()

dirt = [input() for i in range(int(n))]


dx = {"R": 0, "L": 0, "B": 1, "T": -1, "RT": -1, "LT": -1, "RB": 1, "LB": 1}
dy = {"R": 1, "L": -1, "B": 0, "T": 0, "RT": 1, "LT": -1, "RB": 1, "LB": -1}

kingX, kingY = ch-int(king[1]), alphabet[king[0]] 
dolX, dolY = ch-int(dol[1]), alphabet[dol[0]] 
for i in dirt:

	while True:
		nx = kingX + dx[i]
		ny = kingY + dy[i]
		if nx < 0 or nx > ch-1 or ny < 0 or ny > ch-1:
			break

		if nx == dolX and ny == dolY:
			ndolX = dolX + dx[i]
			ndolY = dolY + dy[i]
			if ndolX < 0 or ndolX > ch-1 or ndolY < 0 or ndolY > ch-1:
				break
			else:
				kingX, kingY = nx, ny
				dolX, dolY = ndolX, ndolY
				break
		else:
			kingX, kingY = nx, ny
			break

reversed_alphabet = dict(map(reversed, alphabet.items()))
print(reversed_alphabet[kingY] + str(ch-kingX))
print(reversed_alphabet[dolY] + str(ch-dolX))

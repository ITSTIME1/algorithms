import copy

R, C = map(int, input().split())
card = []
for _ in range(R):
	card.append(list(input()))


A, B = map(int, input().split())

# 오른쪽 위 부분 대칭
# 2 2
for i in range(R):
	row = []
	for j in range(C-1, -1, -1):
		print(j)
		row.append(card[i][j])
	card[i].extend(row)

# extend 를 통해서 오른쪽 대칭 되어지는 걸 만들어주고
print(card)

# 아래부분 대칭 이해됨
for i in range(R-1, -1, -1):
	row = copy.deepcopy(card[i])
	card.append(row)
print(card)

for c in card:
	print("".join(c))
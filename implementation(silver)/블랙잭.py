N, M = map(int, input().split())
card = list(map(int, input().split()))


total = []

for i in range(len(card)-2):
	for j in range(i+1, len(card)-1):
		for k in range(j+1, len(card)):
			if card[i] + card[j] + card[k] <= M:
				total.append(card[i] + card[j] + card[k])
total.sort()
print(total[len(total)-1])


# 문제분석

# 이거 그거 같은데
# D[1] = A 첫수자는 정해져잇고
# D[n] 번부터는 각 자리으 ㅣ숫자를 곱한 값

# 반복되는 첫 시작부터 첫 값과 반복되는 첫 시작 값이 나온다면 그 부분까지를 다 빼고
# 남은 수열
# 결국 같은 숫자가 두번 나올때부터자나

a, p = map(int, input().split())

d, x, ans = [a], 0, 0 
while True:
	for i in d:
		c = list(str(i))
		idx = 0
		for j in range(len(c)):
			idx += int(c[j])**p
		if idx not in d:
			d.append(idx)
		else:
			x = 1
			ans = d.index(idx)
			break
	if x == 1:
		print(len(d[:ans]))
		break
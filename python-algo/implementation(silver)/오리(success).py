import sys
word = ["q", "u", "a", "c", "k"]
string = list(sys.stdin.readline().strip())
n = len(string)
q_arr = [_ for _ in range(n) if string[_] == "q"]
dp = [0] * n
total, x = 0, 1
# 문자열이 정상적인 개수가 아닐때
if n % 5 != 0:
	x = 0
while True:
	cm = 0
	for i in q_arr:
		if dp[i] == 1:
			cm += 1
	if cm == len(q_arr):
		if total == 0:
			total = -1
		if total >= 0 and 0 in dp:
			total = -1
		break
	else:
		com = ""
		ori = 0
		z = 0 
		for i in range(len(string)):
			if string[i] == word[z] and dp[i] != 1:
				# 6, 4
				dp[i] = 1
				com += string[i]
				z += 1
				if com == "".join(word):
					ori += 1
					com = ""
					z = 0
		# 한번 문자열을 전부다 탐색 했을 때
		# ori 의 값이 1개 이상이라면 오리 한마리이므로
		# total 값을 하나 증가시켜준다.
		if ori >= 1:
			total += 1
# 문자열이 맞지 않을때 문자열은 길이가 5인데 보통 5의 길이가 안된다면
# 문자열이 완성될 수가 없음

if x == 0:
	print(-1)
else:
	print(total)

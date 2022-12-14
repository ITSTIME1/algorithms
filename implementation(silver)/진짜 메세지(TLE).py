from string import ascii_uppercase
import sys

alphabet_list = list(ascii_uppercase)
dp = dict()
for i in alphabet_list:
	dp[i] = 0

#O(2N) 100,000 * 2 = 200,000 시간안에 들어오는데..?
# 내일 다시 풀어보자
T = int(sys.stdin.readline().strip())
for i in range(T):
	c = 0
	string = list(sys.stdin.readline().strip())
	word = []
	# AABA
	# ABCABCBBAAA
	# ABCABCBBAA
	# ABCABCBBAAACC

	for j in range(len(string)):
		dp[string[j]]+=1
		if dp[string[j]] == 3:
			dp[string[j]] = 0
			word.extend(string[j] * 2)
			if "".join(word) == "".join(string[:j+2]):
				c = 2
			else:
				c = 1
		else:
			if c == 2:	
				c = 0
			else:
				word.append(string[j])

	for i in dp:
		dp[i] = 0

	if c == 1:
		print("FAKE")
	else:
		print("OK")
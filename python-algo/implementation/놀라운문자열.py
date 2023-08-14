import sys

while True:
	string = input().strip()
	if string == '*':
		break

	flag = True
	for i in range(len(string)-1):

		check = []
		answer = 0
		for j in range(len(string)-(i+1)):
			for k in range(i+j+1, (i+j+1)+1):

				word = string[j] + string[k]

				if word not in check:
					check.append(word)
				else:

					answer += 1
					break

		if answer != 0:
			print(f'{string} is NOT surprising.')
			flag = False
			break

	if flag:
		print(f'{string} is surprising.')

# 0쌍
i = 0, j = 0, k = 1
i = 0, j = 1, k = 2
i = 0, j = 2, k = 3

# 1쌍
i = 1, j = 0, k = 2
i = 1, j = 1, k = 3

# 2쌍
i = 2, j = 0, k = 3
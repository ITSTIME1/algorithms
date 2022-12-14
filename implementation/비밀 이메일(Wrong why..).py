import sys

string = list(sys.stdin.readline().strip())

# R
divisor_list = []
# C
remainder_list = []
N = len(string)
div = len(string)

# 약수를 구해주고
while True:
	div = div // 2
	divisor_list.append(div)
	if div < 2:
		break
# [8, 4, 2, 1]
for i in divisor_list:
	rem = N // i
	remainder_list.append(rem) 
# c>=r 을만족하는 값 중에서
# 여러개일 경우 R이 가장 큰 값을 선택하고
max_divi = []
matrix_R = 0
matrix_C = 0
# [3, 1]
# [2, 6]
if len(divisor_list) > 1:
	cnt = 0
	for n in range(len(divisor_list)):
		if remainder_list[n] >= divisor_list[n]:
			max_divi.append(divisor_list[n])
			cnt += 1
	if cnt > 1:
		matrix_R = max(max_divi)
		matrix_C = remainder_list[divisor_list.index(matrix_R)]
	else:
		matrix_R = divisor_list[0]
		matrix_C = remainder_list[divisor_list.index(divisor_list[0])]
else:
	matrix_R = divisor_list[0]
	matrix_C = remainder_list[divisor_list.index(divisor_list[0])]

dp = [[0 for _ in range(matrix_R)] for _ in range(matrix_C)] 
# 행렬에 문자를 넣어주고
# R = 3
# C = 2

for i in range(matrix_R):
	for j in range(matrix_C):
		dp[j][i] = string[j]
	del string[:matrix_C]
# [[0, 0, 0], 
# [0, 0, 0]]
	
result_string = []
for n in dp:
	result_string.append("".join(n))
print("".join(result_string), end = "")	
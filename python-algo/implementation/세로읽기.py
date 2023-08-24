# 세로 읽기니까
# 가장 긴 단어를 기준으로 일겅야하겠네


import sys
input = sys.stdin.readline

n = 5
arr = []
max_length = 0
for i in range(n):
	string = input().strip()
	arr.append(list(string))
	max_length = max(max_length, len(string))


for idx, value in enumerate(arr):
	if len(value) < max_length:
		
		remain = max_length - len(value)

		for _ in range(remain):
			arr[idx].append(".")

		arr[idx] = "".join(value)

	else:
		arr[idx] = "".join(value)

result = ""
for r in range(max_length):
	for c in range(n):
		if arr[c][r] != ".":
			result += arr[c][r]
print(result)

# 가장 길이가 긴 단어를 중심으로 읽어야 하기 때문에
# 가장 길이가 긴 문자열의 길이를 중심으로 ""채워야 할거 같은데
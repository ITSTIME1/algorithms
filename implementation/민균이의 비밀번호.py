N = int(input())
arr = [input() for _ in range(N)]

result_len = 0
string_index = "none"
for i in range(len(arr)):
	string = list(arr[i])
	string.reverse()
	# 새로운 문자열을 하나 만들어서
	for j in range(len(arr)):
		if "".join(string) in arr[j]:
			result_len = len(string)
			string_index = string[len("".join(string))//2]
			break
		else:
			pass

print(result_len, string_index)

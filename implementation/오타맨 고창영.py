T = int(input())

for _ in range(T):
	w, s = map(str, input().split())

	result = []
	for i in range(len(s)):
		if i != int(w)-1:
			result.append(s[i])
	print("".join(result))

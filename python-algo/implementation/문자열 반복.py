T = int(input())

for i in range(T):
	R, S = input().split()
	new_string = ""
	for j in range(len(list(S))):
		ch = int(R) * S[j]
		new_string+=ch

	print(new_string)

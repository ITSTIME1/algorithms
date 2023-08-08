import sys
input = sys.stdin.readline

string = input().strip()

answer = ""
for i in range(len(string)):
	if string[i].isupper():
		answer += string[i].lower()
	else:
		answer += string[i].upper()

print(answer)

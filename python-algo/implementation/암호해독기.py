from string import ascii_lowercase, ascii_uppercase
from collections import Counter
n = int(input())
s = list(map(int, input().split()))
string = input().strip()

check = Counter(s)
word = {" " : 0}

a = list(ascii_lowercase)
b = list(ascii_uppercase)

total = 26 * 2
for i in range(total):
	if total // 2 > i:
		word[b[i]] = i+1
	else:
		word[a[i-total]] = i+1

tmp = [word[string[i]] for i in range(len(string))]

tmp.sort()
s.sort()

if tmp == s:
	print("y")
else:
	print("n")
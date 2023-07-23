
import sys
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
m_arr = list(map(int, sys.stdin.readline().strip().split()))


dic = {}
for i in arr:
	if i not in dic:
		dic[i] = 0
result = ""
for i in m_arr:
	if i in dic:
		result+='1 '
	else:
		result+='0 '
print(result)
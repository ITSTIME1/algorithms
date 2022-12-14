# 문제분석

# 파일의 확장자 개수를 파악하고
# 해당 파일의 확장자를 알파벳순서대로 나열하고
# 그 나열한 파일의 확장자가 얼마나 있는지 개수로 파악하면 된다.

import sys

N = int(sys.stdin.readline().strip())
string = [sys.stdin.readline().strip() for _ in range(N)]
dic = {}

# O(nlogn)
string.sort(key = lambda x : x.split(".")[1])

for i in range(N):
	dic[string[i].split(".")[1]] = 0
# O(n^2) = 25억 = 25초
# O(logn) = 15억 = 15초
# O(3N) = 150000

for i in string:
	dic[i.split(".")[1]] += 1

for i in dic:
	print(i, dic[i])




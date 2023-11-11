
import sys
from collections import Counter
input = sys.stdin.readline


n = int(input())
while n > 0:

	arr = list(map(int, input().split()))
	t = arr[0]
	human = arr[1:]

	div = (t // 2) + 1

	# 땅의 개수만큼 맞추고
	dic = Counter(human)

	flag = True
	for key,value in dic.items():
		if value >= div:
			print(key)
			flag = False
			break

	if flag:
		print("SYJKGW")
	n -= 1
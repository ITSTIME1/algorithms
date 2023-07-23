# 문제분석

# 최대 만개 종이 주어지고
# 100만개의 그루의 나무가 주어진다

# 미국 전역의 나무들이 주어졌을 때, 각 종이 전체에서 몇 % 를 차지하는지
# 그럼 각종으 그루수 / 전체 나무수 * 100 

import sys

arr = {}
cnt = 0
while True:
	try:
		string = sys.stdin.readline().strip()
		if string == "":
			break
		cnt += 1
		if string not in arr:
			arr[string] = 1
		else:
			arr[string] += 1
	except:
		break

ar_sort = sorted(arr.items())

for i in ar_sort:
	print(i[0] + " " + f'{i[1] / cnt * 100:.4f}')
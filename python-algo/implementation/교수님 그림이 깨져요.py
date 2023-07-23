N, K = map(int, input().split())

arr = [input().split() for _ in range(N)]

result = []
cnt = []
# O(N^2) + O(N)
# O(N^2+2N)
for i in range(len(arr)):
	check = arr[i]
	for j in range(len(check)):
		# 상수 * k 
		result.extend(check[j] * K)
	cnt.append([result[:N*K]])
	result.clear()

for j in cnt:
	c = j*K
	for k in c:
		print(*k)
# ['0', '0', '1', '1', '1', '1', '0', '0']
# N*K 개씩 나눠서 가지고오고

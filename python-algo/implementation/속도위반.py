import sys
input = sys.stdin.readline

arr = [0] * 100
arr1 = [0] * 100

n, m = map(int, input().split())

start = 0
for _ in range(n):
	dist, limit = map(int, input().split())

	for i in range(start, start+dist):
		arr[i] = limit

	start += dist

start = 0
for _ in range(m):
	dist, limit = map(int, input().split())

	for i in range(start, start+dist):
		arr1[i] = limit

	start += dist


# 그랬을때 어떤 구간에서 변경점이 온다면 그 변경점에서도 얼마만큼 속력을 벌렸는지가 나오니까
# 연정이의 속력이 더 높다면 제한속도보다 더 높다면 당연히 연정이가 위반한거니까

tmp = 0
for i in range(100):
	# 연정이의 속력이 더 크다면
	# 연정이가 속력을 위반 한것이므로
	# 속력을 위반했기 때문에 차이가 생길거니까
	if arr1[i] > arr[i]:
		diff = arr1[i] - arr[i]
		tmp = max(tmp, diff)

print(tmp)







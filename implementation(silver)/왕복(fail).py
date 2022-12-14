import time 
c = time.time()

N, K = map(int, input().split())
num = list(map(int, input().split()))

result = 0
while True:
	if K < 0:
		print(result)
		break
	x = 0 
	for i in range(N):
		K-=num[i]
		if K < 0:
			result = i+1
			x = 0
			break
		else:
			x = 1

	# 왕복부분 이 왕복부분은 아직 지점을 찾지 못했을 때이다
	if x == 1:
		for j in range(N-1, -1, -1):
			K-=num[j]
			if K < 0:
				result = j+1
				break
		
print(time.time() - c)

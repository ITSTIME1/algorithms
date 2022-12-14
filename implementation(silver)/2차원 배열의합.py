N, M = map(int, input().split())

# 숫자를 넣을
dp = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
	# 값이 10000 가지 들어오기 때문에
	# k 가 만 까지 루프를 도니까
	i, j, x, y = map(int, input().split())
	# (i,j) 에서 (x,y) 까지의 합은 누적합이다
	# 즉 i~x 까지 j~y의 합을 구해라 라는 말이 된다.
	# 1123
	

	# O(N^2)
	# N = 90000 + 10000 = 100000

	# K = 1 최악의 경우 300 * 300 =  90000
	# K = 2 180000
	# K = 3 270000
	#....
	# K = 10000 * 90000 총 토탈 시간 9억 1초에 1억이라고 생각해도
	# 약 9초... 제한 시간 2초,..
	# 다른걸로 풀어야 된다
	# 하지만 2차원 배열의 생각을 얻었음.
	# 0, 1 리스트 돌고
	result = 0
	for n in range(i-1, x):
		for m in range(j-1, y):
			result += dp[n][m]

			# K = 10000
			# x, y = 90000 
	print(result)

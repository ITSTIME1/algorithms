# 문제분석

import sys

# 범위를 바꾸고
n = int(sys.stdin.readline())


# 메모리에서 걸리네
num = [i for i in range(1, n+1)]
end = 0
interval_sum = 0

ans = 0

for start in range(n):
	# 구간의 합도 n 보다 작고, 끝 값도 n 보다 작을때 까지만 반복을 해서
	while interval_sum < n and end < n:
		# 현재의 end 값을 더해주면서 end 값을 한칸씩 늘린다는 의미는 구간의 합이 증가한다는 의미이기 때문에
		# 구간의 합이 증가하게 되면 원하는 N의 값의 가까워진다는 의미가 된다.
		# 따라서 만약 구간의 합이 원하는 값보다 크거나 같아진다면
		# while 문을 종료시키고
		interval_sum += num[end]
		end += 1

	# 그게 우리가 원하는 값이라면
	# 구간의 합이 == n인 가짓수를 구해야 하기 때문에
	# ans 를 하나 증가시켜준다 
	if interval_sum == n:
		ans += 1

	# 만약 interval_sum 이 우리가 구하고자 하는 값이 아닐경우
	# ans 는 올리지 않고 현재 start 값을 빼서 구간의 합을 낮춘상태로
	# 다시 한번 반복하게 된다.
	# 결과적으로 num 안에 있는 모든 배열을 탐색하게 되므로 결국엔 start 가 n-1 까지 도착하게 되니까
	# O(n) 의 시간복잡도 즉 선형시간안에 동작한다고 볼 수 있다.
	interval_sum -= num[start]

print(ans)


import sys

n = int(sys.stdin.readline())

end, start, total = 0, 0, 0


ans = 0

# while 문이 종료되는 시점은 
# end 값이 n을 넘은시점이기 때문에
# while 문 종료
# end <= n 이라는건 n 이하일때 동안 반복을 해서
# 해당 구간의 합을 찾으라는 의미이기 때문에
# 만약 합이 n보다 작다면 end += 1 올려주고
# total end 값을 더해준다
# 만약 그 total 값이 = n 이라면 ans += 1 올려주고 end + =1 올려준다음
# total 에 더해준다
# 만약 그 total 값이 n 보다 크거나 같다고 한다면 start 만큼의 값을 빼준다음
# start + =1 증가시켜주고 다시 반복하기 시작한다
# start 가 증가한다는건 그만큼 total 의 값이 그만큼 감소한다는 의미이므로
# 값이 초과된다면 당연히 값을 줄여 구간의 합을 다시 구해야 한다.
while end <= n:

	if total < n:
		end += 1
		total += end
	elif total == n:
		ans += 1
		end += 1
		total += end
	else:
		total -= start
		start += 1
print(ans)


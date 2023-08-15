# 그리디
import sys
input = sys.stdin.readline

n = int(input())

snow = list(map(int, input().split()))
l = len(snow)

time = 0
while snow.count(0) != l:
	# 큰순서대로 정렬
	snow.sort(key=lambda pri : -pri)
		
	# 0보다 큰 수가 한개 보다 많을떄
	if l - snow.count(0) > 1:
		snow[0] -= 1
		snow[1] -= 1
	# 0보다 큰 수가 하나보다 적가나 같을떄
	else:
		snow[0] -= 1
	time += 1

if time > 1440:
	print(-1)
else:
	print(time)

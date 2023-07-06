# 내리는 위치에 도달하게 되면 즉시 짐을 내린다고 한다.
# 짐은 벨트 위에서 스스로 이동한다고 하낟
import sys
from collections import deque
input = sys.stdin.readline

# 컨베이어 벨트의 길이, 0의개수
n, k = map(int, input().split())

# 벨트의 내구도를 포함
belt = deque(list(map(int, input().split())))
robot = deque([False]) * (2*n)

cnt = 0

while True:
	# 1
	belt.rotate(1)
	robot.rotate(1)

	if robot[n-1] == True:
		robot[n-1] = False

	# 2
	for i in range(n-1, -1, -1):
		if robot[i] == True and robot[i+1] == False and belt[i+1] >= 1:
			robot[i] = False
			robot[i+1] = True
			belt[i+1] -= 1

	if robot[n-1] == True:
		robot[n-1] = False
	

	if robot[0] == False and belt[0] > 0:
		robot[0] = True
		belt[0] -=1 
	
	cnt += 1	

	zero = belt.count(0)
	if zero >= k:
		break

# 아오 ㅈ같은 문제 
print(cnt)

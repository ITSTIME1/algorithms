import sys 
from collections import deque
input = sys.stdin.readline

# n 트럭개수
# w 는 다리 길이
# l은 최대하중
n, w, l = map(int, input().split())


load, truck = deque([0] * w), deque(list(map(int, input().split())))



time = 0

# 리스트로 접근해보면 참신하네.
while True:
	if len(truck) == 0 and load.count(0) == len(load):
		break
	# 트럭이 올라올 수 있는 조건은 로드에 마지막이 비었을때
	# 그리고 최대하중보다 작거나 같을때만 올라올 수 있음
	# 그렇지 못한 경우는 load에 있는 것들만 옮겨질뿐
	# 만약 마지막게 비어있지 않다면
	# 못올라가는거고 기존에 있던 것들만 옮긴다.
	# 마지막이 비어있지 않다면	
	# for i in range(1, len(load)):
	# 	load[i-1] = load[i]
	# 	load[i] = 0
	# 음 리스트로 접근해본다면
	if load[-1] == 0:	
		if truck and sum(load) + truck[0] <= l:
			load[-1] = truck.popleft()
		else:
			load.popleft()
			load.append(0)
			if truck and sum(load) + truck[0] <= l:
				load[-1] = truck.popleft()
	else:
		load.popleft()
		load.append(0)
		if truck and sum(load) + truck[0] <= l:
			load[-1] = truck.popleft()


	time += 1
print(time)


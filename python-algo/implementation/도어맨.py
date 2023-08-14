import sys
from collections import deque 

input = sys.stdin.readline

x = int(input())

h = deque(list(input().strip()))

# 남, 여
gender = [0, 0]

# 둘의 차이가 x보다 작을때 동안
total = 0
pre = ""


# 1명만 남을 수도 있구나
# 그러네 한명만 남을때는 뒤에 있는 사람을 체크하지 못하니까
while max(gender) - min(gender) <= x:
	if len(h) == 0 or x == 0:
		pre = ""
		break
	if max(gender) - min(gender) == 0:
		if h[0] == "M":
			gender[0] += 1
			pre = "M"
		else:
			gender[1] += 1
			pre = "W"
		h.popleft()
	else:
		# 둘의 비율이 같지 않다라는거니까
		if gender[0] < gender[1]:
			# 남자 비율이 더 작다면
			if h[0] == "M":
				h.popleft()
				gender[0] += 1
				pre = "M"
				continue
			elif len(h) != 1 and h[1] == "M":
				# 이럴때는 두번째를 배주어야 하니까
				del h[1]
				gender[0] += 1
				pre = "M"
			else:
				h.popleft()
				gender[1] += 1
				pre = "W"
		else:
			# 여자 비율이 더 작다면
			if h[0] == "W":
				h.popleft()
				gender[1] += 1
				pre = "W"
				continue
			elif len(h) != 1 and h[1] == "W":
				del h[1]
				gender[1] += 1
				pre = "W"
			else:
				h.popleft()
				gender[0] += 1
				pre = "M"


if pre == "":
	print(sum(gender))
else:
	if pre == "M":
		gender[0]-=1
		print(sum(gender))
	else:
		gender[1] -= 1
		print(sum(gender))

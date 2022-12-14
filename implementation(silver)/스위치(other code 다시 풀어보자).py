# 스위치가 있는데

# 스위치는 1<= n <= 스위치의 개수
# 0 은 스위치가 꺼져 있는 거고 1 은 스위치가 켜져 있는 상태를 의미한다.
# 성별과 받은 수에 따라서 조작 방법이 달라지는데

# 기본 적으로 스위치를 "키고 켜는"

# 우선 남자 일경우 자기가 받은 수의 배수의 스위치 상태를 바꾼다
# ex) 3을 받았다면 3, 6, 9 <=n 까지의 배수 들의 스위치상태를 바꾼다.

# 여학생일 경우 자기가 받은 수를 중심으로 n-1, n, n+1 의 수가 대칭이라면
# n-2 와 n+2 의 상태가 같다면 n-2 부터 n+2 까지의 상태를 모두 바꾼다

# 만약 여학생이 4번을 받았는데 n-1, 과 n+1 의 상태가 서로 다르다면
# n 의 스위치 상태만 바꾼다.

# 스위치의 개수를 받아줍니다.
switch = int(input())
# 0은 off, 1은 on
state = list(map(int, input().split()))
n = int(input())
# 학생 남학생1, 여학생2 스위치 개수와 함께받습니다.
student = [list(map(int, input().split())) for _ in range(n)]



def man(state, num):
	arr = state
	# 남학생이고 num을 받아오면 그의 배수인 수들의 상태를 확인하는거지
	# num 이 만약3이면 3으로 나눴을때 0이 된다는 말이 되니
	# 즉 b를 3으로 나눴을때 0이된다면 b는 3의 배수이고 3은 b의 약수가 된다.
	# 기본적인 약수의 성질을 이용해주면 되는 문제.
	for i in range(len(arr)):
		if (i+1) % num == 0:
			# 만약 num의 배수이고 그 값이 off라면
			if arr[i] == 0:
				arr[i] = 1
			# 만약 num의 배수이고 그 값이 on이라면
			else:
				arr[i] = 0
	return arr

def girl(state, num):
	arr = state
	for i in range(len(arr)):
		# 내가 탐색할 스위치가 맞다면
		# 그 탐색할 스위치의 대칭값이 일치하는지 확인한후
		# 만약 일치한다면 pre-=1 nxt+=1
		# 만약 일치하지 않는다면
		# 그 전까지의 대칭값만 고친다
		if (i+1) == num:
			pre = i-1
			nxt = i+1
			# 키고 끄는건 기본이니
			arr[i] = int(not arr[i])
			while True:
				if pre >= 0 and nxt <= len(arr):
					if arr[pre] == arr[nxt]:
						arr[pre] = int(not arr[pre])
						arr[nxt] = int(not arr[nxt])
					else:
						break
				else:
					break
				pre-=1
				nxt+=1
	return arr


# 학생을 하나 씩 받아옵니다.
# 남녀 두명의 학생의 경우의 수가 있구요
# 이제 남학생인지 여학생인지 판단해서
# 각각에 맞는 로직을 돌릴겁니다.
for i in range(n):
	# 남학생
	if student[i][0] == 1:
		# 스위치의 상태, 스위치 번호
		man(state, student[i][1])
	# 여학생
	else:
		# 스위치의 상태, 스위치 번호
		girl(state, student[i][1])
for i in range(0, len(state), 20):
	print(*state[i:i+20], end="\n")

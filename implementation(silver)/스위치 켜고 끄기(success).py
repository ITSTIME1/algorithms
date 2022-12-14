# 문제분석

# 스위치는 켜져있거나 꺼져있는 상태로만 주어진다
# 1 = on
# 0 = off

# 성별과 받은 수에 따라서 스위치를 조작하는데
# 이때 수는 1 <= N <= 스위치개수 이하로 주어진다

# 남 : 스위치 번호가 자기가 받은 수의 배수이면
# 즉 주어진 번호의 배수의 값들이 1 -> 0 0-> 1

# 여 : 이게 인덱스로 따지는데 주어진 번호가 3이라면 3-1 = index 2  인 곳을 중심으로
# 대칭이면서 가장 많은 스위치를 포함하는 구간 모두 스위치 상태를 바꾼다
# 이때 구간에 속한 스위치의 개수는 항상 홀수개

# 만약 대칭이아니면 해당 번호-1 의 인덱스 스위치 상태만 바꾼다
# 스위치의 마지막 상태를 출력하는것
# 즉 주어진 조건에 맞게
# 마지막까지 해서
# 그 마지막 조건까지 업데이트 한뒤 배열의 상태를 출력하면 되는 문제인데


# 뭔가 남은 쉬운데
# 문제는 여자네...

s = int(input())

sw = list(map(int, input().split()))
n = int(input())

# man function
# 남자는 이렇게 하면 되는데
def man(num):
	for i in range(1, s+1):
		if num*i <= s:
			if sw[(num*i)-1] == 0:
				sw[(num*i)-1] = 1
			else:
				sw[(num*i)-1] = 0

# 여자 function
def girl(num):
	result = []
	index = num-1
	left, right = index-1, index+1
	if sw[index] == 0:
		sw[index] = 1
	else:
		sw[index] = 0

	# result.append(index)

	while True:
		# 범위를 벗어난다면 break
		if left < 0 or right >= s:
			break
		else:
			# 범위를 벗어나지 않고 둘이 대칭이라면
			if sw[left] == sw[right]:
				result.append(left)
				result.append(right)
				left-=1
				right+=1
				continue
			else:
				break
	for i in result:
		if sw[i] == 0:
			sw[i] = 1
		else:
			sw[i] = 0


		

# 1<= num <= s
# 남학생 1 여학생 2
for _ in range(n):
	gender, num = map(int, input().split())
	# 남, 여
	if gender == 1:
		man(num)
	else:
		girl(num)

# 오케이 이렇게 하면 되고
# 출력조건이

for i in range(0, len(sw), 20):
	print(*sw[i:i+20])


# 문제 분석

	# 오케이 무슨 문제인지 파악이 됨
	# 이건 그리디 문제임
	# 최대 무게를 만들 수 있을 무게를 합산하고
	# 만약 합쳤을때 최대무게가 넘어가는 시점이라면 박스를 하나 생성해야 됨

	# 하나를 빼왔을때 book <= M 같은 상황이라도 박스에 들어갈 수 있음
	# 즉 최대 무게 까지는 무게가 들어가진단 얘기
	# 만약 최대 무게가 M = 12 라고 한다면
	# 11 + 1, 10 + 2, 12 가 가능하다는 얘기 6+6 이나
	# 하지만 여기서 하나라도 더 들어온다면 >= M 최대 무게를 넘어가는게 되기 때문에
	# 안됨
	# 사실 여기서 예제 입력 3 에서 더 효율적인 방법을 찾아냈으나
	# 당장 현실적으로 더 좋은 방법을 찾는다면 4개가 맞으 
	# 그 이유는 7+1 조합이 박스를 3개 만들 수 있는 방법인데
	# 여기서 보면 1를 ㄴ찾느라고 다른 책을 가지고 오진 않음
	# 즉 위에서 말한것 처럼 차곡차곡 쌓아 올려져 있기 때문에
	# 하나르 뺸다면 무너지는 것 처럼 다른 쪽에서 가지고 오지 않는다고 생각하면 됨
	# 그렇게 된다면 가능함.

# 숌이 필요한 박스의 개수의 최솟값

# 박스의 최대 넣을 수 있는 무게가 존재한다
# 그리디 같은데 

# n = 책의 개수
# m = 박스에 넣을 수 있는 최대 무게
n, m = map(int, input().split())

ans = 0
# n == 0 이면 그냥 0을 출력.
if n == 0:
	print(ans)
	exit()
else:
	# 0 이 아니라면 책의 무게를 받고
	book = list(map(int, input().split()))
	ans = 1
	# book 을 담고 있는 book 리스트의 책이 다 없어지기 전까지 돌리고
	# box 를 카운트할 값을 정해둠
	total = m
	while len(book) != 0:
		first = book.pop()

		if first <= total:
			total -= first
		else:
			ans += 1
			total = m
			total -= first
	print(ans)
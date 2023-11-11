import sys
input = sys.stdin.readline


# 카드의 개수
N = int(input())

# i번째 카드는 p[i]에게 전달.
p = list(map(int, input().split()))
# i번째 카드를 s[i]번째로 이동.
s = list(map(int, input().split()))

# 초기 카드 위치.
card = [_ for _ in range(N)]

# 카드는 i번째에게 전달.
deliver_p = { card[i] : p[i] for i in range(N)}

# 총 이동횟수
total = 0

def deliver_check(s_list=card) -> bool:
	flag = True
	for i in range(N):
		# 카드의 위치랑, 실제 전달해야될 사람이랑 같은지를 비교
		index = i
		if index >= 3:
			index %= 3
		# 카드의 위치가 전달할 사람이랑 같다면 
		if index == deliver_p[s_list[i]]:
			continue
		else:
			flag = False
			break


	if flag: return True
	else: return False




if deliver_check():
	print(total)
else:
	modify_card = card
	# print(modify_card, s_list, sep="\n")
	while True:
		s_list = [0] * N
		for i in range(N):
			s_list[s[i]] = modify_card[i]

		# 변경된 카드 반영
		modify_card = s_list

		if deliver_check(s_list):
			print(total + 1)
			break
			
		total += 1

		if modify_card == card:
			print(-1)
			break

		

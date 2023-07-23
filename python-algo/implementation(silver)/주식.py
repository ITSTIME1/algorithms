# 그럼 가장 큰 날짜를 찾아서 그 인덱스까지 전부 빼서 차익을 더해주고
# 그 차익 index에 도달했다면 해당 리스트에서 다음 주가가 가장 큰 매도 금액을 찾아서 거기 까지 또 차이를 구한다.stdin

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
	# 날의 수
	n = int(input())
	sc = deque(list(map(int, input().split())))

	total = 0
	max = 0
	for j in range(n-1, -1, -1):
		if sc[j] > max:
			max = sc[j]
		else:
			total += max-sc[j]


	print(total)
	# 반대로 생각해야되는구ㅏㄴ
	# 말이된다.
	# 최대인 날이 아니면 어짜피 사게되니까
	# 왜냐하면 갈수록 감소하는 구간도 있기 때문이다.
	# 따라서 해당 하는 날이 최대가 아니면 살테니까
	# 
	# 반대로 해당하는 날이 최대라면 최대인날에 팔거니까
	# 이걸 반대로 생각해주면 풀린다. deque, del 다 시도했지만 deuqeh도 안될줄이야
	# 산다, 산다, 판다, 산다, 판다

	# 주식을 사는건 = 가격이 낮은날
	# 주식을 파는건 = 가격이 가장 높은날

	# 단순하게 가격이 낮은 날전까지는 주식을 계속 매입하고
	# 주식을 파는 날에 왔을때는 가장 큰금액에서 모두의 차를 합산한다.

	# 1. 가장 높은 날을 찾는게 우선
	# 2. 그럼 그 index까지 for문을 돌려서
	# 3. 가장 작은 값들을 리스트에 넣어주고
	# 4. 도달이 끝났다면 가장 큰 금액에서 차이를 계산한 후 total합산

	# 5. sc리스트에서는 값을 빼주는게 좋을거 같다.
	# 6. 만약 sc리스트에 날이 남아있다면 또 똑같이 계산하는게 좋을거 같음



	



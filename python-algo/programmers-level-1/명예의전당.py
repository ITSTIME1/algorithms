import sys
import heapq
from heapq import heappush, heappop
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# # 음 뭐지..
# # 문제는 이해가 된거같은데
# # 뭔가 이해는 된거 같은데...

# 처음에 k일까지는 들어온다고 했으니까

# k = 3
# score = [10, 100, 20, 150, 1, 100, 200]

# m = [10, 100, 20]

# # 가장 큰 점수가 가장 앞에 오도록 하는거지
# m = [100, 20, 10]
# # 150이 들어오면
# k = 3번째니까 k-1 번째 의 점수보다 크다면
# # ㄱ명예의 전당에 오르면되니까
# # appendleft로 들어오게된다면?
# # 하지만 유지해야되는 리스트의길이는 3이기 때문에
# # k만큼의 길이가 넘어가게된다면 마지막을 잘라
# m = [150, 100, 20, 10]
# m = [150, 100, 20]
# # 점수가 들어올떄마다 가장 최하위 점수를 하나리턴
# re = [10, 10, 10, 20, 20, 100, 100]

# # 1이 들어오게 되면
# # k번째보다 작으니까 내비두고
# # 최하위점수만 리턴
# m = [150, 100, 20]

# # 또 100이 들어오면 크니까
# m = [100, 150, 100, 20]
# # 정렬을해주고
# # 최하위점수 리턴
# m = [150, 100, 100]

# # 200들어오면
# m = [200, 150, 100]

# # 최하위점수 100 리턴
# 뭔가 heap을 써도 가능할거같은데
k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]

# 맞네 최소힙 이용문제
# k번쨰까지 먼저 가지고 오는게 좋을거 같아
heap = []
answer = []
for i in range(len(score)):
	# k일전까지는 쭉 넣어주고
	if i < k:
		heappush(heap, score[i])
		answer.append(heap[0])
	else:
		if score[i] > heap[0]:
			heappush(heap, score[i])
			# [10,20,100,150]
			if len(heap) > k:
				heappop(heap)
			answer.append(heap[0])
		else:
			answer.append(heap[0])


print(answer)

	# 음 뭔가 효율적으로 짜는 방법이 잇을거 같으넫
	# 어짜피 가장 큰 값은 앞쪽부터 유지해야되니
	# heapq를 사용해서 최대힙을 유지하면 도리거같고
	# 최대힙을 유지할떄마다 가장 작은 값은 answer에  저장하면되니까
	# 그러면 sort할 필요가없고deque니까 가장큰값은 또 가장앞에저장시켜두면되고

	# 이렇겧배ㅗ자 


# while len(m) < k:
# 	m.append(score[index])
# 	m.sort(reverse=True)
# 	answer.append(min(m))
# 	index += 1

# #[100, 20, 10]
# for i in range(k, len(score)):
# 	if m[k-1] < score[i]:
# 		m.append(score[i])

# 	m.sort(reverse=True)

# 	if len(m) > k:
# 		m.pop()
# 	else:
# 		answer.append(min(m))
# 		continue
# 	answer.append(min(m))
print(answer)

	


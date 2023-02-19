import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 각 테스트 케이스에는 최고점의 선수가 단 한명만
# 그럼 테스트케이스 1에서는 최고점의 선수가 99로 가장 최고점이된다.
# 그럼 각 주마다 2등인 사람들을 모으면 결과적으로 모든 사람들이
# 각주의 해당하는 2등인 셈
# 그럼 그 사람들 중에서 2등인 사람들을 찾으면

# 그럼 저게 선수번호인가
# 아 브릿지라는게
# 목록의 오르면 포인트가 + 1점씩 오르는 방식이기 떄문에
# 각 주마다 목록의 작성된 선수들의 이름을 hash 로 만들어두고
# 그 hash 가 나올때마다 해당 선수들의 이름을 +1 하면되겠네

pro = {}

while True:
	n, m = map(int, input().split())
	if n == 0 and m == 0:
		break

	prof = {}
	for i in range(n):
		# 각주마다 하나씩 받아오고
		a = list(map(int, input().split()))
		for j in a:
			if str(j) not in prof:
				prof[str(j)] = 1
			else:
				prof[str(j)] += 1

	prof_list = sorted(prof.items(), key = lambda x : -x[1])
	
	# 가장 큰 값은 제거한 뒤
	del prof_list[0]
	maxVal = prof_list[0][1]
	ans = []
	for i in prof_list:
		if i[1] == maxVal:
			ans.append(int(i[0]))

	ans.sort()
	print(*ans)
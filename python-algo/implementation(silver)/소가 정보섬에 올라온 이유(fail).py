import sys
import math
import heapq
import copy
from functools import reduce
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

# 문제분석


# 오케이 문제 분석 끝났어
# 그니까 결국은 Q번의 결처 i번재 소들의 스티커번호가 주어지는데
# 그 스티커 번호가 의미하는건
# 해당 소의 번호의 스티커를 ai*-1 곱해서 계산을 한다는 의미가 된다.item

# 그럼 소의 번호를 변경해야할 소의 번호를 하나씩 가지고와서
# 변경을 한 뒤에 곱셈을 해나가면 되는데
# 문제는 끝번호가 넘어가면

# 첫번째가 주어진 ai번호 끝까지 돌아왔다면
# 종료
# 그전까지는[0:4] 곱한값을 total에 더해주고
# 가장 앞의 있는 값을 빼주고 가장 뒤로 넣어준다음
# 다시 계산하고
# 그렇게 3을 가져왔을때의 값을 따로 리스트의 저장해주고
# 5를 변경했을때의 값을 리스트의 저장해주고
# 2,7 변경해주고 이때 한번더 7이나온건
# 한번더 변경을 해주어야하기 때문에 처음에 7인걸  -7로
# 그리고 또한번 변경한걸 -7->7로 변경한다.
# 그렇게 해서 리스트를 출력해주면 답이 될거 같네deque를 활용한 문제


# N 은 소의 수
# Q 는 장난칠 횟수
N, Q = map(int, input().split())
ai = deque(list(map(int, input().split())))
num = list(map(int, input().split()))


# 시간초과가 나는데
# 흠 TLE..
# dp 문제라고 한다 이게 그냥 구현으로는 시간의 한계가 있다.
# dp 문제를 풀어보고 풀어보자
def pi(arr):
	ret = 1
	for i in arr:
		ret *= i
	return ret

ans = []
for i in num:
	# 소의 번호를 바꿔주고
	ai[i-1] = ai[i-1] * -1
	cha = copy.deepcopy(ai)
	last_number = cha[-1]
	total = 0

	while cha[0] != last_number:
		arr = [cha[i] for i in range(0, 4)]
		total += pi(arr)
		a = cha.popleft()
		cha.append(a)
	
	arr = [cha[i] for i in range(0, 4)]
	total += pi(arr)
	ans.append(total)

for i in ans:
	print(i, end = "\n")


import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


# 반시계

# 10억번 돌리면 이 코드의 시간복잡도가
# r* min(n, m)//2 * 2
# 음 너무 킄ㄴ데?


# N*M-4
# 음 겉 배열을 4*4 일때
# 제자리로 돌아오는 순간이 존재하는데
# 12번이면 제자리로 돌아오자나 (원소 하나를 이동시켜서 자기 자리로 돌아오는걸 생각해본다면)
# 그럼 결국 이 12라는건 j 의 겉 배열 원소들의 개수자나

# 즉 j의 원소들의 개수만큼 반복된다는건 r이 기하급수적으로 커지면
# 반복되는 경우가 그만큼 나온다는 게 되고
# 12번에 한번씩 중복되는 처음으로 와지니까
# 그럼 r // N*M-4 한것 만큼 반복되게 되니까

# 그럼 회전수를 줄일라면
# 그 반복되는걸 줄이는데에서 시작할 수 있을거 같은데
# r번 돌릴때 동안 중복이 생기는걸 제외 하고 돌리는 횟수이면 되지않을까
# r번을 돌릴때까지 중복을 제외한다면 결국 그 줄인 횟수만큼 돌려도 r번 돌린게 나온다는거자나

# 원소의 개수만큼 돌리면 = 원점
# 그럼 이 원점을 이용해서 구지 r번을 다 돌리지 않아도
# 원점을 활용해서 더 적게 돌릴 순 없을까?

# 12 = 원점
# 그럼 12+1 = 13번 돌린거랑 같고
# 12+2 = 14번 돌린거랑 같고
# 12+3 = 15번 돌린거랑 같자나
# 12+4 = 16번 돌린거랑 같고
# 12+5 = 17번 돌린거랑 같고
# 12+6 = 18번 돌린거랑 같고
# 12+7 = 19번 돌린거랑 같고
# 12+8 = 20번 돌린거랑 같자나

# 그럼 결국 내가 r번 = 20번 돌린다고 한다면 8번만 돌리면 20번이랑 같게 된다는 뜻이되자나
# 그럼 결국 r번의 횟수를 % 원점의 주기로 나눈 횟수만큼만 돌린다면
# 8번만 돌려도 20번과 같은 모양이 나오니까
# 그럼 결국 20번 돌릴거 8번 돌리니 2/5나 줄여버리게 된거지
# 결국 5번중 2번의 연산만 하게 되는 꼴이 되니
# 5번 연산하는것보다 반이나 줄어들게 되니 이렇게 줄이면 거의 10^9승을
# 10억이라는 수를 5만번의 연산으로 줄여버리는거지
# 엄청난 효율이다


# 일단 이렇게 돌리는게 맞는건 맞아
# 4각형이니까 4개만큼 중복되는걸 빼준다면
# 원소의 개수가 나오는거지 = 이 만큼 돌렸을때 원점이 나온다는거니까
cycle = r % ((n*2) + (m*2) - 4)
depth = min(n, m) // 2


# 그럼 이걸 가지고 더 줄이는 방법 이존재할까
for _ in range(cycle):
	# 사각형을 선택하기 위한 for문인거지
	for j in range(depth):
		x=y=j
		tmp = arr[x][y]
		for k in range(j+1, n-j):
			pre = arr[k][y]
			arr[k][y], tmp = tmp, pre
			x = k
		for k in range(j+1, m-j):
			pre = arr[x][k]
			arr[x][k], tmp = tmp, pre
			y = k

		for k in range(j+1, n-j):
			pre = arr[n-k-1][y]
			arr[n-k-1][y], tmp = tmp, pre
			x = n-k-1

		for k in range(j+1, m-j):
			pre = arr[x][m-k-1]
			arr[x][m-k-1], tmp = tmp, pre
			y = m-k-1

# for row in arr:
# 	for item in row:
# 		print(item, end = " ")
# 	print()
print("\n".join([" ".join([str(item) for item in row]) for row in arr]))
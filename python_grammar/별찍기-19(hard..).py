# 한번 다시해보자
# 등차수열의 일반항 공식으로
# 첫줄과 마지막줄이 어떻게 별이 증가하는지 알 수 있는데

# 만큼 스타가 늘어난걸 알 수 있다. 
# 4*n-3

# 근데 이건 첫줄과 마지막줄만 이러는데

# 뭔가 어떤규칙으로 출력할 수 있는거지



# 1. 마지막 = 4*n-3 만큼의 스타 진행
# 2. 두번째, 마지막-1 = 4*n-1만큼 공백이 증가
# 3. 가운데는 2*n-1만큼 스타가 증가

# 그럼 이걸가지고 한다면

import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = int(input())

l = 4*n-3

# l == 2

star = [[" " for _ in range(4*n-3)] for _ in range(4*n-3)]


def dis(n, x, y, l):
	# 기저조건으로 인해서
	# 별의 중심점을 찍어주고
	# 각각의 둘러 싸주면 되는 형태일거 같은데
	if n == 1:
		star[x][y] = "*"
		return 0
	else:
		n -= 1
		dis(n, x+2, y+2, l-4)

		for i in range(l):
			for j in range(l):

				# 3 이면 x, y = 0, 0
				# 0 x = 8, j = 8
				# 2, 2, 2, 5
				if i+x == x or i+x == (l-1)+x:
					star[i+x][j+y] = "*"
				else:
					# 여기서 처리해야 되는게
					# 첫값과 끝값만 별로 찍어주면 되는거인데
					star[i+x][y] = "*"
					if j == l-1:
						star[i+x][j+y] = "*"


dis(n, 0, 0, l)


for i in star:
	print("".join(i))


# star = []
# for i in range(l):
# 	if i == 0 or i == l-1:
# 		a = "*" * (4*n-3)
# 		star.append(a)
# 	elif i == l // 2:
# 		a = "* " * (2*n-1)
# 		star.append(a)
# 	else:
# 		a = "*" + " "*(4*n-5) +"*"
# 		star.append(a)


# for i in star:
# 	print("".join(i), end = "\n")


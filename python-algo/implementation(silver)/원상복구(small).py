import sys
import heapq
from collections import deque, Counter
from itertools import permutations, product, combinations, combinations_with_replacement
input = sys.stdin.readline
sys.setrecursionlimit(10**6)



# 일단 예제를 어떻게 맞췄는데 이걸 어떻게 구현하지
# 구현이 어렵네
# 일단 알아낸건 k 의 횟수에 따라서
# di 순서를 배치하면 그게 원래 카드의 위치가 된다라는것
# 즉 k = 1 이라면 한번 배치했을때 나온 si 를 di 의 값만큼 배치한다면
# 그게 pi 값들이 되는거고


# k = 2 라면 di 와 k=2번돌렸을때의 si 값을 가지고 1번째 돌렸을때의
# pi 값을 찾고 하지만 이건 p2 일때의 카드 값이고
# k = 1 이기 때문에 si 를 한번더 di 만큼 배치한다면
# k = 2일때의 si 값을 얻을 수 있게 된다.


# 이건 어려운게 아니라 그냥 문해력이 문제야
# 아까는 거꾸로 햇어\

# 우선 d를 이용해서
n, k = map(int, input().split())

si = list(map(int, input().split()))
di = list(map(int, input().split()))


arr = [0] * n
while k > 0:
	for i in range(n):
		# 몇번째 위치에 i번째 카드값을 놓는다는 소리인데 반대로 해석했네 썅

		arr[di[i]-1] = si[i]
	# si 를 교체해주고
		print(arr)
	si = arr
	arr = [0] * n
	k-=1

print(*si)


# arr = []
# while k > 0:
# 	for i in range(n):
# 		arr.append(si[di[i]-1])
# 	si = arr
# 	k-=1

# print(*arr[5*k-5:5*n])
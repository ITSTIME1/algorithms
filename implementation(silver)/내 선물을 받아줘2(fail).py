import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 이건 문제 이해가 잘 안되었다
# 직사각형의 지도의 e, w의 대한 값이 어떻게 이동되는지의대한
# 시뮬레이션을 돌리면 가능할 거 같았고
# e라면 w를 만나기전까진 직진하기 때문에
# e를 만날때마다 선물을 놓아야하면 최소개수가 맞춰지지 않는다
# 출발위치는 제각각 다를 수 있기 때문에

# ew가 만나는지점의 무한루프가 발생하게 된다
# 이건 무한루프가 발생하는지점만 계속 방문한다는 얘기가 되고
# 계속 방문한다면 항상 거기에 선물을 둔다면 계속 받아먹는다는 애기가 된다.
# 그렇기 때문에 최소개수도 성립하면서
# 선물도 항상 가져가게 된다.

# 문제 이해의 발상이 어려웠다 해답을 보고 어떤 느낌인지 파악이 되었는데
# 문제 이해때문에 굉장히 어려웠던것 같다.


n = int(input())

arr = input()

cnt = 0
for i in range(len(arr)-1):
	if arr[i] == "E":
		if arr[i+1] == "W":
			cnt += 1
print(cnt)
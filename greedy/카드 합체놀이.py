import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 가장 작은 수를 만들려고 할때
# 가장 작은 수끼리 더해고 덮어 써야
# 가장 큰수와 더했을때 가장작은수를 더하게 되니
# 결과적으로 가장작게된다.

# 3 장의 카드와 1번의 합체

# 2 3 6
# x번 카드와 y번카드는 정렬된 뒤 가장 작은 데이터 두개

# 2+3 = 5(x!=y) 다르다는게 보이고
# 둘의 합을 덮어쓴다면
# 5, 5, 6 = 합산하면 10+6 = 16


# 4장의 카드와 2번의 합체


# 1
# 1 2 3 4
# 3 3 3 4

# 6 6 3 4 = 19 맞는거 같네
# 뭔가 디피 스럽긴한데

n, m = map(int, input().split())
arr = list(map(int, input().split()))


cnt = 0
while m != 0:
	arr.sort()
	arr[0] = arr[0] + arr[1]
	arr[1] = arr[0]
	m-=1

cnt = sum(arr)
print(cnt)


import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


b, c, d = map(int, input().split())

ham = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))

ham.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)

ans = [0, 0]
for i in range(min(b,c,d)):
	# 0.9를 곱해도 되는게
	# 0.9라는 수는 할인율을 제외한 나머지 가격만 더한것이기 때문임
	# 어짜피 같은 값이나옴
	ans[1] += int((ham[i] + side[i] + drink[i]) * 0.1)
	ans[0] += int((ham[i] + side[i] + drink[i]))

# sum하는 방법이랑 sort()를 큰 순서대로 나열하는게 키포인
ans[0] += sum(ham[min(b,c,d):])
ans[0] += sum(side[min(b,c,d):])
ans[0] += sum(drink[min(b,c,d):])

ans[1] = ans[0]-ans[1]
print(*ans, sep="\n")
# 문제분서 
import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())

poket = {}

for i in range(n):
	p = input().strip()
	poket[p] = i+1


# 아 이걸 아까 밖에 빼주지 않고 호출될때마다 이걸 해서 그렇구나 그러면 m * items()개수만큼 반복해야되니 엄청난 비용이었네 실수.

poket_list = {v:k for k,v in poket.items()}
for j in range(m):
	a = input().strip()
	if a.isdigit():
		ans = poket_list[int(a)]
		print(ans)
	else:
		ans = poket[a]
		print(ans)
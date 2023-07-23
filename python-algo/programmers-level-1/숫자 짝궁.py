import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

x = "5525"
y = "1255"

dic = {}

for i in range(0, 10):
	if str(i) in x and str(i) in y:
		# 숫자가 같으면 같은걸 반환할거고
		# 숫자가 다르면 마지막 예제처럼 5가 3개중 2개만 맞기 떄문에
		# 나머지 하나는 버려지니까 x, y값중 작은 값으로 한다면 하나는 버려지게되니 이런방법도 있네
		dic[str(i)] = min(x.count(str(i)), y.count(str(i)))


ans, isActive = "", True

if len(dic) == 0:
	ans = "-1"
	isActive = False

for k, v in dic.items():
	if k == '0' and v >= 2 and len(dic) == 1:
		ans = "0"
		continue
	else:
		ans += k*v

if isActive == True:
	ans_list = list(ans)
	ans_list.sort(reverse=True)	
	ans = "".join(ans_list)
print(ans)

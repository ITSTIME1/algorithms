import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline
limit_number = 15000
sys.setrecursionlimit(limit_number)

x = int(input().strip())


# 통과

t = 0
while len(x) != 1:
	t += 1
	x = [int(i) for i in str(sum(x))]


print(t)
ans = ""
if x[0] % 3 == 0:
	ans = "YES"
else:
	ans = "NO"
print(ans)


# 재귀 + while = 당연히 시간초과
t = 0
def function(divide):
	global t
	if len(str(divide)) == 1:
		return divide
	
	total = divide // 10**(len(str(divide))-1) + function(divide % 10**(len(str(divide))-1))
	return total


ans = x // 10**(len(str(x))-1) + function(x % 10**(len(str(x))-1))
answer = ""
if len(str(ans)) == 1:
	if ans % 3 == 0:
		answer = "YES"
	else:
		answer = "NO"
else:
	t += len(str(ans))
	if (ans // 10**(len(str(ans))-1) + ans % 10**(len(str(ans))-1)) % 3 == 0:
		
		answer = "YES"
	else:
		answer = "NO"

print(t)
print(answer)
if x % 3 == 0:
	print(cnt)
	print("YES")
else:
	print(cnt)
	print("NO")

# 합을 이용한 재귀도 가능하긴하겠네
# 자릿수의 합을 재귀로 넘겨서
# 그 인자로받은 재귀값의 길이를 체크한다음
# 그 길이가 1보다 작다면
# answer 를 출력하는 방식이면 되겠지
# 만약 1보다 크다면 결국 다시 합을 만들어준 다음 길이를 반환해주면 되니까



# 시간초과
t = 0
def function(x):
	global t
	if len(str(x)) > 1:
		number = sum(map(int, str(x)))
		if len(str(number)) == 1:
			t += 1
			ans = ""
			if number % 3 == 0:
				ans = "YES"
			else:
				ans = "NO"
			print(t)
			print(ans)
			exit()

		f = number // 10**(len(str(number))-1)
		s = number % 10**(len(str(number))-1)
		
		ans = []
		ans.append(str(f))
		ans.append(str(s))
		t += 1
		function(int("".join(ans)))

function(x)
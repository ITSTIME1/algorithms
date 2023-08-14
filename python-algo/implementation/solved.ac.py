import sys
import math
input = sys.stdin.readline

n = int(input())


# 파이썬에는 round()함수로 반올림하는 것이 존재하는데 파이썬에서 가지고 있는 반올림은 오사오입을 따른다.
# 앞자리가 홀수면 올려주고 짝수면 버려주는 식으로 따라서 2.5 앞이 짝수기 때문에 2가되고 3.5 앞이 홀수기 때문에 4가 된다.
# 반면 우리가 흔히 알고 있는 반올림 방법은 4사 오입을 따른다 4이하면 버리고 5이상일때만 올려주는
# 따라서 round() 함수를 따로 구현해야 되는 반올림 문제다.

def round2(num):
	# num = 3.75
	# int(3.75) = 3
	# 3 + (3.75-3) >= 0.5 보다 크거나 간다면 0.75 >= 0.5보다 크거나 같기 때문에 1을 통해서
	# 3 + 1 = 4로 만들어준다.
	# 그렇지 않을경우 2.0 - 2 = 0.0이기 때문에 0.5보다 작다 따라서 0을 리턴하여 int(num) + 0을 더하니 항상 정수가 된다.
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

# 의견이 없다면
# 0 False, 1True
answer = 0
if not n:
	print(answer)
# 의견이 하나 이상 있다면
else:

	dist = [int(input()) for _ in range(n)]
	
	INF = 0.15
	result = n * INF

	s = round2(result)
	dist_sr = sorted(dist)[s:-s]

	answer = round2(sum(dist_sr)/len(dist_sr))
	print(answer)

# round() 함수는 5사5입 = 앞자리가 홀수면 올리고 짝수면 버린다.n
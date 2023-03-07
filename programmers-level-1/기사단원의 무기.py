import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 15의 약수개수 = 1,3,5,15 총 4개
# 공격력이 4인 무기를 구매 약수의 개수에 해당하는 공격력을 가진 무기를 구매하니까

# ㅇㅋ

# number = 5
# 1~5까지의 약수의 개수를 각각구한다면
# 이렇게 되고

# limit = 3인건 약수의 개수가 3개를 넘지 않아야 한다는거
# power 를 지정했네 만약 3을 넘어가는 공격력을 가진 무기가 있다면
# power 로 지정한 공격력으로 바꿔야하네

# 1 2 2 3 2

# [1, 2, 2, 3, 2, 2, 2, 2, 3, 2]

# 6번 8번 10번은 limit 수치를넘기 떄문에
# 미리 지정해둔 power 를 구매한다
# 그럼
# 음 그러면
# 약수를구하는 함수를 통해서 해당 함수의 약수가몇개인지 구해보자
# 그리고 나서 어짜피 약수의 개수는 수당 1나 이상이니까
number = 10
limit = 3
power = 2

def l(nums):
    divisors = []
    for i in range(1, int(nums**0.5) + 1):
        if nums % i == 0:
            divisors.append(i)
            if i != int(nums/i):
                divisors.append(int(nums/i))
    return len(divisors)



weapon = []
for i in range(1, number+1):
	a = l(i)
	if a <= limit:
		weapon.append(a)
	else:
		weapon.append(power)
print(sum(weapon))


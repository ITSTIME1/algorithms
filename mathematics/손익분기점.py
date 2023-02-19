# 문제분석

# 매년 마다 고정비용 A 만큼이 들고
# 1대의 노트북을 생산하기 위해 B만큼의 비용이 필요.


# a = 1000 = 매년마다 고정비용 1000이 든다는 얘기고
# b = 70 이라고 한다면 노트북 한대를 생산하는데 70이 든다는 얘기다

# 그럼 고정비용 + 가변비용 = 1070 만원이 들게 된다. 이게 노트북 하나를 생산하는데 비용
# 그럼 이걸 10개 생산한다면 

# 고정비용 + (가변비용 * 10) = 1700만원
# 고정비용은 변하지 않는다 말 그대로 고정적인 비용이고 노트북의 가격만 대수의 따라 결정된다
# 문제에서도 읽어보면	 노트북 판매 대수와 상관 없다는 말이 있기 때문에
# 노트북 대수의 영향을 미치는 가격이 아니다 .


# 이때 노트북가격을 c라고 측정했을때

# 일반적으로 생산대수를 늘려가다 보면 총수입 = 고정비용 + 가변비용 보다 커지게 된다
# 총수입 > 고정비용 + 가변비용 이때 
# 최초로 총 수입이 총 비용보다 많아지는 때를 손익 분기점이라고 한다.


# a, b, c 가 주어졌을때 최초로 손익분기점이 나는 시기를 구해주세요.

# 그럼 총수입 total
# a = 고정비용 b 가변비용


# 1대의 노트북 값이 c만원이라고 한다
# 그럼 한대 생산할때마다 a+b*i
import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


a, b, c = map(int, input().split())

# 1000 70 170
# 아 손익 분기점 이라는게 총 고정 비용을 c-b로 나눈 것을의미하네
# a / (c-b)

# 판매대수의 따라서 총 매출액이 달라지니

# 판매량을 구하고 싶은거니까 판매량을 x로 둔다면

# 손익분기점은 = 매출액 = 총비용과 일치하는 시점을 말한다.
# 그래서 특별한 이익이나 손실이 없는 경우를 말하며
# 이 손익분기점 보다 높으면 이익이 발생되고
# 이 손익분기점 보다 낮으면 손실이 발생된다.
# c*x = a+b*x 
# c*x = a+(b*x)
# cx = a+bx	
# cx-bx = a
# x(c-b) = a
# x = a/c-b

# 그럼 손익분기점일 발생되지 않는시점은 언제일까
# 결국에 판매량이 높아지게 되면 총 매출이 증가하게 되는것

# 170 * 1 = 1000 + 70 * 1
# 170 * 2 = 1000 * 70 * 2

# 생산하는데 드는 비용보다 판매하는 비용이 작다면
# 즉 생산하는데 드는 비용 > 판매비용
# 이러면 이익이 날리가 없지
# 만약에 생산하는데 드는 비용이 10원이라고 치자 
# 그리고 판매하는 비용이 2원이야
# 그럼 1대 생산하는데 10원 주고 만들고
# 판매는 2원이라면 결과적으로 8원을 손실본건데
# 이 8원을 어디서 매꿔
# 결국 2대 생산하면 20원이고
# 2대 다 판매한다면 4원이라는건데
# 격차가 점점 벌어지게 되면서
# 손실만 나게 되는거지
# 매꿀 수 없어

# 최초 손익분기점이 되는 시점이니까
# 총 수입이 총 비용보다 많아져 즉 생산하는데 들어가는 비용보다 수입이 더 많아지는 때이기 때문에
# 이런경우는 수입이 올라가기 때문에 더 많이 만들어 낼 수 있지.
# 그렇다면 결과적으로 이익
# 그럼 손익분기점은 저 공식대로 하면되고
# 여기서 문제에서 말하는 손익분기점은 최초 이익이 발생된 판매량을 말하는거기 때문에
# 원래 손익분기점의 손실도 이익도 없는 지점을 말하는게 아니라
# 최초로 이익이 발생된 시점을 말하기 때문에 + 1 해줌으로써 판매량을 한대 늘리면 손익분기점을 넘어
# 11대를 판매하게 되면 최초로 손익분기점을 넘긴다는 얘기가된다.



def solve(a, b, c):
	break_point = int(a / (c-b)) + 1
	return break_point

if b > c:
	print(-1)
else:
	ans = solve(a, b, c)
	print(ans)

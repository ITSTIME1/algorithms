# # 문제분석

# # 기타줄 1개의 패키지는
# 1pac : 6개줄이라고한다.

# # 그리디 같은데도 그리디처럼 안되는데

# # 1. 패키지 가격과 낱개 가격의 최소가격을 찾는게 먼저임.

# 4 2
# 12 3

# 이렇게 생각해볼 수 있겠는데

# 낱개로 샀을때의 가격
# 패키지 두개를 샀을때의 가격

# 4개줄 필요하니까 4*3 = 12달러
# 패키지로산다면 12 달러


# 10 3

# 20 4

# 낱개로 살때 10*4 = 40
# 패키지로 살때

# 아 이게 패키지와 낱개가격이 항상 패키지가 크지 않아
# 그걸 염두해두어야하네

# 결국엔 줄의개수 의따라서 분류하는게 아니라
# 패키지든 낱개든 돈이 덜 드는 쪽을 선택하게끔 만들면 될거같은데
# 가령 예를들면
# 10 
# 20 4

# 10-6 = 4
# 4-6 = -2 < 0
# pac : 20 + 20 = 40
# single : 10*4 = 40
# pac+single = 20 + 4*4= 36

# 결과적으로 크게 세가지 정도의 경우가 있을 수 있겠네
# 패키지로 다 사버리는거
# 낱개로 다 사드리는거
# pac+single 섞어서 사는거

# 그럼 저 세가지 경우의 수 들중에서 가장 적은 값을 리턴하면 되는거자나

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pac, single = [], []

for i in range(m):
	p, s = map(int, input().split())
	pac.append(p)
	single.append(s)

# 가장 작은 값을 분류해주고
p, s = min(pac), min(single)

def pac(num, p, s):
	cnt = 0
	while num > 0:
		cnt += p
		num-=6
	return cnt


def single(num, p, s):
	cnt = 0
	cnt += s*n
	return cnt

def pacSingle(num, p, s):
	pac = p
	single = s
	cnt = 0
	while num > 0:
		if num >= 6:
			cnt += p
			num -= 6
			continue
		else:
			pac_price = cnt + p
			single_price = cnt + (s*num)

			tmp = min(pac_price, single_price)

			if tmp == pac_price:
				cnt += p
			else:
				cnt += s*num

			num-=num

	return cnt



pacValue = pac(n, p, s)
singleValue = single(n, p, s)
pac_single = pacSingle(n, p, s)

print(min(pacValue, singleValue, pac_single))

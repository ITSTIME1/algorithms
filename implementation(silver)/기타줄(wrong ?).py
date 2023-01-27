# 문제분석

# 4 2
# 12 3
# 15 4

# 1pac = 6

# 그럼 어짜피 돈을 지불해도 가장 가격에서 살것이니
# 1. 패키지중 가장 작은 가격, 낱개 중 가장 작은 가격을 선별

# 12 3
# 12-6 = 4
# 20 4
# 20 + 16 = 36

# 15 1
# 100 40

# 15-6 = 9
# 9-6 = 3
# 3-6=-3 < 0
# 패키지 : 100 + 100 + 120 = 320
# 낱개 : 100 + 100 + 100 = 300

# 7 2
# 10 2

# 7-6 = 1
# 10+2 = 12

# 마지막 예제는
# 9
# 3, 8
# 9-6=3
# 3+3=6
# 그럼 어짜피 돈을 지불해도 가장 가격에서 살것이니
# 1. 패키지중 가장 작은 가격, 낱개 중 가장 작은 가격을 선별


# 2. 부러진줄의 수가 >= 패키지 줄의 수보다 크다면 : 패키지 구입
# 	패키지를 구입하고 줄을 줄인다.

# 	부러진 줄의 수가 < 패키지 줄의 수보다 작다면 
# 		중요한건 이부분이다
# 		위 예제처럼 부러진 줄의수가 6줄 보다 작다면 무조건 낱개를 사게 되면 140원 이되버린다
# 		반면에 패키지 하나를 사게 된다면 100 이 되므로 더 적다

# 	만약 패키지를 산 가격 과 낱개로 산가격을 구해서
# 	더 적은 가격을 리턴하고 줄의수를 줄인다.


import sys
input = sys.stdin.readline
# O(N*M)

n, m = map(int, input().split())

pac_list, single_list = [], []
p, s = 0, 0
for _ in range(m):
	pac, single = map(int, input().split())
	pac_list.append(pac)
	single_list.append(single)

# 가장 작은 값들을 골라놓고
p = min(pac_list)
s = min(single_list)

# 10 3
# 20 8
# 40 7
# 60 4

cnt = 0
while n > 0:
	if n >= 6:
		if n*s == n:
			cnt = n*s
			break
		cnt += p
		n-=6
		continue
	else:
		single_price = (s*n)+cnt
		package_price = cnt + p
		tmp = min(single_price, package_price)

		if tmp == single_price:
			cnt += s*n
		else:
			cnt += p
		n-=n
print(cnt)




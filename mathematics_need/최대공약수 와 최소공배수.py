# 최대공약수란 = 공약수 중에서 가장 큰 수를 최대공약수 라고 한다
# 공약수란 = 수의 약수들을 나열해봤을 때 공통되는 약수가 존재한다면 그 수는 공약수라고 한다.

# 큰 수의 최대공약수를 구하려면 두 수든 세수든 한 수의 약수의 개수를 구해주어야 하는데
# 숫자가 기하급수적으로 커질 수록 이 방법은 굉장히 많은 시간이 필요하다
# 때문에 이런 숫자가 기하급수적으로 커져 시간이 너무 오래 걸려 고안된 방법이 유클리드 호제법을 이용해서
# 최대공약수를 구한다.

# 최소공배수란 = 공배수 중에서 가장 최소(가장작은) 수를 최소 공배수 라고한다.
# 공배수란 = 두 수의 배수들 중에서 공통된 배수들을 공배수 라고한다.
# 그럼 최소 공배수는 결국 공배수들 중 가장 작은 수를 공배수 라고 한다.

# 최대공약수 와 최소공배수 의 차이가 무엇이냐
# 최대 공약수는 두 수 혹은 두 수 이상의 수들의 약수를 구해서 그 수들의 약수들 중 공통된 수들인 공약수를 구해
# 그 공약수중 가장 큰 값을 구하면 된다 즉 (약수) 이냐 (배수)냐 차이다.

# 최소 공배수는 두 수 혹은 두 수 이상의 수들의 배수들을 구해서 그 수들의 배수들 중 공통된 배수인 공배수를 구해
# 그 공배수 중 가장 작은 값을 구하게 되면 그게 바로 최소 공배수 인것이다.



# GCD 를 구하는 방법 (Greatest Common Divisor)
# 최대 공약 수를 짧게 설명해보자면 두 수 혹은 그 이상의 수의 약수들 중에서 공통된 약수를 공약수라고하고
# 그 공약수 중에서 가장 큰 수를 최대공약수 GCD 라고 한다.

# a, b 둘다 나누어 떨어지게 하는 수가 바로 공약수이다.
# 2, 4 라고 한다면 최소 값은 2이기 때문에 i = 2 부터 
# 그리고 1 한다면 최대 공약수는 결국 두개의 수를 동시에 나눠서 나머지를 0을 만드는 수가 바로
# 최대공약수 일 것이다.
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def gcd1(a, b):
	if a < b:
		min = a
	else:
		min = b
	res = 0
	# min+1 이나 min 이나 최대 공약수는 가장 큰 수 부터 -1씩 감소 시키면서
	# 가기 때문에 상관없다
	for i in range(min+1, 1, -1):
		if a % i == 0 and b % i == 0:
			res = i
			break
	return res


# LCM (Least Common Multiple)
def lcm(a, b):
	for i in range(max(A,B), (A*B) + 1):
		# 이 코드는 약수의 성질중
		# b가 a의 배수이면 a는 b의 약수이다
		# 12가 4의 배수이면 4는 12의 약수이다.
		if i % A == 0 and i % B == 0:
			print(i)
			break


def lcm1(a, b):
	if a > b:
		max = a
	else:
		max = b
	for i in range(max, a*b+1):
		if i % a == 0 and i % b == 0:
			print(i)
			break

# 유클리드 호제법으로 최대공약수와 최소공배수 구하기.
# 방법1 # 재귀적으로 호출해서 n 이 0이 되면 예를들어 6, 0 이 들어온다면
# 최대공약수는 6이된다.
def gcd(m,n): # gcd == "Greatest Common Divisor"
	if m < n:
		m, n = n, m
	if n == 0:
		return m
    if m % n == 0:
		return n
	else:
		return gcd(n, m%n)

# 방법2
def gcd(m,n):
    while n != 0:
       t = m%n
       (m,n) = (n,t)
    return abs(m)


# 유클리드 호제법
def gcd2(a, b):
	if a < b:
		a, b = b, a 
	while b != 0:
  		a=a%b
  		a,b=b,a

  	return a

# 유클리드 호제법
def gcd3(a, b):
    while b > 0:
        a, b = b, a % b
    return a
# 최소공배수의 성질 중 두 수의 곱을 / 두 수의 최대공약수로 나눈 값이 바로 최소공배수가 된다.
def lcm(a, b):
    return a * b / gcd(a, b)

# 소인수 분해
# 소인수 분해 = 어떠한 자연수를 나눴을때 몫이 소수가 나올때 까지 소인수 들로만 나누는 분해 방법을 소인수 분해라고 합니다.
# 소인수란 = 인수들 중 소수인 수를 소인수라고 합니다.
# 인수란 = 어떠한 자연수를 곱으로만으로 나타냈을때 나오는 수를 인수라고 합니다.
# 소수란 = 1과 자기 자신만을 약수로 가지는 수를 소수라고 합니다.


# 소인수 분해에서 나누는 수가 소수가 아니어도 된다.
def factorization(x):
    d = 2
    while d <= x:
        if x % d == 0:
            x = x / d
        else:
            d = d + 1

factorization(60)

# 이 함수는 소인수분해 함수인데 d<=x 보다 작을때 까지만
# 반복한다 이 뜻은 나누는수가 커지는 순간이 있을때가 마지막 소인수 분해 이기 때문이다
def fa(x):
	d = 2:
	while d <= x:
		if x % d == 0:
			x //= d
		else:
			d += 1
	

# Q. 만약 n까지 소수를 찾아서 소수를 따로 나누고 그 소수들로 소인수 분해를 진행했을 때
# 해당 n의 소인수들을 구하는 문제.

  # 소수 판별
  def isPrime(num):
      for i in range(2, math.floor(math.sqrt(num))+1):
          if num % i == 0:
              return False
      return True

  # 소수 찾기
  def findPrimes(n):
      primes = []
      for i in range(2, n+1):  # for i in range(2, (n//2)+1) 로 개선 가능
          if isPrime(i):
              primes.append(i)
      return primes

  print('소수 리스트', findPrimes(30))

  # 소인수 분해 1
  def factorize(n):
      factors = []
      primes = findPrimes(n)  # n의 소수 리스트를 추출
      for i in primes:
          while (n % i == 0):  # 소수 중 나누어 떨어지는(약수) 수를 찾는다
              factors.append(i)
              n = n // i
      return factors

  print('소인수분해 결과', factorize(30))
  
# 약수란 = 어떠한 자연수 N을 N까지의 수로 나누었을 때 나누어 떨어지게 만드는 수를 약수라고 한다
# 소수란 = 1과 자기 자신만이 나누어떨어지게 하는 수이며 약수의 개수가 두개인 수 (1, N)인 수를 소수라고 한다.
# 다른말로 = 1과 자기 자신 이외에 나누어 떨어지는 수가 생긴다면 그 수는 소수가 아니다.

# 1은 소수? = 1은 소수가 아니다 즉 소수를 판별할때 1보다 큰 자연수부터 시작해야 된다.

# 기본 약수 판별 알고리즘
# 1부터 N까지 수 중에서 n을 나누었을 때 나누어 떨어지게 하는 수들은 전부 약수이다.
def check_divisor(nums):
	divisors = []
	for i in range(1, nums+1):
    	if nums % i == 0:
    		# cnt 를 체킹하던지 아님 리스트에 약수를 추가하여
    		# 약수의 개수를 반환하던지
        	divisors.append(i)
    return divisors

# 기본 소수 판별 알고리즘
# 1 보다 큰 자연수 중에 1은 소수가 아니기 때문에
# 2부터 시작하여 num 전까지 수 중에서 나누어 떨어지는 수가 있다면 그 수는 더 이상 소수가 아니다.
def check_prime_number(nums):
	for i in range(2, nums):
    # 2 이상의 자연수인 nums에 대해 반복문을 돌며 nums-1까지 일일히 확인해
    	if i % nums == 0:
        	return False
        # i가 nums와 나누어 떨어지면 nums는 소수가 아님
    return True


# 약수의 성질을 이용한 알고리즘 최적화
# 해당 수의 제곱근 까지만 구한다면 그 수의 약수의 개수를 전부 구할 수 있다.
def check_divisor(nums):
    divisors = []
    for i in range(1, int(nums**0.5) + 1):
        if nums % i == 0:
            divisors.append(i)
            if i != int(nums/i):
                divisors.append(int(nums/i))
    return sorted(divisors)


# 제곱근을 이용해서 구하는 방법.
# for i in range(1, int(nums**0.5)+1):
# 	if nums % i == 0:
# 		divisors.append(i)
# 		# 모든 약수를 구하기 위해서 제곱근의 수가 아니라면 
# 		# i 와 nums/i 값을 다르기 때문에
# 		# nums/i한 값또한 약수이기에 넣어준다.
# 		# 제곱근에 도달해서 같다면 이미 4는 같은 값이 하나 들어가져 있기 때문에
# 		# 포함시키지 않는것이다.
# 		if i != int(nums/i):
# 			divisors.append(int(nums/i))



# 약수의 성질을 이용한 소수 판별
# 이것또한 약수의 성질중 제곱근 까지 구하게 되면 
# 소수의 판별을 알 수 있다.
# 제곱근 판별은 제곱근까지 확인을 해야 한다.
# 왜냐하면 16이 소수인지 알기 위해선 약수의 개수가 두개 인지 1과 자기 자신이외에 떨어지는 수가 있는지
# 확인을 할때 소수 판별을 사용하는데 16의 약수들은 1대1 대칭 되기 때문에 
# 1*16, 2*8, 4*4, 8*2, 16*1
# 즉 16의 제곱근인 4까지만 확인한다면 그 다음은 서로 대칭되는 값이기 때문에
# 구할 필요가 없어진다.


# 시간복잡도 O(N^1/2)num
def check_prime(num):
    if num == 1: return False # 1은 소수가 아니므로 제외
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 에라토스테네스의 체
def prime_number(num):
    # 0부터 num 범위의 자연수의 소수 판별 여부를 위한 리스트. 
    # 0과 1은 소수가 아니므로 False로 선언
    check_prime = [False, False] + [True] * (num - 1)

    # 앞서 설명한 약수의 원리를 응용해 소수 판별 범위 축소
    for i in range(2, int(num**0.5)+1):
        if check_prime[i]:
            for j in range(i+i, num+1, i):
                check_prime[j] = False

    return [i for i in range(2, num+1) if check_prime[i]]
    
print(prime_numbers(131))


n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)



array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘 
# 시간복잡도는 O(NloglogN)
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i] == True: # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2 
        while i * j <= n:
            array[i * j] = False
            j += 1

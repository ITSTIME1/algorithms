import sys

dp = [_ for _ in range(1, 246913)]

def sieve_of_eratosthenes(n):
	if n == 1:
		return False
	# 루트 10 정도가 3.16..
	else:
		for _ in range(2, int(n**0.5)+1):
			if n % _ == 0:
				return False
		return True

# 소수 인것만 따로 모아놓고
new_dp = [_ for _ in dp if sieve_of_eratosthenes(_)]

while N:=int(sys.stdin.readline().strip()):
	if N == 0:
		break
	# cnt = 0
	print(len([_ for _ in new_dp if N < _ < (2*N)+1]))
	# for _ in new_dp:
	# 	if N < _ < (2*N)+1:
	# 		cnt+=1

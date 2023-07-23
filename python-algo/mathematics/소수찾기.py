# 소수 = 1과 자기 자신만이 나눠지는 수
# 이걸 구하려면 약수의 개수를 구하고 약수의 개수가 2개라면
# 소수임
# 1은 소수가 아님
N = int(input())

arr = list(map(int, input().split()))

sosu = 0
for num in arr:
	error = 0
	if num > 1:
		for i in range(2, num):
			# 5 2 3 4
			if num % i == 0:
				error += 1
		if error == 0:
			sosu+=1
print(sosu)
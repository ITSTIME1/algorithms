import sys
input = sys.stdin.readline


t = int(input())

for i in range(t):
	n, m = map(int, input().split())
	# 수 자릿수를 어떻게 맞춰야 하지.
	x = "".join(input().strip().split())
	y = "".join(input().strip().split())
	answer = 0
	number = list(map(str, input().strip().split()))

	# new_number = number + number[:m-1]

	# for i in range(len(number)):
	# 	if int(x) <= int("".join(new_number[i:i+m])) <= int(y): answer += 1
	for j in range(len(number)):
		if j + m > len(number):
			first = "".join(number[j:j+m])
			# 4+3 = 7
			check = ((j+m) - len(number)) % m
			second = "".join(number[:check])
			if int(x)<= int(first + second) <= int(y):
				answer += 1
		else:
			if int(x) <= int("".join(number[j:j+m])) <= int(y):
				answer += 1
	print(answer)

	



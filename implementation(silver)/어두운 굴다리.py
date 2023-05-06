
# 전체 길이가 짝수일경우

# 짝수길이라 최대가 홀수가 된다면 +1을 더해주어야 전부 밝혀준다.

# 홀수길이에서 최대가 홀수가 된다면 그대로 높이를 잡으면 전부 밝혀지고

# 전체 길이가 짝수일경우에
# 1. 홀수가 최대일경우 +1
# 2. 짝수가 최대일경우 


# 결국 전체길이가 홀수일 경우는 짝수가 나오든 홀수가 나오든
# 그냥 쓰더라도 전부를 밝힐 수 있음

# 전체 길이가 홀수일경우
# 1. 홀수가 최대일 경우 사용
# 2. 짝수가 잡힐경우 그대로 사용

# 그럼 전체 길이가 짝수일 경우에는 홀수가 최대일 경우 + 1를 더해주어야 하는거네

# 이건 좀 어렵네
# 생각을 깊게 해야 되는문제네
n = int(input())
m = int(input())


arr = list(map(int, input().split()))

# 오름 차순으로 받는거니까
# 나중에 다시 풀어봐야 겠네

minHeight = arr[0]


for i in range(len(arr)):
	# 마지막 가로등
	if i == len(arr)-1:
		minHeight = max(minHeight, n-arr[i])
	# 첫 가로등과 마지막 가로등 사이
	else:
		t = (arr[i+1] - arr[i])
		if t % 2 == 0:
			minHeight = max(minHeight, t // 2)
		else:
			minHeight = max(minHeight, (t // 2) + 1)

print(minHeight)

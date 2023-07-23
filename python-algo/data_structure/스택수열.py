# ubuntu test


# mac test 해볼게요 0
import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

ans, stack = [], []
index, x = 1, 0

for i in range(n):
	# 첫 수보다 작은 숫자들까지 채워주고
	while index <= arr[i]:
		stack.append(index)
		ans.append("+")
		index+=1
	# [1,2,5]
	# [3,4]
	# 6 3
	# index 는 증가 되었기 때문에
	# 더이상 while 문을 돌지않고
	# 밑으로 내려와서
	# 스택의 끝 값이 현재 뽑고자 하는 값이 맞는지 
	# 확인하고
	# 만약 뽑고자 하는 값이 아니라면
	# 순서가 맞지 않으므로
	# 스택의 순열을 맞출 수 없다
	if stack[-1] == arr[i]:
		ans.append("-")
		stack.pop()
	else:
		print("NO")
		x = 1
		break
if x == 0:
	for i in ans:
		print(i, sep="\n")
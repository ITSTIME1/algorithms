# 문제분석
# 1부터 n까지 스택에 넣었다가 뽑는다

# 스택에 push 하는 순서는 반드시 오름차순을 지킨다.
# 쯕 스택에 들어가는 순서는 반드시 1,2,3,4 이런식으로 쌓여가야 된다는 것이다
# 임의의 수열이 주어졌을때 어떤 순서로 push와 pop연산을 수행해야 하는지 알아낼 수 있느
# 프로글매을 작성해라


# 이런 배열을 만들기 위해서
[4, 3, 6, 8, 7, 5, 2, 1]
# 논리 적으로 설명을 해보자
# 일단 처음에 4가 오려면 스택에 일단 쌓아야 하는 숫자가 있어야 하니까
# 4보다 작은 숫자들을 쌓고 난 다음에 4를 뽑으면 4가 가장 맨 처음에 잇을 수 있찌

# 즉 4보자 작은 숫자들을 먼저 stack 에 push + + + + 
# [1,2,3,4]
# 입력이 끝났으면 마지막 숫자를 뽑아서 새로운 리스트에 넣어주고 
# [4,]
# [3,6,8,7,5,2,1]
# 그런 다음 원래 리스트에서 4를 제거
# 그다음에 3을 뽑기 위해서 저 위에 리스트에 3이 있다면 뽑고
# [4,3]
# [1,2]
# 이제 스택에 6이 끝수가 아니라면 6이 나올때까지 push 해준다
# [1,2,5]
# 그럼 이제 6을 가져올 수 있으므로 pop
# [4,3,6,7,8]
# 그다음 숫자는 8이므로 8이 나올때까지 push한다
# 8이 나왔으므로
# [4,3,6,8], [1,2,5,7]
# 그다음 수는 7이므로
# [4,3,6,8,7]
# 그다음 수는 5

# 1. 처음 숫자보다 작거나 같은 숫자들을 먼저 스택에 넣어준다
# 2. 위 과정이 끝난뒤 우리가 찾을 4 즉 arr[0] == stack[-1] 과 동일하다면
# 3. 뽑아서 새로운 리스트에 넣어준다 [4] 그리고 arr 인덱스를 하나 올린다
# 4. 그럼 arr[i] == stack[-1] 과 같다면 또 뽑아주고
# 5. [4,3]
# 6. 만약 없다면 처음 숫자 이후의 숫자들을 i가 나올때 까지 넣어준다
# 7. i가 나왔다면 arr[i] == stack[-1] 이라면 뽑아준다
# 8. 위의 과정들을 리스트에 하나씩 +, -로 남겨준다면
# 9. 마지막에 순서대로 출력만 해주면 된다

import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

first = 0
stack, ans, result = [], [], []
for i in range(len(arr)):
	# 스택에 현재 수가 없다면
	if arr[i] not in stack:
		for j in range(first+1, arr[i]+1):
			if j not in stack:
				ans.append("+")
				stack.append(j)

		first = stack[-1]
		# 숫자보다 작거나 같은 숫자들ㅇ르 넣어주고
		if stack[-1] == first:
			result.append(stack.pop())
			ans.append("-")
	else:
		result.append(stack.pop())
		ans.append("-")
cnt = 0
for i in range(len(arr)):
	if result[i] != arr[i]:
		cnt += 1

if cnt >= 1:
	print("NO")
else:
	for i in ans:
		print(i, sep="\n")


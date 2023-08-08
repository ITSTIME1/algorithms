
import sys
from collections import deque
input = sys.stdin.readline



# 36% 실패
string = list(input().strip())

total = 0

o, c = 0, 0
flag, end = False, False
stand = ""
check = deque([])
total = 0

for i in range(len(string)):

	# 아직 검사를 시작 안했고 이제 검사를 시작하는 거라면
	if flag == False:
		if string[i] == "(":
			if not check:
				total = 0
			stand = "("
		elif string[i] == "[":
			if not check:
				total = 0
			stand = "["
		o += 1
		flag = True

	else:
		if stand == "(" and string[i] == "(" or stand == "[" and string[i] == "[":
			o += 1
			check.append(string[i])
		elif stand == "(" and string[i] == ")" or stand == "[" and string[i] == "]": 
			c += 1
			if o != c:
				check.append(string[i])
			else:
				if len(check) == 0:
					if stand == "(" and string[i] == ")":
						total += 2
					elif stand == "[" and string[i] == "]":
						total += 3
					o, c = 0, 0
					flag = False
					stand = ""
					continue

		elif stand == "(" and string[i] == "[" or stand == "[" and string[i] == "(":
			check.append(string[i])
		elif stand == "(" and string[i] == "]" or stand == "[" and string[i] == ")":
			check.append(string[i])

		# 열린 괄호의 개수와 닫힌 괄호의 개수가 같아졌다면
		# 이제 해당 부분들을 검사할건데
		# check에 저장해두었던 문자들을 하나씩 검사해날거고

		# ()(
		# [(])
		# 그 검사하면서 (), [] 문자들을 만나면 저장해둘거임
		if o == c:
			# 바로 오는 경우는 어떡할까
			flag = False
			open = 0
			close = 0
			# 음 저장해둔게 (((((())))))
			# 이런 경우라면((((()))))
			# 여기까지가 검사지점이 될텐데 그럼 안쪽부터 검사를 해나가야 하는거 같은데
			stack = []
			while check:
				s = check.popleft()
				if not stack:
					stack.append(s)

				if stack[-1] == "(" and s == ")":
					stack.pop()
					open += 1

				elif stack[-1] == "[" and s == "]":
					stack.pop()
					close += 1
				elif stack[-1] == "(" and s == "]":
					end = True
					break
				elif stack[-1] == "[" and s == ")":
					end = True
					break
				else:
					stack.append(s)

			# 이건 어떻게도 만들 수 없었다는 뜻이 되니까
			if open == 0 and close == 0:
				end = True
				stand = ""
				break

			if open == 0 or close == 0:
				if open == 0:
					if stand == "(":
						total += (2*(3**close))
					elif stand == "[":
						total += (3*(3**close))
				else:
					if stand == "(":
						total += (2*(2**open))
					elif stand == "[":
						total += (3*(2**open))
			else:
				if stand == "(":
					total += (2*(2**open + 3**close))
				elif stand == "[":
					total += (3*(2**open + 3**close))
			

			o, c = 0, 0
			check = deque([])
			stand = ""
# 마지막 처리를 해줘야 하는데
# ()(
# 앞쪽은 처리가 되는데 마지막은 처리가 안되자나

if end == True or check:
	print(0)
else:
	print(total)












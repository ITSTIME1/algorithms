
# import sys
# input = sys.stdin.readline

# # 문자열
# string = input().strip()
# # 폭발문자열
# boomb = input().strip()


# s = ""
# pre = 0
# i = 0
# while True:
# 	if string[i:i+len(boomb)] == boomb:
# 		pre = (i+len(boomb))-1
# 	else:
# 		if i == 0:
# 			s += string[i]
			
# 		if i > pre:
# 			s += string[i]

# 	if i == len(string)-1:
# 		if string == s:
# 			break
# 		else:
# 			if s == "":
# 				# 12ab, []
# 				string = ""
# 				break
# 			else:
# 				string = s
# 				s = ""
# 				i = 0
# 				pre = 0
# 				continue
# 	i += 1
# if string == "":
# 	print('FRULA')
# else:
# 	print(string)


# s = [1,2,3,4]
# 이 표현 자체가 뒤에서 3번째 까지라는 말이 되네
# 음 그러면 풀릴 수 있구나 뒤에서부터 탐색을 해가면서 풀어진다는게 신기하네.
import sys
input = sys.stdin.readline

string = input().strip()
boomb = input().strip()


stack = []
# 시간복잡도가 O(N)만큼에서 끝나게 되고
# 폭발문자열의 길이가 될때마다 계속 검사를 할거니가 뒤에서부터
# 결국 추가할때마다 추가된 지점에서부터 뒤로 계속 검사해 나간다면 폭발 문자열들을 전부 찾을 수 있게 된다.
for i in string:
	stack.append(i)
	if len(stack) >= len(boomb):
		if "".join(stack[-len(boomb):]) == boomb:
			del stack[-len(boomb):]	

print(stack)





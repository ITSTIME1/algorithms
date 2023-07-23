# 문제분석
# 계속 틀렸다고 나오니 답을 보니까
# 정규표현식 이라고 한다.
# 정규표현식은 한번도 공부해본 적은 없는데

# 그럼 정규표현식을 사용하지 않고는 어떻게 풀었어야 했을까

# 생각해보면 간단한 문제같은데
# 우선 패턴의 규칙은 알파벳과 중간 별 그리고 알파벳이다
# 중간에 별이 있다는건 별표를 기준으로 양옆의 알파벳의 개수가 똑같아야 한다는건 아니다
# 우선 그렇다면 왼쪽과 오른쪽을 나눠서 저장한뒤

# aa*dddd
# aasdfd
# left = [a,a] 2
# right = [d,d,d,d] 1
# 오른쪽은 어떻게 검사할까..
# s[len(s[left:len(s)-1])]
# 아 이렇게 맞출 수도 있겠네
# 아 그러면 문제가 좀 쉬워지겠다


# a*dddd
# [a] 1
# [d d d d] 4

# 입력받은 문자열이 주어진 패턴보다 길이가 길어지는 때가 있네
# a dd

n = int(input())
pattern = list(map(str, input().split("*")))
# [a, b]
# [a], [d]
left = pattern[0]
right = pattern[1]

for i in range(n):
	string = input()
	# 빈문자열이어도 같아지게끔 한다는건가.
	if string[:len(left)] == left and string[-len(right):] == right and len("".join(pattern)) <= len(string):
		print("DA")
	else:
		print("NE")



# AB*BD

# [A,B] 2 
# [B,D] 2
# # 겹쳐서 나오는구나
# ABD
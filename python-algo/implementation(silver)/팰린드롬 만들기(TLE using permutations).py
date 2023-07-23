# 팰린드롬 = 회문
# 거꾸로 읽어도 우영우
# 똑바로 읽어도 우영우
# 기러기 스위스 토마토 인도인 별똥별 우영우 윤영윤


# 알파벳 순서를 바꿔서 회문을 만들어라

# AABB
# ABBA
# ABABA

# 처음에 회문인지 아닌지 판별을 해준다ㅡㅇ멩
# 만약 회문이 아니라면
# 처음 문자열을 지워보고 회문인지 아닌지판단하고
# 또 회문이 아니라면
# 그다음 첫 번쨰 문자를 지워서 회문인지 보고
#  AABB x
#  ABB x [A]
#  BB o [A, A]

# 그럼 이럴땐 회문이니까
# 최소 앞뒤로 붙여야 하는 문자가 A, A 라는걸 알 수 있음


# AAABB x 
# AABB x [A]
# ABB x [A, A]
# BB o [A, A, A]
# 0, 1, 2

# 팰린드롬이 만들어진다면 그 문자열과 뽑아낸 문자열을가지고
# 문자열을 만들어서
# 새로운 문자열이 회문이 되는지 확인을 해야 할거 같은데


# ABCD 같은 경우 끝까지 회문 판별이 안될 경우
# 즉 리스트가 빌 경우
# 팰린드롬 문자열을 만들지 못함


import itertools
string = list(input())

word = ""
for i in itertools.permutations(string, len(string)):
	list(i).sort(key = lambda x : x[:])
	c = list(i)
	if "".join(c) == "".join(c[::-1]):
		word += "".join(c)
		print(word)
		break
if word == "":
	print("I'm Sorry Hansoo")
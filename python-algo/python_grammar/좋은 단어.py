# import sys
# from collections import deque
# input = sys.stdin.readline


# # 일단 이 문제는 단어가 좋은 단어라는 뜻 자체를 이해하는게 필요하다
# # 좋은 단어라는건 각 단어가 선이 겹치지 않으면서 다른 위치의 있는 같은 글자와 짝지어진다면
# # 그 단어는 좋은 단어라는거다.

# # 그럼 여기서 생각해야될게 두가지있다

# # 1. 선이 중첩되지 않는다는게 뭘까
# # 2. 좋은 단어라는건 그 주어진 단어가 좋은 단어라는것이다 짝지어진 단어가 좋은단어라는게 아니라
# # 1번 조건이 만족 된다면 그 단어는 좋은 단어라는 뜻.


# # 그럼 선이 중첩되지 않는다는게 뭘까..

# # 아래 처럼 3개의 단어가 주어졌다고 하자 그럼 3개의 단어중 어떤 단어가
# # 좋은 단어라고 할 수 있을까

# # 한번 생각해본다면

# ABAB
# AABB
# ABBA


# 1. ABAB 는 글자의 개수는 짝이 맞는다 a : 2, b: 2 이므로 짝이 맞춰질 조건은 만족했다
# 하지만 a를 짝지을려면 b를 통과해야 한다 그럼 한개의 a의 단어는 맞춰지지만
# b의 단어를 맞추려고 할때 선이 중첩되면서 1번 조건을 만족하지 못한다
# 때문에 1번은 '좋은 단어가 ' 아니다.

# 2. AABB 또 한글자의 개수가 a: 2, b: 2로 단어의 짝 조건을 만족한다
# 그럼 1번조건이 만족하는지 봐야 하는데 a를 연결한 짝선과 b를 연결한 짝선이 겹치지 않는다
# 때문에 2번은 1번조건을 만족하는 "좋은 단어 " 이다.

# 3. ABBA 또한 a와 b의 짝조건은 맞춰져있고 a를 연결한 선과 b가 연결한 선은 겹치지 않는다 즉 a의 선이 b의선ㅇ르 포함하는 집합형태처럼 보인다




# AAA
# AA
# AB
# AAA 이건 짝이 맞지 않아 홀수라면 짝이 맞지 않아지지 a가 짝수가 아닌 홀수기 때문이지
# AA 짝이 맞아


# AAAA 이런 상태면 되겠찌
# AA랑 AA랑 묶으면 되니까

# AB 연결할 짝이 없지
# ABBABB
# 이건 되는거지
# a도 짝수 b도 짝수
# 일단 연결될 조건은 맞아
# 근데 이제 이걸 연결이 되냐 안되냐인데
 
# 1. 일단 그 문자의 개수가 모두 짝수인지 확인을해
# 2. 문자의 중첩은 있을 수 있지만 count 는 문자의 개수를 세는것이기 때문에 하나라도 문자의 개수가 홀수가 된다면 그 문자는 더 이상 좋은 단어가아니야

 
# [A, B, B, A]
# [B,B]
# 문자의 길이가 10만

# 주어진 문자의 길이의 총합은 100만을 넘지 않는다,.
# o

# 1. 리스트를 정확히 절반으로 나눠 list1 과 list2 로 나눠준다
# 2. list1 에서 len(list1)-1 and len(list1)-2 의 "".join 값이 AA 또는 BB가 만들어지나 확인한다
# 만약 만들어진다면 리스트에서 삭제해준다.
# 3. 만약 이 과정이 끝났다면 list1 에 list2에서 deque를 이용해 가장 첫번째 값을 list1의 가장 마지막값에 추가한다
# 4. 똑같이 2번과정을 반복한다 그랬을때 맞춰지는 값이 있으면 똑같이 삭제해준다
# 5. 만약 없다면 list2에서 하나더 가지고온다


# 6. 이렇게 했을때 리스트의 내용이 비어잇찌 않다면 좋은 단어가 아니다


import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

arr = [input().strip() for _ in range(n)]

def word_check(word):
	dic = {}
	for i in word:
		if i not in dic:
			dic[i] = 1
		else:
			dic[i] += 1

	isCheck = True
	for i in dic.items():
		if i[1] % 2 != 0:
			isCheck = False
			break
	return isCheck



# 이걸 어떻게 짜면 좋을까
def line_check(word):
	word_len = len(word) // 2
	left = list(word[:word_len])
	right = deque(word[word_len:])

	a = 'AA'
	b = 'BB'

	while True:
		if len(right) == 0:
			if len(left) != 0:
				if "".join(left) == a or "".join(left) == b:
					left.clear()
			break

		if len(left) == 1:
			left.append(right.popleft())

		check = left[len(left)-2] + left[len(left)-1]

		if "".join(check) == a or "".join(check) == b:
			
			left.pop()
			left.pop()
			if len(left) == 0 and len(right) == 0:
				break

			if len(left) == 0 and len(right) != 0:
				left.append(right.popleft())
				continue
		left.append(right.popleft())

	ans = len(left) + len(right)

	return ans

cnt = 0
for i in arr:
	# 단어가 짝이 맞는지 짝이 맞지 않는지 체크
	check = word_check(i)
	# 만약 단어를 검사 했을때 False 가 나온다면
	# 그 단어는 좋은 단어가 아니므로 패스
	if check == False:
		continue

	ans = line_check(i)

	if ans == 0:
		cnt += 1
print(cnt)


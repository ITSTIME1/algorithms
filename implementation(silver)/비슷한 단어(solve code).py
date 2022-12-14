
import copy
n = int(input())
words = [input().rstrip() for _ in range(n)]

word = {}
for w in words[0]:
	if w in word:
		word[w] += 1
	else:
		word[w] = 1

res = 0
for i in range(1, n):
	# 두 가지 경우의 대해서는 단어가 비슷해질 수 없으므로 만들 수 없음
	if len(words[i]) > len(words[0])+1 or len(words[i]) < len(word[0])-1:
		continue
	# 단어가 첫번째 단어 + 1 한거보다 크다면 만약 DOG :3  DOGSS 5 DOG + 1 해도 4인데 5는 2이상 차이나기 때문에
	# 될 수 가 없음 DOG : 3-1 = 2 D OG 가 있어야 하는데 이러면 하나 추가해도 단어가 만들어지지 않으므로 패스
	# deep copy 가 뭐야?
	# 즉 원본 배열을 가지고 와서 복사
	# dic 형식을 딥 카피해서 가지고옴
	check = copy.deepcopy(word)
	for w in words[i]:
		if w in check:
			check[w] -= 1
		else:
			check[w] = -1
	# 1
	# D: 1 0 - 1
	change = [0, 0]
	flag = True
	for c in check:
		if check[0] == 0:
			continue
		# DOG
		# DDO
		if check[c] == 1:
			change[1] += 1
		elif check[c] == -1:
			change[0] += 1
		else:
			flag = False
			break
	# DOG
	# LLL
	# 
	D: 1
	O: 1
	G: 1

	D: -1
	O: -1
	G: -1
	if sum(change) > 2:
		flag = False
	elif change[0] > 2 or change[1] > 2:
		flag = False

	if flag:
		res += 1

print(res)


















# immutable 이란 변경이 안된다
# mutable 은 변경된다
# mutable 의 대표적인 list 를 살펴보면
# a = [1,2,3,4]
# b = a
# 이렇게 한다면 a = [1,2,3,4] 원소가 포함된 객체를 가리키고 있으며
# b 또한 a의 리스트를 가리키고 있다
# 그렇기 때문에
# b[0] = taesun 이라고 바꾼다면 b -> a를 가르키고 있기 때문에
# 결국 가르키는 리스트의 원소를 바꾼 꼴이 된다
# 때문에 a, b 둘다 리스트가 바뀌게 되는 것이다
# 즉 이런걸 a, b는 같은 주소값을 참조한다고 한다
# 즉 같은 주소값을 참조하고 있기 때문에
# 같은 주소값을 참조하고 있는 모든 리스트변수는 전부다 변경이 가능하다
# 그럼 이런 점을 잘못 이용한다면 원본배열은 그대로 두어야 하는데
# 배열이 변경될 경우 크게 잘 못 될 소지가 있기 때문에
# 원본 배열은 그대로 두어야 할 때가 있다


# # deep copy 는 그런 원본배열을 그대로 복사해서 가지고 오는 거네
# a = [1,2,3,4]
# # 깊은 복사가 이루어진것 깊은 복사란 참조된 객체 자체를 복사
# # 얕은 복사는 객체를 새로운 객체로 복사 원본객체의 주소값을 복사
# # 즉 주소값은 같은 곳을 참조하고 있기 때문에 얕은 복사 같은경우
# # 값을 변경하게 되면 참조된 모든 mutable 한 리스트 변수의 값들은 전부다 변경되게 된다 
# # 딮 카피는 원본객체 자체를 완전복사 하기 때문에
# # 결국 참조하는게 아닌 그저 '객체 자체를 복사하낟'

# b = copy.deepcopy(a)

# # copy() 배열도 있는데
# # 이 메서드는 배열의 내부 겍체까지 깊은 복사를 해주지 않음
# b[1] = 0
# print(a)
# print(b)

# # 이렇게 리스트를 매개변수에 원본을 전달
# a = [1,2,3,4]
# b = list(a)

# # 리스트 생성후 원본객체를 extend 매개변수에 전달해서
# # 확장시킨 의미로 전달
# a = [1,2,3,4]
# b = []
# b.extend(a)

# # 파이썬의 문자열 처리 특징 중 하나인 슬라이싱을 이용해서
# # 전체 복사
# a = [1,2,3,4]
# b = a[:]

# # 반복문을 통한 복사 
# a = [1,2,3,4]
# b = [i for i in a]

# # 위 방법들 모두 같은 값을 참조하지 않고
# # 새로운 객체를 만들어 내는데 포커싱 하고 있다는 것이다
# # 그렇기 때문에 결국 각각의 참조값들은 다르고
# # 고유의 mutable 한 객체 변수를 변경하더라도 그 참조값만을 가진
# # mutable 객체만 변경 되게 된다 \ 

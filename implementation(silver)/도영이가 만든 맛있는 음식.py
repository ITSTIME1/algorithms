# 문제분석

# 일단 요구하는건 재료의 신맛과 쓴맛이 주어졌을때
# 신맛과 쓴맛의 차이가 가장 작은걸 만드는게 목표
# 모든 재료를 사용해서 요리를 만들었을때 10억보다 작은 양의정수이다

# N
# S, B

# 재료가 4가지가 주어졌다고 본다며 

# 일단 2, 3, 4 번째 재료를 이용해서 문제에서 적어도 1개 이상의 재료를 사용하라고 했으니까
# 조건은 만족했고
# 그럼 2, 3, 4 를 이용해서 만든 요리의 신맛과 쓴맛을 각각 구해본다면
# 조합된 이 요리의 신맛은 = 각각의 재료의 신맛의 곱 이니까 = 2 * 3 * 4 = 24
# 조합된 이 요리의 쓴맛은 = 각각의 재료의 쓴맛의 합 이니까 = 6 + 8 + 9 = 23
# 그럼 이 조합(2, 3, 4) 의 신맛과 쓴맛의 차이는 = max(s, b) s-b = 1 나오기 때문에
# 차이가 가장 최소로 된다


# 차이가 가장 작은 것만 하면 되니까 그냥 그 중에서 가장 작은 값만선택해도 맞을거 같은데
## 적어도 1개 이상 사용해야 되니까
# 1개를 사용했을떄 
# 2개를 사용했을때
# 3개를 사용했을때
# 4개를 사용했을때

# 1개를 사용했을때
# 1번재료를 사용했을때 신맛 = 1
# 1번재료를 사용했을때 쓴맛 = 7
# 차이는 6

# 2번재료를 사용했을때 신맛 = 2
# 2번재료를 사용했을때 쓴맛 = 6
# 차이는 4

# 3번재료를 사용했을때 신맛 = 3
# 3번재료를 사용했을때 쓴맛 = 8
# 차이는 5

# 4번재료를 사용했을때 신맛 = 1
# 4번재료를 사용했을때 쓴맛 = 7
# 차이는 6


## 2개를 사용했을때 조합이니까 2, 3을 뽑나 3, 2을 뽑나 같은 거


# 1, 2를 사용했을때 신맛은 = 1 * 2 = 2
# 1, 2를 사용했을때 쓴맛은 = 7 + 6 = 13
# 두개의 차이는 11


# 1,3 = 3, 15 = 12
# 1,4 = 4, 16 = 12
# 2,3 = 6, 14 = 8
# 2,4 = 8, 15 = 7
# 3,4 = 12, 17 = 5

## 3개를 사용했을 때
# [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]

# 1, 2, 3 = 6, 22 = 16
# 1, 2, 4 = 8, 22 = 17
# 1, 3, 4 = 12, 24 = 12
## 2, 3, 4 = 24, 23 = 1


# 4개를 이용했을때
# [1,2,3,4]
# 24, 30 = 6

# 이렇게 N까지의 재료를 사용해서 조합해보면
# 각각의 신맛고 쓴맛의 차이가 조합을 적게한다고 가장 작은 수가 나오는게 아니 라는걸 알 수 있고
# 각각의 신맛과 쓴맛은ㅇ 지문대로 각 조합의 신맛의 곱 이고 쓴맛은 각재료의 합이다
# 양의 정수가 나온다고 가정했으니까
# 큰 값에서 작은 값에서 뺀 걸로 출력해주면 답일거 같다
from itertools import combinations

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


# 모든 경우의 수를 다 만들어놓을까?
# N 도 작아서 그냥 다 만들어도 10개를 다 선택하는 경우의 수가지
# 최악의 경우의 경우의 수 가지도 1023 가지 밖에 없어서 널널한 편인데
total = []
cnt = 1

while True:
	if cnt > N:
		break
	for i in combinations(range(1, N+1), cnt):
		total.append(i)
	cnt+=1

result = []
for i in total:
	check = list(i)
	s = 1
	b = 0
	# 이게 키포인트 같네 이 문제는
	for j in check:
		s*=arr[j-1][0]
		b+=arr[j-1][1]
	# 사실상 o,
	max_num, min_num = max(s, b), min(s, b)
	result.append(max_num - min_num)

print(min(result))

# 2
# 3 8
# 5 8
# 1개
# 3 8 = 5
# 5 8 = 3

# 2개
# 15, 16 = 1
# DNA 풀어보자
# 문제 분석
# 이 문제는 빈도수의 문제인데
# 설명이 너무 헷갈리게 되어 있따
# 난 처음에 문자열을 하나씩 비교 해서 distance 를 찾는줄 알았는데 그렇게 되면
# 예제 입력의 나오는 단어가 나오지 않게 된다
# 곰곰히 살펴보니.. s와s1 s와s2 ... s와sn을 비교한다고 되어 있으니
# 그럼 처음부터 n까지 비교하는 것과 같다 그랬을때
# 해밍디스턴스의 길이는 전체문자열의 개수 - 가장 많이 나온 빈도수의 문자열 개수
# 하면 해당 문자들의 해밍 디스턴스의 길이를 알 수 있다 
# 그때의 누적된 값이 해밍 디스턴스의 최소값이 된다
# 또 한가지
# 만약 각각 문자가 한번씩 나왔을 경우 사전순으로 가장 빠른 순으로 출력해야 되니까
# 만약 AGTC 라고 했을때 가장 빠른 문자열이 A 그럼 전체 문자열의 개수 - a의 빈도수 를해주면
# 해밍 디스턴스의 거리가 나온다

N, M = map(int ,input().split())

arr = [input() for _ in range(N)]

result = ""
total = 0
# 시간복잡도는 O(M*N)
for i in range(M):
	word = []
	for j in range(N):
		word.append(arr[j][i])			
	# 문자열 하나를 다 가지고 와서 완성했으니까
	dic = {}
	for c in word:
		dic[c] = 0

	# 문자열의 빈도수를 저장해주고
	for k in word:
		if k in dic:
			dic[k] += 1
	# 우선 value 값을 기준으로 먼저 최대값을 앞으로 최소값을 뒤로 보내주고
	# 그다음 키 값을 기준으로 문자열을 오름차순으로 정렬한다.
	sorted_dict = sorted(dic.items(), key = lambda x: (-x[1], x[0]))

	# 가장 큰값은 가장 앞에 있는 값
	# 가장 작은 값은 가장 뒤에 있는 값으로 정렬
	# 해밍디스턴스
	total += N - sorted_dict[0][1]
	result += sorted_dict[0][0]

print(result, total, sep="\n")
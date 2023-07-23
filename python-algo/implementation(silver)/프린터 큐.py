from collections import deque

T = int(input())

# N = 문서의 개수
# M = 궁금한 현재 문서 위치 이 문서의 위치는 0부터 시작 즉 첫번째가 0 = index 순서

# 뺀것을 다른 리스트에 넣어서
# 내가 기억하고자 하는 리스트의 숫자를 저장해둔뒤
# 그 인덱스가 어느 위치에 있는지 확인하면 될거 같으넫?
# 튜플값으로 그 값이 빠져나갈 위치랑 같이 저장해주면
# 나중에 내가 원하는 값을 찾을때
# 그 순서의 그 값이랑 같은걸 index로 출력하면 되겠다는데?

# O(N)
for i in range(T):
	N, M = map(int, input().split())
	doc = list(map(int, input().split()))
	doc_c = deque()
	for j in range(len(doc)):
		doc_c.append((j, doc[j]))

	# 리스트에서 최대값찾기
	
	total = []
	while True:
		if len(doc_c) == 0:
			break
		first = doc_c[0][1]
		max_num = max(doc)
		if first != max_num:
			ch, ch_1 = doc_c.popleft(), doc.pop(0)
			doc_c.append(ch)
			doc.append(ch_1)
		else:
			chose = doc_c.popleft()
			total.append(chose)
			doc.pop(0)
	

	
	index = 0
	for c in total:
		if c[0] == M:
			index = total.index(c)


	print(index+1)
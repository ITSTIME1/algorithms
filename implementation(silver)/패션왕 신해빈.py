

import itertools
T = int(input())

# t * n * n
# n^2 선에서 끝난다


while T != 0:
	n = int(input())
	dic = {}
	for _ in range(n):
		pro, subj = input().split()
		if subj not in dic:
			dic[subj] = [pro]
		else:
			dic[subj].append(pro)
	# 분류는 했고
	# 범위가 작아서 in 메서드를 사용해도 문제 없이 될거 같음
	
	# 그럼 우선 키가 다 똑같아서 1개밖에 없는 경우들이 있고
	# 키가 2개가 생기는 거지 분류할 항목이 두개이상이라면
	# key 가 한개일때 n을 출력하는 이유는
	# 우선 key가 한개라는건 같은 종류의 것들만 1개이상이라는 얘기가 된다.
	# 따라서 같은 종류의 것들을 하루에하나씩 입는다면
	# 해당 dic.values() 값은 = 0이 될 수 없고 1이상이기에 결국 입력 받은 값이 = 입을 수 있는 날짜가 된다

	if len(dic.keys()) == 1: 
		print(n)
		continue
	if len(dic.keys()) >= 2:
		# 여길 어떻게 할가..
		# 되게 고민이네 이거
		# key+value를 합치는 쪽으로 문자열을 만들자
		arr = []
		for i in dic.items():
			header, string = i[0], ""
			check = i[1]
			for j in check:
				string = header
				arr.append(string)
				string = ""	
		
		index = 1
		ans = set()
		while index <= n-1:
			for i in itertools.permutations(arr, index):
				check = i
				isActive = True
				for j in check:
					if check.count(j) >= 2:
						isActive = False
						break

				if isActive == True:
					ans.add(check)
			print(ans)
			index += 1
	T-=1


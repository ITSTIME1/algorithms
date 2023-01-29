# 문제분석

# 단어 맞추기

# 순열 = n개 중에서 r개를 택한 경우의수
# 중복순열 = n개 중에서 r개를 택해서 나열한것고 중복을 허락하고

# 조합 = n개 주에서 r개를 택하는 경우 뽑는경우
# [e,r,s,t]

# 단어를 나열했을때
# 주어진 단어에서 단어들을 나열했을대
# 그 단어가 중복되게 나오게 되는데 똑같은 단어가 나오게 된다는 것.
# 그것때문 중복된 경우는 제외하기 위해서 set() 자료형을 사용해서
# 해당 중복된 값들을 배제 시킨다.

# permutation 쓰면 편한데...
# 이걸 시간초과 걸어두네..

# 그럼 어떻게 해야할까..


# n! 너무 큰데 그러면 너무 크지 ㅋㅋㅋ
# 그럼 직접구현해야하나..?
# 아 찾아보니까 사전순으로 다음에 올 수를 구하는 알고리즘이라고 한다.

import itertools
t = int(input())




for _ in range(t):
	string = list(input())

	set_list = set()
	for j in itertools.permutations(string, len(string)):
		set_list.add(j)

	arr = [list(_) for _ in set_list]
	arr.sort()

	ans = arr.index(string)
	ans+=1

	if len(arr) == ans:
		ans -= 1

	print("".join(arr[ans]))




# [('B', 'E', 'E', 'R'),
#  ('B', 'E', 'R', 'E'),
#  ('B', 'R', 'E', 'E'), 
#  ('E', 'B', 'E', 'R'), 
#  ('E', 'B', 'R', 'E'), 
#  ('E', 'E', 'B', 'R'), 
#  ('E', 'E', 'R', 'B'), 
#  ('E', 'R', 'B', 'E'), 
#  ('E', 'R', 'E', 'B'), 
#  ('R', 'B', 'E', 'E'), 
#  ('R', 'E', 'B', 'E'), 
#  ('R', 'E', 'E', 'B')]
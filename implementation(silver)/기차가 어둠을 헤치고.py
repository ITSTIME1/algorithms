import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


n, m = map(int, input().split())

train = {str(i): [0]*20 for i in range(1, n+1)}

# 1~n 번 까지의 기차가 있다고 한다
# 그럼 이 기차들을
def first_command(train, seat):
	if train[int(seat)-1] == 0:
		train[int(seat)-1] += 1

	return train

def second_command(train, seat):
	if train[int(seat)-1] == 1:
		train[int(seat)-1] -= 1
	return train

def third_command(train):
	if train[len(train)-1] == 1:
		rotate = deque(train)
		rotate.rotate(1)
		rotate[0] = 0
	else:
		rotate = deque(train)
		rotate.rotate(1)
		
	return rotate


def last_command(train):
	if train[0] == 1:
		rotate = deque(train)
		rotate.rotate(-1)
		rotate[len(rotate)-1] = 0
	else:
		rotate = deque(train)
		rotate.rotate(-1)
	
	return rotate

for i in range(m):
	inp = list(input().split())
	
	if inp[0] == "1":
		# 태우는거
		train[inp[1]] = first_command(train[inp[1]], inp[2])
	elif inp[0] == "2":
		# 하차시키는거
		train[inp[1]] = second_command(train[inp[1]], inp[2])
	elif inp[0] == "3":
		train[inp[1]] = list(third_command(train[inp[1]]))
	else:
		train[inp[1]] = list(last_command(train[inp[1]]))

# 음 이렇게 하면 될거 같은데
# 일단 기록을 저장하는게 필요한데
# 문제는 dic 을 하나씩 가져와서 완전탐색으로 푼다면N이 10만개까지 주어지기 때문에
# 절대로 1초안에 해결은 불가능하고
# 뭔가 방법이 있을거 같은데
# 리스트가 같은걸 찾는다면 이런식으로 찾으면 되겠네
ans = []
for k, v in train.items():
	if v not in ans:
		ans.append(v)

print(len(ans))
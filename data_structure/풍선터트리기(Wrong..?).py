# 코드 다시 짜보자.

import sys

input = sys.stdin.readline

n = int(input())


balloon = list(map(int, input().split()))

dic = {i : False for i in range(n)}



def right(value, index):
	move_index = index+abs(value)

	while True:
		if move_index > len(balloon)-1:
			move_index = 0

		if dic[move_index] == False:
			break

		move_index += 1



	dic[move_index] = True

	# while 문을 통과했다면 그 move_index 는 이동할 값을 찾은것이기 때문에
	return [move_index, balloon[move_index]]




def left(value, index):
	
	move_index = index-abs(value)

	while True:
		if move_index < 0:
			move_index = len(balloon)-1


		if dic[move_index] == False:
			break

		move_index -= 1


	dic[move_index] = True

	# while 문을 통과했다면 그 move_index 는 이동할 값을 찾은것이기 때문에
	return [move_index, balloon[move_index]]



arr = []
pre, index = 0, 0
while len(arr) != n:
	if dic[0] == False:
		dic[0] = True
		arr.append(1)
		pre = balloon[0]
		index = 0

	if pre > 0:
		re = right(pre, index)
		pre = re[1]
		index = re[0]
		arr.append(index+1)
		continue
	else:
		re = left(pre, index)
		pre = re[1]
		index = re[0]
		arr.append(index+1)
print(*arr)	

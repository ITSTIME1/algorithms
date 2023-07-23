# 퀵정렬로 풀면 시간 초과가 나옴 

N = int(input())

array = []
quick_list = []
for i in range(N):
	array.append(int(input()))

def quick_start(array):
	if(len(array) < 1):
		return array

	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x < pivot]
	right_side = [c for c in tail if c > pivot]

	return quick_start(left_side) + [pivot]  + quick_start(right_side)
	
	


quick_list = quick_start(array)

for i in quick_list:
	print(i)	

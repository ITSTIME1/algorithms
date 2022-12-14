array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_start(array):
	if(len(array) < 1):
		return array

	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x < pivot]
	print(left_side)
	right_side = [c for c in tail if c > pivot]
	print(right_side)
	return quick_start(left_side) + [pivot] + quick_start(right_side)
print(quick_start(array))

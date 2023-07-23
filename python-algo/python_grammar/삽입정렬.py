array = [8,4,6,2,9,1,3,7,5]

def insertion_sort(array):
    n = len(array)

`   # 1, 2, 3, 4, 5, 6, 7, 8
    for i in range(1, n):
		for j in range(i, 0, - 1):

            # 4 > 8
            # array 0 > array 1
            # 8 > 4
			if array[j - 1] > array[j]:
				array[j - 1], array[j] = array[j], array[j - 1]
		print(array[:i+1])
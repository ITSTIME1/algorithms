from collections import Counter
import sys
# import time

# start = time.time()
N = int(sys.stdin.readline())

array = [int(sys.stdin.readline()) for i in range(N)]


def quick_start(array):
	if(len(array) < 1):
		return array
`
	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail if x <= pivot]
	right_side = [c for c in tail if c > pivot]

	return quick_start(left_side) + [pivot]  + quick_start(right_side)
new_array = quick_start(array)

# for j in range(N):
# 	min_index = j
# 	for k in range(j+1, len(array)):
# 		if array[min_index] > array[k]:
# 			min_index = k
# 	array[j], array[min_index] = array[min_index], array[j]
# array.sort()
#1
# python 에서 / -> type - float
# // -> type - int
print(round(sum(new_array) / N))
print(new_array[N//2])
cnt = Counter(new_array).most_common(2)
if len(new_array) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(nct[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

print(max(new_array) - min(new_array))
# print(f"{time.time()-start:.1f} sec")
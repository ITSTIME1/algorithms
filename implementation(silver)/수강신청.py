# 뭘 해도 시간초과가 나는데
# hash 로 다시 접근해볼까


# import sys

# dic = {}
# k, l = map(int, sys.stdin.readline().strip().split())

# for i in range(l):
# 	number = sys.stdin.readline().strip()
# 	dic[number] = i

# sorted_dic = sorted(dic.items(), key = lambda item : item[1])


# index = 0
# for i in sorted_dic:
# 	if index == k:
# 		break
# 	print(i[0])
# 	index+=1
	



# import copy
# import sys

# O(2n)
# k, l = map(int, sys.stdin.readline().strip().split())
# arr = []
# for i in range(l):
# 	number = sys.stdin.readline().strip()
# 	arr.append(number)

# # 대기목록에 일단 다 넣어주고

# cpy_arr = arr.copy()
# for i in arr:
# 	if cpy_arr.count(i) >= 2:
# 		c = cpy_arr.index(i)
# 		del cpy_arr[c]

# print(*cpy_arr[:k], sep ="\n")
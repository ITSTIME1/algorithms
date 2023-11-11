# import numpy as np
# print(np)
# print("test")
# # shape 이 같다 = 차원이 같다

# a = np.arange(1, 11).reshape(2, 5)

# b = np.arange(6, 16).reshape(2, 5)

# print(a)
# print(b)

# print(a + b)


# c = np.arange(1, 7).reshape(2, 3)
# d = np.arange(2, 8).reshape(3, 2)


# # array = c.reshape(3, 5, inplace=True)
# # print(arry)

# # print(np.dot(c,d))
# # print(c @ d )
# # # 행렬곱셈은
# # # np.dot(a, b)
# # # a @ b

# # array = np.array([1,2,3,4,5])

# # array = np.append(array, 10)
# # print(array)

# # a = np.array([[1, 2, 3],
# # 			[4, 5, 6]])

# # np.append(a, [[i for i in range(4)] for i in range(3)], axis = 0)
# # np.append(a, [[i] for i in range(4) for c in range(3)], axis = 1)

# # print()

# a = np.arange(24).reshape(3, 4, 2)
# print(a.ravel())

# a.shape(3, 1)
# b.shape(1, 3)
# # 1 .# 1, 3 먼저 확인 둘중에 하나가 1이면 1쪽을 맞춰준다
# # 2 .# 3, 1 둘 중 하나가 1이면 1쪽을 맞춰준다.

# # 즉 오른쪽부터 차례대로 일치하거나, 둘중에하나가 1인경우
# # 브로드캐스팅이 가능해진다.

# import numpy as np


# a = np.arange(5).reshape(1, 1, 5)
# print(a)
# d = a + np.arange(5).reshape(5, 1)
import numpy as np



s = [1,2,3,4,5]
print(s[:])
print(s[:-1])
print(s[::-1])
print(s[1::1])
# 1,1,5
# 1,5,1 (reshape로 인해서 차원이 바뀌었으니까)
# 5열로 바뀌고
# 5행으로 연산이 되니까
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# print(d)
# 0 0 0 0 0
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
filter = lambda x : True if x % 2 == 0 else False
arr = np.arange(10)
# arr = np.arange(10)
# filter(arr)
new_arr = arr[filter]
print(new_arr)


# 브로드캐스팅, 행렬곱, 인덱싱, 슬라이싱
# 선형대수학 관련 함수.


# a = "hello world"

# # hello -> hi로 바꾸면서 문자열의 변경이 일어난다
# s = a.replace("hello", "hi")

# s = "oxoxoxoxoxo"
# sd = s.replace("ox", "*", 1)
# print(sd)



# # 딕셔너리
# d = {'a': 12, 'abc': "blog", 'ff': 3, 43: 'name'}
 
# # 값이 없을때 get 접근

# for i in d:
# 	r1 = d.get("sss")
# 	# 이렇게해서 없는 키값이면 None을 반환하도록 할 수 있따.
# 	if r1 is None:


# # 만약 두번째 주자가 
# a = [[False, False, False], [2, 6, 18]]
# # a.sort(key = lambda x : x[1])

# a.sort(key = lambda x : (x[2], x[1]))
# print(a)


# s = a[0].count(False)
# print(s)



s = [1,2,3,4,5]

for idx, v in enumerate(s, start=1):
    print(idx, v)
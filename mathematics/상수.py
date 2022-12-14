A, B = input().split()

a_re, b_re = list(A), list(B)

# reverse() 함수는 list 타입에서 제공해주는 함수이다.
a_re.reverse()
b_re.reverse()

a_ch = "".join(a_re)
b_ch = "".join(b_re)

if a_ch > b_ch:
	print(a_ch)
else:
	print(b_ch)

	
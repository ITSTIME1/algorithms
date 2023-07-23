A, B = input().split()

a_list = list(A)
b_list = list(B)
a_ch = "".join(a_list[::-1])
b_ch = "".join(b_list[::-1])
print(a_ch if a_ch > b_ch else b_ch)

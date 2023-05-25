import sys

input = sys.stdin.readline

T = int(input())

limit = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(T):
	string = input()

	year = string[:4]
	month = string[4:6]
	day = string[6:]
	# 유효한지 판단을 해야되는거니까

	if int(month) == 0:
		print("#"+str(i+1)+" "+str(-1))
		continue

	if int(day) <= limit[int(month)-1]:
		print("#"+str(i+1)+" "+str(year)+"/"+str(month)+"/"+str(day), end="")
	else:
		print("#"+str(i+1)+" "+str(-1))



# 5
# 22220228
# 20150002
# 01010101
# 20140230
# 11111111
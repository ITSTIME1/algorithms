import sys
import copy
input = sys.stdin.readline

string = list(input().strip())
check_string = copy.deepcopy(string)
check_string.reverse()

# print(string)
# string.reverse()
# print(string)
# if string == string[::-1]:
# 	print(1)
# else:
# 	print(0)
if string == check_string:
	print(1)
else:
	print(0)

# for i in reversed(string):
# 	print(i)


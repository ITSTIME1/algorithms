import sys
from collections import deque
input = sys.stdin.readline



string = deque(input().strip())



new_string = ""
n_string = ""


flag = True

if len(string) == 1 or "X" not in string:
	print("-1")
	flag = False

while True:
	if "." not in string:
		if len(string) % 4 == 0:
			n_string += "AAAA" * (len(string) // 4)

		elif len(string) // 4 == 0 and len(string) % 4 == 2:
			n_string += "BB"
		elif len(string) // 4 == 0 and len(string) % 4 != 2:
			print("-1")
			flag = False
			break

		elif len(string) // 4 >= 1 and len(string) % 4 != 2:
			print("-1")
			flag = False
			break
		elif len(string) // 4 >= 1 and len(string) % 4 == 2:
			n_string += "AAAA" * (len(string) // 4)
			n_string += "BB"
		
			print("-1")
			flag = False
			break

		break


	s = string.popleft()

	if s == "X":
		new_string += s
	else:
		# 점이 들어왔을대
		# XXXXXX
		# 10개짜리
		if len(new_string) % 4 == 0 and new_string != "":
			n_string += "AAAA" * (len(new_string) // 4)
			new_string = ""

		elif len(new_string) // 4 == 0 and len(new_string) % 4 == 2:
			n_string += "BB"

		elif len(new_string) // 4 >= 1 and len(new_string) % 4 != 2:
			print("-1")
			flag = False
			break
		elif len(new_string) // 4 >= 1 and len(new_string) % 4 == 2:
			n_string += "AAAA" * (len(new_string) // 4)
			n_string += "BB"
		elif len(new_string) % 4 != 0:
			flag = False
			print("-1")
			break

		
		new_string = ""
		
		n_string += "."

		

	if not string:
		break
if flag:
	print(n_string)
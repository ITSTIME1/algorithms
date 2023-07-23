from collections import deque
while True:
	try:
		s, t = input().split()
		de_s = deque(s)
		for i in t:
			if len(de_s) != 0 and i == de_s[0]:
				de_s.popleft()
		if len(de_s) == 0:
			print("Yes")
		else:
			print("No")

	except:
		break
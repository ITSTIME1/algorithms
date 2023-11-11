import sys
input = sys.stdin.readline


while True:
	s = list(input().strip())
	if "".join(s) == "END":
		break
	else:
		# 단순 해당 리스트를 뒤섞어주는 함수 reverse()
		# reversed()는 반환함.
		print("".join(reversed(s)))


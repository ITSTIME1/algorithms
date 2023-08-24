import sys
# from string import ascii_lowercase
# from collections import Counter
input = sys.stdin.readline


s = input().strip()
# table = Counter(list(ascii_lowercase))

# for i in s:
# 	table[i] += 1

# # for i in a:
# # 	print(s.count(i), end = " ")

# for i in table.values():
# 	print(i-1, end = " ")




# 아스키 코드 값으로 구할 수 있네
arr = [0] * 26

for i in range(len(s)):
	# 소문자 범위가 97 부터 122까지기 때문에
	# 97로 나누게 되면 97~122까지의 소문자 위치를 얻을 수 있음
	# 결과적으로 s에 있는 각 문자들을 아스키코드 값으로 변경하고
	# 그 변경한 값을 97로 나눠 소문자의 위치 값으로 반환 시킨다음
	# 그걸 a~z에 대응 시키는 리스트로 적용해서 더해 가지고 값을 구하는 방식임
	index = int(ord(s[i]) % 97)
	arr[index] += 1


for i in arr:
	print(i, end = " ")
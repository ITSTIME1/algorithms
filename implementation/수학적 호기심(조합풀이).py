from itertools import combinations
T = int(input())

for i in range(T):
	n, m = map(int, input().split())
	cnt = 0
	for k in combinations(range(1, n), 2):
		r = list(k)
		if float((r[0]**2+r[1]**2+m)/(r[0]*r[1])).is_integer():
			cnt += 1
	print(cnt)
# 정수라는건 0 양의정수 음의정수

# 소수점 뒤에 모두 0이 있는 부동 소수점을 고려해야 하는 경우
# float.is_integer() 기능. 
# 그것은 반환 True 
# float 인스턴스가 정수 값으로 유한하고 False 그렇지 않으면.

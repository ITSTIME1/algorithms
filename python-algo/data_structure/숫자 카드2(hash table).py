# 문제분석 


# 숫자 카드에는 정수가 적혀져 있는 카드가 있다
# 이런 정수가 적혀져 있는 카드를 N개를 가지고 있다


# 정수 M개가 주어졌을때
# 이 M개의 수가 적혀져 있는 숫자 카드를 상근이가 몇 개 가지고 있는지
# 구하는 프로그램을 작성하시오
import sys
# hasp table 

# int 범위내에 해결이 되고 dictionary
n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
m_arr = list(map(int, sys.stdin.readline().strip().split()))


# change in code to not in 
# 752ms ot 732ms
dic = {}
for i in arr:
	# dic[i] == 0 으로 하게 되면
	# dic[i] 값들이 처음에 들어온 값을 제외하게 되기 때문에
	# 주의해야함
	if i not in dic:
		dic[i] = 1
	else:
		dic[i] += 1

print(' '.join(str(dic[i]) if i in dic else '0' for i in m_arr))



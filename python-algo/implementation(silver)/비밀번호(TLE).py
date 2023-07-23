
import sys
input = sys.stdin.readline
n, m = map(int, input().split())


arr = []
if m !=0:
	for _ in range(m):
		c = list(map(int, input().split()))
		for i in c:
			arr.append(i)
# 리스트의 입력은 값이 없다는건 m == 0이라는뜻
# 그럼 이 경우엔 자릿수의 해당하는 모든 값이 정답이 됨

def zero(leng):
	length = leng
	# len = 1 0~9
	# len = 2 00~99
	# len = 3 000~999
	return 10**length

def not_zero(leng, arr):
	# 해당 숫자의 길이만큼 loop를 돌리니까
	# 그 숫자들이 ar 안에 모두다 있냐만 체크하면 되겠
	cnt = 0
	# O(1000만 * 7) = 7000만
	# 7자리에 7개..
	for i in range(0 , 10**leng):
		check = list(map(int, format(i, "0"+str(leng))))
		check_cnt = 0
		for j in arr:
			if check.count(j) >= 1:
				check_cnt += 1

		if check_cnt == len(arr):
			cnt += 1
	return cnt

if len(arr) == 0:
	ans = zero(n)
	print(ans)
else:
	ans = not_zero(n, arr)
	print(ans)



# 1 0
# 10개

# 2 2
# 1 7
# 2개



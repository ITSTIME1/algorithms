

# 1. 합했는데 100 이 되면 그대로 100 출력
# 2. 합하다가 100이 넘는 값 이전 값과
# 3. 그 이후 값을 받고
# 4. 100 기준 값에서 누가 더 가까운지 차이를 계산한후
# 차이가 별로 없는 값까지의 합을 출력
# 만약에 차이 값이 같다면 더 큰 값을 선택 해서 출력.
import sys
N = 10

tmp = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

# 100 - 87 = 13
# 142 - 100 = 42

result = 0
for i in range(N):
	result += tmp[i]

	# 합한 값이 100 보다 커졌다면
	if result > 100:
		p = 100 - (result - tmp[i])
		s = result - 100
		# 만약 이전 값이 더 작다면 작다는건
		# 100 에 더 가깝 다는거기 때문에 더 가까운거 출력
		if p < s:
			result = result-tmp[i]
		# 만약 같은 경우라면 더 큰 값을 선택
		elif p == s:
			# 값 갱신이 중요함 break 이전의 값 갱신을 안한다면
			# 이전 값을 갖고 있기 때문에 주의해야됨.
			result = result
			break
	# 합한 값이 100 이 되었다면
	elif result == 100:
		result == 100
		break
print(result)

# 점수별로 sort()
# n = 나라 번호
# j = 학생 번호
# g = 학생의 성적
N = int(input())
dp = [0] * (N+1)
stu = []
for i in range(N):
	n, j, g = map(int, input().split())
	stu.append((n, j, g))


# 학생성적을 점수가 높은 순서대로 sorting
stu.sort(key = lambda x : (-x[2]))

result = []
for i in range(len(stu)):
	# 메달의 개수가 2개이하라면
	# 건너뛴다.
	if dp[stu[i][0]] >= 2:
		continue
	else:
		dp[stu[i][0]] += 1
		result.append([stu[i][0], stu[i][1]])
	if len(result) == 3:
		break

for i in result:
	print(*i, sep=" ")


# 학생의 소속국가와 점수를 가지고 와서
# 해당 소속국가가 메달을 얼마나 가지고 있는지 확인
# 해당 소속국가가 메달을 2개이하로 가지고 있다면 넘기고
# 다른국가를 검사
# 만약 2개보다 적거나 
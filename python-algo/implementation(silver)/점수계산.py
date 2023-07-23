# 문제분석


# 문제는 총 8문제를 푼다고 한다.

# 점수를 풀었을때 얻는 점수가 있다 

# 풀기시작한 시간 ~ 경과한 시간 과 난이도로 결정한다 = 점수
# 만약 문제를 풀지 못했다면 0점이다


# 참가자의 총 점수는 가장 높은 점수 5개의 합이다.

n = 8

arr = []
for i in range(n):
	num = int(input())
	arr.append((num, i+1))

arr.sort(reverse=True)

maxVal = 0
maxVal_num = []
for i in range(5):
	maxVal += arr[i][0]
	maxVal_num.append(arr[i][1])
maxVal_num.sort()
print(maxVal)
print(*maxVal_num)

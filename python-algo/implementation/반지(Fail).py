# 반지

string = list(input())
N = int(input())

# while
arr = [list(input()) for _ in range(N)]
dp = [False] * N

# i = 7
# j 
# string[i:len(string)+i]
# 10-4= 6+1
for i in range(N):
	for j in range(10-len(string)+1):
		for k in range(len(arr)):
			# 만약에 아니라면
			if "".join(arr[i][j:len(string)+j]) == "".join(string):
				dp[i] = True
	
cnt = 0
for i in range(len(dp)):
	if dp[i] == True:
		cnt += 1
	else:
		result = arr[i]
		first = arr[i][0]
		last = arr[i][9]
		if first in string and last in string:
			# string 에서 last 의 인덱스를 찾고
			# arr 에서 뽑은 last+first 가 
			# string 에 Y+Z랑 같은지 확인
			# last+first YZ
			c = string[string.index(last)]
			z = string[string.index(last)+1]
			
			if last+first == c+z:
				cnt+=1
print(cnt)
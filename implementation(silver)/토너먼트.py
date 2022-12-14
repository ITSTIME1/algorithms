N, K, Y = map(int, input().split())

cnt = 0
while True:
	if K == Y:
		break
	K -= K // 2
	Y -= Y // 2
	cnt += 1
print(cnt)


import math
import sys
#사람수,김지민,임한수
n,kim,lim = map(int,sys.stdin.readline().split())
cnt=0
while True:
    #둘의 반올림이 같은 경우 whil문 끝내기
    if math.ceil(kim)==math.ceil(lim):
        break
    #김지민,임한수/2로 나누고 반올림 한 값 대입
    kim=math.ceil(kim/2)
    lim=math.ceil(lim/2)
    cnt+=1
 
print(cnt)


# 소수, 약수, 최대값, 최소값, 등차수열, 반올림, 올림, 사사오입, 소인수분해, 소수와 합성수
# 최대공약수, 최소공배수, 경우의 수, 순열, 조합
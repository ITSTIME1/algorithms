import time # time 라이브러리 import
start = time.time() # 시작
time.sleep(1) # 측정하고자 하는 코드 부분
 
def solution(s):
	# 문자열로만 판단하는 방법

	answer = 0
	stand = ""
	check = [0, 0]
	while True:
		if len(s) == 0:
			if check[0] != check[1] :
				answer += 1
			break

		if stand == "":
			stand = s[0]
			s = s[1:]
			check[0] += 1
			continue
		else:
			if stand == s[0]:
				check[0] += 1
			else:
				check[1] += 1

			if check[0] == check[1]:
				answer += 1
				stand = ""
				check = [0, 0]

			s = s[1:]

	return answer
solution("aaabbaccccabba")
print(f"{time.time()-start:.4f} sec") # 종료와 함께 수행시간 출력

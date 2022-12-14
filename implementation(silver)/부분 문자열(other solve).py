# 이거 구나
# 문자열 공부를 더해야겠다
# 문자열 이해가 부족해..

while True:
	try:
		s, t = input().split()
		index, value = 0, False
		for i in range(len(t)):
			if t[i] == s[index]:
				index+=1
				# 찾을때마다 인덱스를 올리니까
				# 그 문자를 다 찾았다는 얘기가 됨
				# 인덱스를 올린다 = 그 전 값은 찾았다
				# 때문에 그 s의 문자열끝까지 온다면
				# 문자열을 다 찾은 것
				if index == len(s):
					value = True
					break
		if value:
			print("Yes")
		else:
			print("No")
	except:
		break


import sys
from collections import deque

while True:
    try:
        s, t = input().split()
        queue = deque(list(s))
        # 그럼 큐엔 아무것도 남아있찌 않을거고
        # 큐에 남아있는게 있다면 False 기 때문에
        for c in t:
            if queue and c == queue[0]:
                queue.popleft()
        # 큐가 비어있다면 부분문자열이고
        # 큐가 비어있찌 않다면 부분문자열이 아니다
        if queue:
            print('No')
        else:
            print('Yes')
    except:
        break
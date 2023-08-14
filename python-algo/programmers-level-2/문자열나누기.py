from collections import deque
import time # time 라이브러리 import
start = time.time() # 시작
time.sleep(1) # 측정하고자 하는 코드 부분

def solution(s):    

    same, diff = 0, 0
    answer = 0
    word = deque(s)
    stand = ""
    w = ""
    while True:
        # 단어가 없다면 종료한다.
        if len(word) == 0:
            if same != diff:
                answer += 1
            break
    
        else:  
            if stand == "":
                stand = word[0]
                same += 1
                w += stand
                word.popleft()
                continue

            if stand == word[0]:
                same += 1
            else:
                diff += 1

            w += word[0]
            word.popleft()
            

            if same == diff:
                answer += 1
                w = ""
                stand = ""
                same, diff = 0, 0

solution("banana")
print(f"{time.time()-start:.4f} sec") # 종료와 함께 수행시간 출력

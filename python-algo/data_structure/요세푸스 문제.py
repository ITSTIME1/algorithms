# 문제분석


# 요세푸스 순열 ? - 그게 뭐임;;
# 1번부터 N번까지 N명의사람이 있다고 했을때

# 양의정수 K가 주어지는데
# K = 삭제될 사람 사람의 위치 ex) K = 3 3번째 사람

# 제거되고 나서 남은 사람끼리 또 이 과정을 반복해서 한다
# 언제까지? N명의 사람이 모두 사라졌을 때 까지

# (N, K) - 요세푸스 순열 이라고 한다

# ex) (7, 3) - 이라고 한다면

# 아 이해됐어

# 7명 3번째
from collections import deque
n, k = map(int, input().split())

arr = deque(i for i in range(1, n+1))
re = []
while True:
	if len(arr) == 0:
		break
	for i in range(k-1):
		c = arr.popleft()
		arr.append(c)
	re.append(arr.popleft())

print(str(re).replace('[', '<').replace(']', '>'))
# print("<",", ".join(answer)[:],">", sep='') #출력


# other solve
N,K = map(int,input().split()) #입력받기
arr = [i for i in range(1,N+1)]    #맨 처음에 원에 앉아있는 사람들 리스트

answer = []   #제거된 사람들을 넣을 배열 리스트
num = 0  #제거될 사람의 인덱스 번호

for t in range(N): #반복문 사용
    num += K-1  
    if num >= len(arr):   #한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈  
        num = num%len(arr) 
 
    answer.append(str(arr.pop(num)))
print("<",", ".join(answer)[:],">", sep='') #출력
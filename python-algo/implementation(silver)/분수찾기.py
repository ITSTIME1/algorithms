import sys
import heapq
import math
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline

n = int(input())

line = 0
max_num = 0

while n > max_num:
	line += 1
	max_num += line


# 결국 규칙찾기 문제네 어렵다;;

d = max_num - n
if line % 2 != 0:
	t = d + 1
	b = line - d
	print(str(t) + "/" + str(b))
else:
	t = line - d
	b = d + 1
	print(str(t) + "/" + str(b))


# 표 특성상 규칙을 먼저 찾아야한다

# 우선 지그재그라는게 힌트로 주었다
# 지그재그로 갔을때 4번째를 주의해야하는데
# 4번째가 1/3이 아니가  3/1이다
# 그럼 이걸 유추해봤을때
# 사선의 짝수라인과
# 사선의 홀수라인이 시작하는 방향이 다르다는걸 알 수 있다

# 그럼 사선의 짝수라인을 본다면
# 분자는 1씩 증가, 분모는 1씩 감소

# 사선의 홀수라인은
# 분자는 1씩 감소, 분모는 1씩 증가
# 이런 규칙이 보인다.


# 그럼 규칙을 찾았으니 다시 돌아와서
# 몇번째에 위치한 분수를 찾는게 목적이다
# 그럼 그 분수가 어떤 사선라인의 있는지 알 수 있다면


# 어떠한 관계에 의해서 찾을 수 있을거 같은데
# 만약 내가 찾고자하는 번째가 7번째라면
# 1/4가 출력이 되어야하낟.
# 그럼 이건 4번째 라인에 존재하는 분수이다
# 그럼 첫번째 라인의 분수의 개수 1
# 두번째 라인의 분수의 개수는 2개
# 세번째 라인의 분수의 개수는 3개이다
# 그럼 최대 라인수를 이 라인의 개수로 본다면
# 7번째 분수는 maxLine이 = 10이 될거다
# 그럼 내가 찾고자 하는 분수의 위치가 maxLine보다 작은 공간에 차지한다는걸 알았으니까
# 이 라인을 토대로 생각해보면

# 10번째라는건 그 라인의 가장 큰 분수의 값이 된다.
# 그랬을때 내가 구하고자하는 값은 7번째에 있는값이므로
# 짝수번째 라인에 존재하니까
# 분자가 하나씩 줄어든다는걸 생각하고
# 10-7 = 3차이가 3나니까
# 차이를 = d라고 했을떄
# 분자가 하나씩 줄어들려면
# n=7
# max=10
# line=4
# line - d 차이만큼빼게 되면
# 분자가되고
# d + 1하게 되면 분모가 되니까
# 분모는 항상 d의 값의 의해 줄어들고
# 분모는 항상 1씩 증가하는 형태가 될 수 있네
# 그럼 이거의 반대니까
# 분자 분모에 식을 반대로 적용시킨다면 가능할거 같은데?





X=int(input())

line=1
while X>line:
    X-=line
    line+=1
    
if line%2==0:
    a=X
    b=line-X+1
else:
    a=line-X+1
    b=X
    
print(a, '/', b, sep='')

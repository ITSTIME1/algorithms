import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline


# 카드에 적힌 단얻릉르 사용해 원하는 순서의 단어 배열을 만들 수 있나 ?

# 두 카드 뭉치고 주어지고
# 원하는 카드배열이 주어졌다고 한다

# 두 카드 뭉치를 가지고 goal 를 만들 수 있다면 yes
# 만들 수 없다면 No를 리턴해보자

# 그럼 스택에서 하나씩 단어를 빼가지고
# 가장 앞의 있는 단어들을 조합했을때
# 저 단어가 만들어지나 확인해야겠네?

# 카드는 순서대로 사용해야 된다는 조건이 있으니까
# 2번예시처럼 drink 와야 하는 상황에서 water가 먼저 와버리게 되면
# 순서가 맞지 않으므로 만들 수 없는게 되는거지

# 또한 한 번 사용한 카드는 재사용이 안되니까 빼주어야하는거고
# 순서를 바 꿀 수없으니 정렬을 해서는 안되고
# 스택의 관련된 문제?
# 디큐인거같은데


cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]


c1 = deque(cards1)
c2 = deque(cards2)
g = deque(goal)

g_word = "".join(g)
answer = ""

while len(g) != 0:

	if len(g) == 0:
		break

	word = g.popleft()
	if len(c1) != 0 and word == c1[0]:
		c1.popleft()
		answer += word
		continue
	elif len(c2) != 0 and word == c2[0]:
		c2.popleft()
		answer+= word
		continue
	else:	
		answer = "No"
		break

if answer == g_word:
	answer = "Yes"
else:
	answer = "No"


print(answer)



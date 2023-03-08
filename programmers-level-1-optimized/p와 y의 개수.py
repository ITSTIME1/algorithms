import sys
import heapq
from collections import deque
from itertools import permutations, combinations, product, combinations_with_replacement
input = sys.stdin.readline




# 이 코드의 핵심은 lower()함수를사용해서 문제의 제시된 내용을 잘 활용한 예시다
# 왜냐하면 문제에서 대문자와 소문자의 구분은 없다고 했으므로 모두다 upper() 혹은 lower()로 만든다음 개수를 비교하면 되기 때문이다.

# 또하나 count()함수를 이용해서 이 s문자열에 있는 lower()로 변환된 p의 문자의 개수를 구한다는 것이다.
# lower() + count() 조합을 사용해 특정 문자의 개수를 찾고 있다.
# 또한 p와 y의 개수가 같으면 True를 그렇지 않다면 False 만약 p와 y가 하나도 없다면 false를


# pPoooyY
s = "abc"
a = s.lower().count('p') == s.lower().count('y')

# 첫번째 예시를 통해서 p의 개수와 y의 개수가 같으므로 True값을 리턴하는걸 볼 수 있고
# 두번째 예시를 통해서 p와 y의 개수가 다르므로 False를 리턴하는걸 볼 수 있다.
# 그럼 마지막 p와 y가 없다면 어떻게 될까? p와 y가 모두 하나도 없는 경우는 항상 True를 리턴하라고 되어있다. 
# 위 abc 예제를 통해서 유추해볼 수 있다.
# abc에는 현재 p와 y문자 모두 들어있지 않고, 그로인해 p의 개수 = 0, y의 개수 = 0 이기 떄문에 둘다 0으로 같아 첫번째 조건인 두 문자의 개수가 같으면 True를 리턴하라는 조건의 부합한다.
# 때문에 두 문자가 하나도 없어도 True를 리턴하는 것이다.

# 조금더 생각해보면 문자열에서 해당 문자의 개수가 몇개나 들어있는지 찾을때 count() 함수를 이용한다면 쉽게 찾을 수 있을 것 같다.
# 이렇게 총 abc의 문자 3개를 찾을 수 있는 걸 볼 수 있다.
c = "abccabccabc"
ans = c.count("abc")
print(ans)


# 문자열이 길고 복잡하더라도 abcd 라는 단어를 정확히 찾아낸다.
s = "abcddddddddabcdddabcddd"
ans1 = s.count("abcd")
print(ans1)

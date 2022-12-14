from collections import Counter
import sys
N = 10
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

cnt = Counter(arr)
# most_common method 는 내림차순으로 정렬


# 각 리스트를 구성하는 튜플에서 튜플의 첫번재 요소는 list에 있는 숫자고
# 튜플의 두번째 값은 해당 숫자가 얼마나 나왔는지 count 한 값이다

# >>> cnt.most_common(3)
# [(4, 3), (3, 2), (5, 2)]


# 그럼 최빈값 = 빈도수가 많은 값을 찾아야 하기 때문에
# 딕셔너리 형태로 결과물을 받아오면
# 각 해당 숫자들이 얼마나 많은 빈도를 가지고 있는지
# 나타내주고 있고
# most_common() 매개변수를 지정해주지 않았다면
# counter 값을 내림차순으로 보여주게 된다.


# most_common 에 1 을 부여하게 되면
# 첫번째로 큰 값만을 보여주게 된다
count = cnt.most_common(1)

print(sum(arr) // len(arr))
print(count[0][0])


from itertools import product
sets = [1,2,3]
#2개를 뽑아 일렬로 나열하는 경우의 수(단, 중복 허용)
data = list(product(sets, repeat = 3))
print(data)

# product 함수 자체가 첫번째 인자로 iterable 반복가능한 객체를 받고
# repeat = 반복 횟수를 지정해주는 인자를 넣어주면 그만큼을 반복 가능한 객체로 만들어준다



# 중복 조합
# 반복가능한 객체 n 에서 r개를 뽑아서
# 중복을 허용해서
from itertools import combinations_with_replacement

for cwr in combinations_with_replacement([1,2,3,4], 2):
    print(cwr, end=" ")

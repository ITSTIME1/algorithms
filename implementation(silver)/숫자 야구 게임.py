import itertools

# 만약 1, 2, 3 이 2스트라이크 1볼이라고 가정했을때
# 1, 2가 스트라이크 자리라고 가정한다면
# 1,2,3 은 2스트라이크 1볼이되고
# 만약이걸 순서를 고려하지 않는다면
# 2,1,3 이런식으로 된다면
# 0스트라이크 3볼이 되기 때문에
# 순서가 달라짐에 따라 값이 달라지기 때문에 
# 달라지면 안된다
# 따라서 순서를 고려하면서 완전탐새으로 풀어야하는 문제이다.
data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(itertools.permutations(data, 3))
print(num)
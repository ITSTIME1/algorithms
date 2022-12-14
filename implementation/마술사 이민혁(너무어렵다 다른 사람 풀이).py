R, C = map(int, input().split())
data = [list(map(str, input())) for _ in range(R)]
A, B = map(int, input().split())
err = {'#': '.', '.': '#'}

print(data)

# for i in data:
#     # 가지고온 리스트 값의 요소를 반대로 가지고온다.
#     # 슬라이싱의 기본은 i[start:end:step] 
#     # 예를 들어 >>> a = ['a', 'b', 'c', 'd', 'e']
#     # a[ 3 : : -1 ]

#     # 이런식으로 된다면 start = 3 이기 때문에
#     # 인덱스 위치의 3번째 위치부터 
#     # 끝은 정해져 있지 않으면서
#     # step = - 1이기 때문에
#     # 3 이전에 있는 값들을 역순으로 출력한다.
#     # 만약 끝이 정해져 있다면 거기까지 역순으로 출력한다.
#     print(i[::-1])



for row in data:
    row.extend(row[::-1])

# extend 되어진 data 값을 볼 수 있다.
print(data)
tmp = []
# reversed() 함수는 역방향으로 접근

for row in reversed(data):
    print(row)
    tmp.append(list(row))
    print(tmp)
data.extend(tmp)
print(data)

data[A-1][B-1] = err[data[A-1][B-1]]

for row in data:
    print(*row, sep='')

# 얕은 복사 그리고 이런 방법을 어떻게 생각했는지 공부해보자

# 복사를 하지 않아도 구현해 낼 수 있음


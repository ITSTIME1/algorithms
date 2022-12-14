# 우선 N * N 의 칸이 만들어지고
# N 이 짝수이든 홀 수 이든 당근을 놓는 위치나 개수는 큰 차이가 없다
# 변이 마주하고 있는 곳은 놓을 수 없기 때문에 4가지 대각선 방향으로만 당근을 놓을 수 있으며
# 우선 먼저 놓아지는 당근의 위치가 중요한데
# 당근위 위치R, C 가 짝홀 혹은 홀짝 혹은 홀홀 혹은 짝짝 이런 경우가 있다
# (1,1) 이 칸의 가장 첫 지점이며
# 이 경우 홀 홀 이기 때문에 1,1 에 당근을 놓았다면 1은 홀수 이기 때문에 홀에는 홀에만 둘 수 있다
# 반대로
# (2, 2) 일 경우 2는 짝이기 때문에 짝에다가만 놓는다면 N이 4일경우 2, 4에만 놓을 수 있다.


# 만약 (1, 4) 홀 짝 이라면 홀수 이면서 짝에다가 두면 된다.

# 쯕 홀 수 이면서 짝수냐 홀 수 이냐가 중요한 관건이다
# 홀 수 이고 홀 수 라면 짝수에다가 둘 수 없고 홀수 에다가만 둘 수 있기 때문이고
# 홀 수 이면서 짝수에다 놓았다면 짝수에다가만 둘 수 있기 때문이다.

N, R, C = map(int,input().split())


# R+C 먼저 심은 곳이 (2, 3) 이라면 짝수이면서 홀 수 이기 때문에
# 그게 짝수라면
if (R + C) % 2 == 0:
    for i in range(N):
    	# 0부터 시작하기 때문에
    	# 현재 2, 3은 짝수이면서 index 위치가 2가 == 0 이 되기 때문에
    	# 만약 나머지가 1이라면
    	# 반대로 짝수가 된다면 .v 모양으로 되어야 한다.
    	# 심는 위치에따라 개수가 달라지지 않기에
    	# 심는 위치에 따라 달라진다는게 포인트이다.


    	# 이런 문제는 한번 심는 위치가 주어졌기 때문에
    	# 심는 위치에 따라서 어떻게 변하는지 패턴을 찾아야 하며
    	# 그 심는 위치가 짝수나 홀 수 일때 변화가 되는지 찾아보아야 한다.
        if i % 2 == 0:
            print("v." * (N // 2) + 'v' * (N % 2))
        else:
            print(".v" * (N // 2) + '.' * (N % 2))
            
else:
    for i in range(N):
        if i % 2 == 1:
            print("v." * (N // 2) + 'v' * (N % 2))
        else:
            print(".v" * (N // 2) + '.' * (N % 2))
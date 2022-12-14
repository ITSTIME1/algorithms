N, M = map(int, input().split())
J = int(input())
app = [input() for _ in range(J)]

num = [_ for _ in range(1, N+1)]
# [1, 5, 3]
c = num[:M]
max_num = max(c)
min_num = min(c)

cnt = 0
for i in app:
	if min_num <= int(i) <= max_num:
		cnt+=0
	elif int(i) > max_num:
		re = int(i) - max_num
		cnt+=re
		max_num+=re
		min_num+=re
	elif int(i) < min_num:
		re = min_num - int(i)
		cnt += re
		max_num-=re
		min_num-=re
print(cnt)

# M == 1 일때와 1이 아닐때로 나눠보ㅕㅁㄴ

# M == 2
# [1,2,3,4,5]

# [1,5,3]
# 처음 왼쪽 M 칸을 차지 하고 있으므로 [1,2]
# 순서대로 사과를 담는거니까 1번째가 가장큰 값안에 포함되면 cnt += 0
# 그다음 사과를 가지고 왔을때 max(arr) == 2 인데 < 5 다음값이 5이므로 오른쪽으로 이동해야됨
# 즉 현재 가장 큰 값보다 다음 사과 위치가 크다면 오른쪽 위치로 이동
# 이때 이동할 사과의 위치 - max(arr)=2 = 3 cnt+=3 이동횟수를 갱신
# 그리고 나서 최대값과 최소값을 각각 이동한 만큼 갱신 [4,5]
# 그리고 나서 다음 사과의 위치를 가지고 왔을때 max(arr) = 5인 값보다 크면 오른쪽
# 포함 되어있다면 cnt+=0 그렇지 않고 작다면 min(arr) = 4 랑 비교해서
# 해당 값보다 얼마나 작은지 확인 현재 최소값 min(arr) = 4 - 사과의 위치 = 1
# cnt += 1 갱신
# 그리고 나서 왼쪽으로 이동했으므로 각각 -1 씩 해줌 [3,4]









